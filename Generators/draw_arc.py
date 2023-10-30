import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator

"""
drawSmoothArc() does anti-aliasing but at 0, 90, 270 & 360° the edges are not
anti-aliased (because the are straight) this means:
For any combination of these angles (and there negative counterparts) 
drawSmoothArc(roundEdges=false) should yield the same result as drawArc(smooth=true).
This is does not hold, because drawSmoothArc produces some artifacts when using
negative coordinates.

This relation also covers drawing an arc from eg. 90 to 90.
drawSmoothArc() yields full circle and drawArc() yields no circle.

Drawing an arc from 0 to 360 using drawSmoothArc(roundEdges=false) should yield
the same result as an arc from 0 to 360 using drawArc(smooth=true). This holds.

drawSmoothArc() from eg. 180 to -270, should be the same as 180 to 90.
In other words  drawSmoothArc() from eg. 180 to -270 should equal drawArc() from eg. 180 to -270.
This does not hold. With -270 we get anti-aliasing on a straight edge.

Another observation: startAngle must no be bigger than 360,
otherwise we get stuck in an endless loop.
"""


class DrawArc(MTCGenerator):
    def __init__(self, path='', name="drawArc"):
        super(DrawArc, self).__init__(path, name)

    def source_testcase(self, cpp):
        cpp(f"tft.drawSmoothArc({self.args['x']},{self.args['y']},{self.args['r']},{self.args['ir']},{self.args['start']},{self.args['end']},{self.args['color_arc']},{self.args['color_bg']},false);")

    def followup_testcase(self, cpp):
        cpp(f"tft.drawArc({self.args['x']},{self.args['y']},{self.args['r']},{self.args['ir']},{self.args['start']},{self.args['end']},{self.args['color_arc']},{self.args['color_bg']},true);")

    def random_args(self):
        constraints = Generators.Util.constraints.drawArc
        self.args = {}
        for val in constraints:
            if val != "start_end":
                self.args[val] = random.randrange(*constraints[val])
        self.args["start"] = random.choice(constraints["start_end"])
        self.args["end"] = random.choice(constraints["start_end"])
