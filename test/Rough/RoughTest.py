import random

from super_scad.d2.Square import Square
from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.type import Vector2

from super_scad_smooth_profile.RoughFactory import RoughFactory
from test.ScadTestCase import ScadTestCase


class RoughTest(ScadTestCase):
    """
    Testcases for rough profile.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_sizes(self):
        """
        Test the sizes of rough profile.
        """
        factory = RoughFactory()

        self.assertAlmostEqual(0.0, factory.offset1(inner_angle=random.uniform(0, 360.0)))
        self.assertAlmostEqual(0.0, factory.offset2(inner_angle=random.uniform(0, 360.0)))

    # ------------------------------------------------------------------------------------------------------------------
    def test_on_child(self) -> None:
        """
        Test fillet for convex corners with sharp and oblique angles.
        """
        path_actual, path_expected = self.paths()

        scad = Scad(context=Context())
        body = Square(size=10.0)

        factory = RoughFactory()
        body = factory.create_smooth_profile(inner_angle=90.0,
                                             normal_angle=45.0,
                                             position=Vector2.origin,
                                             child=body)

        scad.run_super_scad(body, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
