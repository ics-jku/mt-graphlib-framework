import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator


class DrawRectangle(MTCGenerator):
    def __init__(self, path='', name="drawRectangle"):
        super(DrawRectangle, self).__init__(path, name)

    def source_testcase(self, cpp):    
        cpp(f"tft.drawRoundRect({self.args['posx']},{self.args['posy']},{self.args['sizex']},{self.args['sizey']},{self.args['radius']},{self.args['color']});")

    def followup_testcase(self, cpp):
        cpp(f"tft.drawRect({self.args['posx']},{self.args['posy']},{self.args['sizex']},{self.args['sizey']},{self.args['color']});")

    def random_args(self):
        constraints = Generators.Util.constraints.rectangle
        self.args = {}
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])
