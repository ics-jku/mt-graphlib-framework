import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator


class FillScreen(MTCGenerator):
    def __init__(self, path='', name="fillScreen"):
        super(FillScreen, self).__init__(path, name)
        self.should_be_equal = False

    def source_testcase(self, cpp):
        cpp(f"tft.fillScreen({self.args['color']});")

    def followup_testcase(self, cpp):
        cpp(f"tft.fillScreen({(self.args['color']+1)});")

    def random_args(self):
        constraints = Generators.Util.constraints.fillScreen
        self.args = {}
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])
