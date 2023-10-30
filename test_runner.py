import numpy as np
import cv2
import os
import json
import time
import socket
import datetime
import config
from subprocess import Popen
from pathlib import Path
from Generators.Util.mtc_generator import MTCGenerator

class TestRunner():
    def __init__(self, generator: MTCGenerator):
        self.generator = generator
        self.main1 = "main1.cpp"
        self.main2 = "main2.cpp"
        self.firmware1 = "firmware1.elf"
        self.firmware2 = "firmware2.elf"
        self.screenshot1 = "screenshot_1.png"
        self.screenshot2 = "screenshot_2.png"
        self.diff = "diff.png"

    def run(self, timeout, ignore_fail = True):
        # timeout in seconds
        tests = []
        idx = 0
        failed_cases = []
        passed_cases = []
        timedout = True
        startdate = datetime.datetime.now()
        start = time.time()
        while time.time() < (start+timeout):
            idx += 1
            path = config.PATHS['TESTCASES']+self.generator.name+'/'+str(idx)
            Path(path).mkdir(parents=True, exist_ok=True)
            os.chdir(path)
            
            self.generator.generate_mtc()

            try:
                compiletime = time.time()
                self.compile(self.main1, self.firmware1)
                self.compile(self.main2, self.firmware2)
                compiletime = time.time() - compiletime
            except RuntimeError as error:
                print('[ERROR] An error occured while compiling test {}: {}! A new test will be generated.'.format(idx, error))
                idx -= 1 # generate test again with same id
                continue

            runtime = time.time()
            self.run_vp(self.firmware1, self.screenshot1)
            self.run_vp(self.firmware2, self.screenshot2)
            runtime = time.time() - runtime

            equal = self.analyze()
            passed = not (equal ^ self.generator.should_be_equal)

            tests.append({
                "id": idx,
                "passed": passed,
                "compiletime": round(compiletime, 2),
                "runtime": round(runtime, 2)
            })
            if not passed:
                failed_cases.append(idx)
                if not ignore_fail:
                    timedout = False
                    break
            else:
                passed_cases.append(idx)

        runtime = time.time() - start
        results = {
            "relation": self.generator.name,
            "should_be_equal" : self.generator.should_be_equal,
            "host": socket.gethostname(),
            "starttime": startdate.isoformat(),
            "endtime": datetime.datetime.now().isoformat(),
            "total_runtime": str(datetime.timedelta(seconds=runtime)),
            "avg_compiletime_pc": round(sum(d['compiletime'] for d in tests) / len(tests), 2),
            "avg_runtime_pc": round(sum(d['runtime'] for d in tests) / len(tests), 2),
            "timeout": timedout,
            "ignore_fail": ignore_fail,
            "number_of_tests": idx,
            "number_failed": len(failed_cases),
            "number_passed": idx - len(failed_cases),
            "failed_cases": str(failed_cases), # cast to str in order to avoid indentation - a bit ugly
            "test": tests
        }

        with open(config.PATHS['TESTCASES']+self.generator.name+".json", "w") as outfile:
            outfile.write(json.dumps(results, indent=4))


    def compile(self, code_file, firmware_file):
        compile = [config.PATHS['GCC'], '-o', code_file+'.o', code_file]
        compile.extend(config.BUILD['COMPILE'].split())

        compile_p = Popen(compile)
        compile_p.communicate()[0]
        compile_p.wait()
        if compile_p.returncode:
            raise RuntimeError('unable to compile firmware')

        link = [config.PATHS['GCC'], '-o', firmware_file, code_file+'.o']
        link.extend(config.BUILD['LINK'].split())

        link_p = Popen(link)
        link_p.communicate()[0]
        link_p.wait()
        if link_p.returncode:
            raise RuntimeError('unable to link firmware')


    def run_vp(self, firmware_file, screenshot_file):
        screenshot = Path(screenshot_file)
        if screenshot.is_file():
            screenshot.unlink()

        vp = Popen([config.PATHS['VP'], '--wait-for-gpio-connections', firmware_file])
        gui = Popen([config.PATHS['GUI'], '--platform', 'offscreen'])

        """
        GUI/VP doesn't close when FW is finished hence we wait
        for the last screenshot and then terminate the process
        TODO think of a better way to do this
        """
        while not screenshot.is_file():
            pass

        time.sleep(1)

        gui.terminate()
        vp.terminate()


    def analyze(self) -> bool:
        """Load two RGBA images. For each pixel: 
        if there is a difference in one or more channels, output 255 else 0. 
        In the final image white pixels indicate a difference."""
        img1 = cv2.imread(self.screenshot1, cv2.IMREAD_UNCHANGED)
        img2 = cv2.imread(self.screenshot2, cv2.IMREAD_UNCHANGED)

        diff = np.where(img1[:, ..., [0, 1, 2, 3]] != img2[:, ..., [0, 1, 2, 3]], 255, 0)
        diff = np.where(np.sum(diff, axis=2) > 0, 255, 0)
        cv2.imwrite(self.diff, diff)

        return bool(np.all(np.equal(img1, img2)))
