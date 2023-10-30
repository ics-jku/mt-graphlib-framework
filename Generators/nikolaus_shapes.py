import random
import Generators.Util.constraints
from itertools import tee
from Generators.Util.mtc_generator import MTCGenerator


class NikolausShapes(MTCGenerator):
    def __init__(self, path='', name="nikolausShapes"):
        super(NikolausShapes, self).__init__(path, name)

    def source_testcase(self, cpp):
        cpp("tft.setRotation(5);")
        for start, end in pairwise(self.args["points"]):
            cpp(f"tft.drawLine({(start[0])},{(start[1])},{(end[0])},{(end[1])},{(self.args['color'])});")

    def followup_testcase(self, cpp):
        x = self.args["posx"]
        y = self.args["posy"]
        size = self.args["size"]
        color = self.args["color"]
        
        cpp("tft.setRotation(5);")
        cpp(f"tft.drawRect({(x)},{(y)},{(size+1)},{(size+1)},{(color)});")
        cpp(f"tft.drawLine({(x)},{(y)},{(x+size)},{(y+size)},{(color)});")
        cpp(f"tft.drawLine({(x+size)},{(y)},{(x)},{(y+size)},{(color)});")
        cpp(f"tft.drawTriangle({(x)},{(y+size)},{(x+int(size/2))},{(y+size+int(size/2))},{(x+size)},{(y+size)},{(color)});")

    def random_args(self):
        constraints = Generators.Util.constraints.nikolaus
        self.args = {}
        self.args["points"] = []
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])

        points = [
            [self.args["posx"], self.args["posy"]],
            [self.args["posx"]+self.args["size"], self.args["posy"]],
            [self.args["posx"], self.args["posy"]+self.args["size"]],
            [self.args["posx"]+self.args["size"], self.args["posy"]+self.args["size"]],
            [self.args["posx"]+int(self.args["size"]/2), self.args["posy"]+self.args["size"]+int(self.args["size"]/2)]
        ]

        for p, _ in zip(*random.sample(paths, 2)):
            self.args["points"].append(points[p])

paths = [
        [0, 1, 2, 0, 3, 2, 4, 3, 1],
        [0, 1, 2, 0, 3, 4, 2, 3, 1],
        [0, 1, 2, 3, 0, 2, 4, 3, 1],
        [0, 1, 2, 3, 4, 2, 0, 3, 1],
        [0, 1, 2, 4, 3, 0, 2, 3, 1],
        [0, 1, 2, 4, 3, 2, 0, 3, 1],
        [0, 1, 3, 0, 2, 3, 4, 2, 1],
        [0, 1, 3, 0, 2, 4, 3, 2, 1],
        [0, 1, 3, 2, 0, 3, 4, 2, 1],
        [0, 1, 3, 2, 4, 3, 0, 2, 1],
        [0, 1, 3, 4, 2, 0, 3, 2, 1],
        [0, 1, 3, 4, 2, 3, 0, 2, 1],
        [0, 2, 1, 0, 3, 2, 4, 3, 1],
        [0, 2, 1, 0, 3, 4, 2, 3, 1],
        [0, 2, 1, 3, 2, 4, 3, 0, 1],
        [0, 2, 1, 3, 4, 2, 3, 0, 1],
        [0, 2, 3, 0, 1, 2, 4, 3, 1],
        [0, 2, 3, 0, 1, 3, 4, 2, 1],
        [0, 2, 3, 1, 0, 3, 4, 2, 1],
        [0, 2, 3, 1, 2, 4, 3, 0, 1],
        [0, 2, 3, 4, 2, 1, 0, 3, 1],
        [0, 2, 3, 4, 2, 1, 3, 0, 1],
        [0, 2, 4, 3, 0, 1, 2, 3, 1],
        [0, 2, 4, 3, 0, 1, 3, 2, 1],
        [0, 2, 4, 3, 1, 0, 3, 2, 1],
        [0, 2, 4, 3, 1, 2, 3, 0, 1],
        [0, 2, 4, 3, 2, 1, 0, 3, 1],
        [0, 2, 4, 3, 2, 1, 3, 0, 1],
        [0, 3, 1, 0, 2, 3, 4, 2, 1],
        [0, 3, 1, 0, 2, 4, 3, 2, 1],
        [0, 3, 1, 2, 3, 4, 2, 0, 1],
        [0, 3, 1, 2, 4, 3, 2, 0, 1],
        [0, 3, 2, 0, 1, 2, 4, 3, 1],
        [0, 3, 2, 0, 1, 3, 4, 2, 1],
        [0, 3, 2, 1, 0, 2, 4, 3, 1],
        [0, 3, 2, 1, 3, 4, 2, 0, 1],
        [0, 3, 2, 4, 3, 1, 0, 2, 1],
        [0, 3, 2, 4, 3, 1, 2, 0, 1],
        [0, 3, 4, 2, 0, 1, 2, 3, 1],
        [0, 3, 4, 2, 0, 1, 3, 2, 1],
        [0, 3, 4, 2, 1, 0, 2, 3, 1],
        [0, 3, 4, 2, 1, 3, 2, 0, 1],
        [0, 3, 4, 2, 3, 1, 0, 2, 1],
        [0, 3, 4, 2, 3, 1, 2, 0, 1]
    ]

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
