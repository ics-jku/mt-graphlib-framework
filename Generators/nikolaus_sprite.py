import random
import Generators.Util.constraints
from itertools import tee
from Generators.Util.mtc_generator import MTCGenerator


class NikolausSprite(MTCGenerator):
    def __init__(self, path='', name="nikolausSprite"):
        super(NikolausSprite, self).__init__(path, name)

    def fn0(self, cpp, data):
        idx = 0
        cpp("tft.setRotation(5);")
        for start, end in pairwise(data):
            cpp(f"TFT_eSprite spr{idx} = TFT_eSprite(&tft);")
            cpp(f"spr{idx}.createSprite(35,35);")
            cpp(f"spr{idx}.fillSprite(TFT_TRANSPARENT);")
            cpp(f"spr{idx}.drawLine({start[0]},{start[1]},{end[0]},{end[1]},{self.args['color_fg']});")
            cpp(f"spr{idx}.pushSprite({self.args['x']},{self.args['y']},TFT_TRANSPARENT);")
            idx += 1
        
    def source_testcase(self, cpp):
        self.fn0(cpp, self.args["points1"])

    def followup_testcase(self, cpp):
        self.fn0(cpp, self.args["points2"])

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
