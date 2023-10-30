import string
import random
import Generators.Util.constraints
from Generators.Util.mtc_generator import MTCGenerator


class Println(MTCGenerator):
    def __init__(self, path='', name="println"):
        super(Println, self).__init__(path, name)

    def setup(self, cpp):
        cpp(f"tft.setRotation({self.args['rotation']});")
        cpp(f"tft.setTextSize({self.args['size']});")
        cpp(f"tft.setTextColor({self.args['color_text']},{self.args['color_bg']});")
        cpp(f"tft.setCursor({self.args['x']},{self.args['y']});")

    def source_testcase(self, cpp):
        self.setup(cpp)
        line = ""
        for word in self.args["wordlist"]:
            line += word + "\\n"
        cpp("tft.print(\""+line+"\");")

    def followup_testcase(self, cpp):
        self.setup(cpp)
        for word in self.args["wordlist"]:
            cpp("tft.println(\""+word+"\");")

    def random_args(self):
        constraints = Generators.Util.constraints.println
        self.args = {}
        for val in constraints:
            self.args[val] = random.randrange(*constraints[val])

        self.args["wordlist"] = []
        for _ in range(self.args["lines"]):
            rand = ''.join(random.choices(string.ascii_letters + string.digits, k=self.args["characters"]))
            self.args["wordlist"].append(str(rand))
