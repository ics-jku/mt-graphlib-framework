import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator


class DrawPixel(MTCGenerator):
    def __init__(self, path='', name="drawPixel"):
        super().__init__(path, name)
        self.args = []

    def source_testcase(self, cpp):
        for x, y, c in self.args:
            cpp(f"tft.drawPixel({x},{y},{c});")

    def followup_testcase(self, cpp):
        for x, y, c in reversed(self.args):
            cpp(f"tft.drawPixel({x},{y},{c});")

    def random_args(self):
        constraints = Generators.Util.constraints.drawPixel
        used_coords = set()
        self.args = []
        for _ in range(random.randrange(*constraints["pixels"])):
            while True:
                x = random.randrange(*constraints["x"])
                y = random.randrange(*constraints["y"])
                if (x, y) in used_coords:
                    continue
                used_coords.add((x, y))
                c = random.randrange(*constraints["color"])
                self.args.append((x, y, c))
                break
