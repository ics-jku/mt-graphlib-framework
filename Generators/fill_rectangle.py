import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator


class FillRectangle(MTCGenerator):
    def __init__(self, path='', name="fillRectangle"):
        super(FillRectangle, self).__init__(path, name)

    def source_testcase(self, cpp):
        if self.args["function"] == 1:
            cpp(f"tft.fillSmoothRoundRect({self.args['posx']},{self.args['posy']},{self.args['sizex']},{self.args['sizey']},{self.args['radius']},{self.args['color']},0);")
        elif self.args["function"] == 2:
            cpp(f"tft.fillRoundRect({self.args['posx']},{self.args['posy']},{self.args['sizex']},{self.args['sizey']},{self.args['radius']},{self.args['color']});")

    def followup_testcase(self, cpp):
        cpp(f"tft.fillRect({self.args['posx']},{self.args['posy']},{self.args['sizex']},{self.args['sizey']},{self.args['color']});")

    def random_args(self):
        constraints = Generators.Util.constraints.rectangle
        self.args = {}
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])
        self.args["function"] = random.randrange(1,3)
