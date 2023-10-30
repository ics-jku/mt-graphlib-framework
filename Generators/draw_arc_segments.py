import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator


class DrawArcSegments(MTCGenerator):
    def __init__(self, path='', name="drawArc_segments"):
        super(DrawArcSegments, self).__init__(path, name)

    def source_testcase(self, cpp):
        cpp(f"tft.drawArc({self.args['x']},{self.args['y']},{self.args['r']},{self.args['ir']},{self.args['start']},{self.args['end']},{self.args['color_arc']},{self.args['color_bg']},false);")

    def followup_testcase(self, cpp):
        half = self.args["start"]+((self.args["end"]-self.args["start"])/2)
        cpp(f"tft.drawArc({self.args['x']},{self.args['y']},{self.args['r']},{self.args['ir']},{self.args['start']},{half},{self.args['color_arc']},{self.args['color_bg']},false);")
        cpp(f"tft.drawArc({self.args['x']},{self.args['y']},{self.args['r']},{self.args['ir']},{half},{self.args['end']},{self.args['color_arc']},{self.args['color_bg']},false);")

    def random_args(self):
        constraints = Generators.Util.constraints.drawArc_segments
        self.args = {}
        for val in constraints:
            if val != "end":
                self.args[val] = random.randrange(*constraints[val])

        while True:
            end = random.randrange(*constraints["end"])
            if end > self.args["start"]:
                break
        
        self.args["end"] = end
