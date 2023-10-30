from abc import ABC, abstractmethod
import Generators.Util.file_gen


class MTCGenerator(ABC):
    def __init__(self, path='', name=''):
        self.path = path
        self.name = name
        self.args = {}
        self.should_be_equal = True

    @abstractmethod
    def source_testcase(self, cpp):
        pass

    @abstractmethod
    def followup_testcase(self, cpp):
        pass

    @abstractmethod
    def random_args(self):
        pass

    def generate_mtc(self):
        self.random_args()
        self.generate_file(self.path+"main1.cpp", 1, self.source_testcase)
        self.generate_file(self.path+"main2.cpp", 2, self.followup_testcase)

    def generate_file(self, src_path, screenshot_num, testcase_fn):
        cpp = Generators.Util.file_gen.CppFile(src_path)
        cpp("#include \"TFT_eSPI.h\"")
        with cpp.block("int main()"):
            cpp("TFT_eSPI tft = TFT_eSPI();")
            cpp("tft.init();")
            testcase_fn(cpp)
            cpp("tft.writecommand(0xFF);")
            cpp(f"tft.writedata16({screenshot_num});")
            cpp("return 0;")
        cpp.close()
