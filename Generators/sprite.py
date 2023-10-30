import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator


class Sprite(MTCGenerator):
    def __init__(self, path='', name="sprite"):
        super(Sprite, self).__init__(path, name)

    def source_testcase(self, cpp):
        cpp("TFT_eSprite spr = TFT_eSprite(&tft);")
        cpp(f"spr.createSprite({self.args['sizex']}, {self.args['sizey']});")
        cpp(f"spr.fillRect(0,0,{self.args['sizex']},{self.args['sizey']},{self.args['color']});")
        cpp(f"spr.pushSprite({self.args['posx']},{self.args['posy']});")

    def followup_testcase(self, cpp):
        cpp(f"tft.fillRect({self.args['posx']},{self.args['posy']},{self.args['sizex']},{self.args['sizey']},{self.args['color']});")

    def random_args(self):
        constraints = Generators.Util.constraints.sprite
        self.args = {}
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])
