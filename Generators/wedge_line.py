import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator


class WedgeLine(MTCGenerator):
    def __init__(self, path='', name="wedgeLine"):
        super(WedgeLine, self).__init__(path, name)

    def source_testcase(self, cpp):
        cpp(f"tft.drawWedgeLine({self.args['x2']},{self.args['y2']},{self.args['x1']},{self.args['y1']},{self.args['r2']},{self.args['r1']},{self.args['color_fg']},{self.args['color_bg']});")

    def followup_testcase(self, cpp):
        cpp(f"tft.drawWedgeLine({self.args['x1']},{self.args['y1']},{self.args['x2']},{self.args['y2']},{self.args['r1']},{self.args['r2']},{self.args['color_fg']},{self.args['color_bg']});")

    def random_args(self):
        constraints = Generators.Util.constraints.wedgeLine
        self.args = {}
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])
