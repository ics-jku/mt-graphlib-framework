import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator

"""
Drawing a full arc/circle (0-360deg) with inside radius 0 & with anti-aliasing
using drawArc() should be the same as fillSmoothCircle().
This is not (always) the case, they differ by a few pixels, due to 
the different ways they are calculated/implemented.
But mathematically speaking, they should yield the same result.
"""

class FillSmoothCircle(MTCGenerator):
    def __init__(self, path='', name="fillSmoothCircle"):
        super(FillSmoothCircle, self).__init__(path, name)

    def source_testcase(self, cpp):
        cpp(f"tft.fillSmoothCircle({self.args['x']},{self.args['y']},{self.args['r']},{self.args['color_fg']},{self.args['color_bg']});") 

    def followup_testcase(self, cpp):
        cpp(f"tft.drawArc({self.args['x']},{self.args['y']},{self.args['r']},0,0,360,{self.args['color_fg']},{self.args['color_bg']}, true);")

    def random_args(self):
        constraints = Generators.Util.constraints.fill_draw_Circle
        self.args = {}
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])

