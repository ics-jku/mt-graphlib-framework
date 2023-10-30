import random
import Generators.Util.constraints
from itertools import tee
from Generators.Util.mtc_generator import MTCGenerator


class NikolausMove(MTCGenerator):
    def __init__(self, path='', name="nikolausMove"):
        super(NikolausMove, self).__init__(path, name)

    def setup(self, cpp):
        cpp("tft.setRotation(5);")
        cpp(f"tft.fillScreen({self.args['color_bg']});")
        cpp(f"TFT_eSprite spr = TFT_eSprite(&tft);")
        cpp("spr.createSprite(35, 35);")
        cpp(f"spr.fillSprite({self.args['color_bg']});")
        cpp(f"spr.drawRect(0, 0, 35, 35, {self.args['color_bg']});")

    def source_testcase(self, cpp):
        self.setup(cpp)
        for start, end in pairwise(self.args["points1"]):
            cpp(f"spr.drawLine({start[0]},{start[1]},{end[0]},{end[1]},{self.args['color_fg']});")
        cpp(f"spr.pushSprite({self.args['x']}, {self.args['y']});")

    def followup_testcase(self, cpp):
        self.setup(cpp)
        for start, end in pairwise(self.args["points2"]):
            cpp(f"spr.drawLine({start[0]},{start[1]},{end[0]},{end[1]},{self.args['color_fg']});")

        cpp(f"int x = {self.args['x']};")
        cpp(f"int y = {self.args['y']};")
        cpp(f"int new_x = {(self.args['x']+self.args['movex'])};")
        cpp(f"int new_y = {(self.args['y']+self.args['movey'])};")
        cpp("spr.pushSprite(x,y);")

        if self.args["movex"] < 0:
            cpp("while(x > new_x) spr.pushSprite(--x, y);")
        if self.args["movex"] > 0:
            cpp("while(x < new_x) spr.pushSprite(++x, y);")

        if self.args["movey"] < 0:
            cpp("while(y > new_y) spr.pushSprite(x, --y);")
        if self.args["movey"] > 0:
            cpp("while(y < new_y) spr.pushSprite(x, ++y);")

        cpp(f"x = {self.args['x']};")
        cpp(f"y = {self.args['y']};")

        if self.args["movex"] < 0:
            cpp("while(new_x < x) spr.pushSprite(++new_x, new_y);")
        if self.args["movex"] > 0:
            cpp("while(new_x > x) spr.pushSprite(--new_x, new_y);")

        if self.args["movey"] < 0:
            cpp("while(new_y < y) spr.pushSprite(new_x, ++new_y);")
        if self.args["movey"] > 0:
            cpp("while(new_y > y) spr.pushSprite(new_x, --new_y);")


    def random_args(self):
        constraints = Generators.Util.constraints.nikolaus_sprite
        self.args = {}
        self.args["points1"] = []
        self.args["points2"] = []

        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])

        points_unordered = [
            [self.args["posx"], self.args["posy"]],
            [self.args["posx"]+self.args["size"], self.args["posy"]],
            [self.args["posx"], self.args["posy"]+self.args["size"]],
            [self.args["posx"]+self.args["size"], self.args["posy"]+self.args["size"]],
            [self.args["posx"]+int(self.args["size"]/2), self.args["posy"]+self.args["size"]+int(self.args["size"]/2)]
        ]

        for p1, p2 in zip(*random.sample(paths, 2)):
            self.args["points1"].append(points_unordered[p1])
            self.args["points2"].append(points_unordered[p2])

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
