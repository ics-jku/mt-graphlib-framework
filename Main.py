from test_runner import TestRunner

from Generators.sprite import Sprite
from Generators.println import Println
from Generators.draw_arc import DrawArc
from Generators.rotation import Rotation
from Generators.fill_screen import FillScreen
from Generators.wedge_line import WedgeLine

from Generators.viewport import Viewport
from Generators.frame_viewport import FrameViewport
from Generators.viewport_unequal import ViewportUnequal

from Generators.nikolaus import Nikolaus
from Generators.nikolaus_shapes import NikolausShapes
from Generators.nikolaus_move import NikolausMove
from Generators.nikolaus_sprite import NikolausSprite

from Generators.draw_rectangle import DrawRectangle
from Generators.fill_rectangle import FillRectangle

from Generators.fill_ellipse import FillEllipse
from Generators.draw_ellipse import DrawEllipse

from Generators.draw_circle import DrawCircle
from Generators.fill_circle import FillCircle
from Generators.draw_smooth_circle import DrawSmoothCircle
from Generators.fill_smooth_circle import FillSmoothCircle

from Generators.draw_pixel import DrawPixel
from Generators.draw_arc_segments import DrawArcSegments

TestRunner(DrawPixel()).run(10)
TestRunner(FillScreen()).run(10)
TestRunner(Println()).run(10)
TestRunner(Rotation()).run(10)
TestRunner(Sprite()).run(10)
TestRunner(WedgeLine()).run(10)

TestRunner(Viewport()).run(10)
TestRunner(FrameViewport()).run(10)
TestRunner(ViewportUnequal()).run(10)

TestRunner(Nikolaus()).run(10)
TestRunner(NikolausShapes()).run(10)
TestRunner(NikolausMove()).run(10)
TestRunner(NikolausSprite()).run(10)

TestRunner(DrawRectangle()).run(10)
TestRunner(FillRectangle()).run(10)

TestRunner(DrawEllipse()).run(10)
TestRunner(FillEllipse()).run(10)

TestRunner(DrawCircle()).run(10)
TestRunner(FillCircle()).run(10)
TestRunner(DrawSmoothCircle()).run(10)
TestRunner(FillSmoothCircle()).run(10)

TestRunner(DrawArc()).run(10)
TestRunner(DrawArcSegments()).run(10)
