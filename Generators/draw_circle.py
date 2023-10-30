import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator

"""
Drawing a full arc/circle (0-360deg) using drawArc() with thickness=1 (ir=r-1) 
without anti-aliasing should yield the same result as drawCircle().
This does not hold. The circles are different in shape and color.

Shape difference is due to the different ways they are calculated/implemented.
But mathematically speaking, they should yield the same result.

Color difference is due to drawArc() using alphablending().
Is needed for anti-aliasing but should not be used when anti-aliasing is turned off.
"""

class DrawCircle(MTCGenerator):
    def __init__(self, path='', name="drawCircle"):
        super(DrawCircle, self).__init__(path, name)

    def source_testcase(self, cpp):
        cpp(f"tft.drawCircle({self.args['x']},{self.args['y']},{self.args['r']},{self.args['color_fg']});") 

    def followup_testcase(self, cpp):
        cpp(f"tft.drawArc({self.args['x']},{self.args['y']},{self.args['r']},{(self.args['r']-1)},0,360,{self.args['color_fg']},TFT_WHITE, false);")

    def random_args(self):
        constraints = Generators.Util.constraints.fill_draw_Circle
        self.args = {}
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])

