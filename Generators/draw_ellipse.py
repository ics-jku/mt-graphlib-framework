import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator

class DrawEllipse(MTCGenerator):
    def __init__(self, path='', name="drawEllipse"):
        super(DrawEllipse, self).__init__(path, name)

    def source_testcase(self, cpp):
        cpp(f"tft.drawEllipse({self.args['x']},{self.args['y']},{self.args['r']},{self.args['r']},{self.args['color_fg']});") 

    def followup_testcase(self, cpp):
        cpp(f"tft.drawCircle({self.args['x']},{self.args['y']},{self.args['r']},{self.args['color_fg']});") 

    def random_args(self):
        constraints = Generators.Util.constraints.fill_draw_Circle
        self.args = {}
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])
