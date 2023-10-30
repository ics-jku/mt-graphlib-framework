import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator

"""
Drawing a full arc/circle (0-360deg) using drawArc() with thickness=1 (ir=r-1) 
wit anti-aliasing should yield the same result as drawSmoothCircle().
This seams to hold.
"""

class DrawSmoothCircle(MTCGenerator):
    def __init__(self, path='', name="drawSmoothCircle"):
        super(DrawSmoothCircle, self).__init__(path, name)

    def source_testcase(self, cpp):
        cpp(f"tft.drawSmoothCircle({self.args['x']},{self.args['y']},{self.args['r']},{self.args['color_fg']},{self.args['color_bg']});") 

    def followup_testcase(self, cpp):
        cpp(f"tft.drawArc({self.args['x']},{self.args['y']},{self.args['r']},{(self.args['r']-1)},0,360,{self.args['color_fg']},{self.args['color_bg']}, true);")

    def random_args(self):
        constraints = Generators.Util.constraints.fill_draw_Circle
        self.args = {}
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])
