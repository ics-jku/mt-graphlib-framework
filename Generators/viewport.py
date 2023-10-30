import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator


class Viewport(MTCGenerator):
    def __init__(self, path='', name="viewport"):
        super(Viewport, self).__init__(path, name)

    def rect(self, cpp):
        cpp(f"tft.fillRect({(self.args['posx']+self.args['offset'])},{(self.args['posy']+self.args['offset'])},{(self.args['sizex']-(self.args['offset']*2))},{(self.args['sizey']-(self.args['offset']*2))},{self.args['color']});")

    def source_testcase(self, cpp):
        cpp(f"int32_t a = {(random.randrange(-2147483648,2147483648))};")
        cpp(f"int32_t b = {(random.randrange(-2147483648,2147483648))};")
        cpp(f"int32_t c = {(random.randrange(-2147483648,2147483648))};")
        cpp(f"int32_t d = {(random.randrange(-2147483648,2147483648))};")
        cpp("tft.clipAddrWindow(&a,&b,&c,&d);")
        cpp(f"tft.fillScreen({(random.randrange(-2147483648,2147483648))});")
        cpp("tft.clipWindow(&d,&c,&b,&a);")
        cpp(f"tft.fillScreen({(random.randrange(-2147483648,2147483648))});")
        cpp(f"tft.setViewport({(random.randrange(-2147483648,2147483648))},{(random.randrange(-2147483648,2147483648))},{(random.randrange(-2147483648,2147483648))},{(random.randrange(-2147483648,2147483648))},{random.getrandbits(1)});")
        
        cpp("tft.resetViewport();")
        cpp("tft.fillScreen(TFT_BLACK);")
        cpp(f"tft.setViewport({self.args['posx']},{self.args['posy']},{self.args['sizex']},{self.args['sizey']},false);")
        if self.args["fill"]:
            cpp(f"tft.fillScreen({self.args['color']});")
        else:
            self.rect(cpp)

    def followup_testcase(self, cpp):
        cpp("tft.fillScreen(TFT_BLACK);")
        if self.args["fill"]:
            cpp(f"tft.fillRect({self.args['posx']},{self.args['posy']},{self.args['sizex']},{self.args['sizey']},{self.args['color']});")
        else:
            self.rect(cpp)

    def random_args(self):
        constraints = Generators.Util.constraints.viewport
        self.args = {}
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])
        self.args["fill"] = bool(random.getrandbits(1))
