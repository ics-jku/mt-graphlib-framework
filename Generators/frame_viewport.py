import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator


class FrameViewport(MTCGenerator):
    def __init__(self, path='', name="frameViewport"):
        super(FrameViewport, self).__init__(path, name)

    def source_testcase(self, cpp):
        cpp(f"tft.setViewport({self.args['posx']},{self.args['posy']},{self.args['sizex']},{self.args['sizey']});")
        cpp(f"tft.frameViewport({self.args['color']},{self.args['in_out']});")

    def followup_testcase(self, cpp):
        if self.args["sizex"] == 0 or self.args["sizey"] == 0:
            return
        if self.args["in_out"] == 1:
            cpp(f"tft.drawRect({self.args['posx']},{self.args['posy']},{self.args['sizex']},{self.args['sizey']},{self.args['color']});")
        if self.args["in_out"] == -1:
            cpp(f"tft.drawRect({(self.args['posx']-1)},{(self.args['posy']-1)},{(self.args['sizex']+2)},{(self.args['sizey']+2)},{self.args['color']});")

    def random_args(self):
        constraints = Generators.Util.constraints.viewport
        self.args = {}
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])
        self.args["in_out"] = random.choice([-1,1])
