import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator


class ViewportUnequal(MTCGenerator):
    def __init__(self, path='', name="viewportUnequal"):
        super(ViewportUnequal, self).__init__(path, name)
        self.should_be_equal = False

    def fn0(self, cpp):
        cpp(f"tft.fillRect({(self.args['posx']-self.args['offset'])},{(self.args['posy']-self.args['offset'])},{(self.args['sizex']+(self.args['offset']*2))},{(self.args['sizey']+(self.args['offset']*2))},{self.args['color']});")
        
    def source_testcase(self, cpp):
        self.fn0(cpp)

    def followup_testcase(self, cpp):
        cpp(f"tft.setViewport({self.args['posx']},{self.args['posy']},{self.args['sizex']},{self.args['sizey']},false);")
        self.fn0(cpp)

    def random_args(self):
        constraints = Generators.Util.constraints.viewport_unequal
        self.args = {}
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])
