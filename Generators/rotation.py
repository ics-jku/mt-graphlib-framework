import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator


class Rotation(MTCGenerator):
    def __init__(self, path='', name="rotation"):
        super(Rotation, self).__init__(path, name)

    def fn0(self, cpp):
        cpp(f"tft.fillScreen({self.args['color_bg']});")
        # draw two diagonal lines
        cpp(f"tft.drawLine(0,0,tft.width()-1,tft.height()-1,{self.args['color_line']});")
        cpp(f"tft.drawLine(tft.width()-1,0,0,tft.height()-1,{self.args['color_line']});")
        # draw four corner pixels
        cpp(f"tft.drawPixel({self.args['offset']},{self.args['offset']},{self.args['color_px']});")
        cpp(f"tft.drawPixel({self.args['offset']},tft.height()-1-{self.args['offset']},{self.args['color_px']});")
        cpp(f"tft.drawPixel(tft.width()-1-{self.args['offset']},{self.args['offset']},{self.args['color_px']});")
        cpp(f"tft.drawPixel(tft.width()-1-{self.args['offset']},tft.height()-1-{self.args['offset']},{self.args['color_px']});")
        # draw four center pixels
        cpp(f"tft.drawPixel(tft.width()/2,tft.height()/2,{self.args['color_px']});")
        cpp(f"tft.drawPixel(tft.width()/2-1,tft.height()/2,{self.args['color_px']});")
        cpp(f"tft.drawPixel(tft.width()/2,tft.height()/2-1,{self.args['color_px']});")
        cpp(f"tft.drawPixel(tft.width()/2-1,tft.height()/2-1,{self.args['color_px']});")

    def source_testcase(self, cpp):
        cpp(f"tft.setRotation({self.args['rot1']});")
        self.fn0(cpp)

    def followup_testcase(self, cpp):
        cpp(f"tft.setRotation({self.args['rot2']});")
        self.fn0(cpp)

    def random_args(self):
        constraints = Generators.Util.constraints.rotation
        self.args = {}
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])
        
        self.args["rot1"] = random.randrange(0,8)
        while True:
            self.args["rot2"] = random.randrange(0,8)
            if self.args["rot1"] != self.args["rot2"]:
                break
