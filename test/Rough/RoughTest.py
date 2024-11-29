import random
import unittest

from super_scad.scad.Context import Context
from super_scad.type import Vector2

from super_scad_smooth_profile.Rough import Rough
from super_scad_smooth_profile.SmoothProfileParams import SmoothProfileParams


class RoughTest(unittest.TestCase):
    """
    Testcases for rough profile.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_convexity(self):
        """
        Test the convexity of rough profile.
        """
        profile = Rough()
        self.assertIsNone(profile.convexity)

    # ------------------------------------------------------------------------------------------------------------------
    def test_internal_external(self):
        """
        Test that a rough profile is nighter external nor internal.
        """
        profile = Rough()
        self.assertFalse(profile.is_external)
        self.assertFalse(profile.is_internal)
        self.assertIsNone(profile.side)

    # ------------------------------------------------------------------------------------------------------------------
    def test_sizes(self):
        """
        Test the sizes of rough profile.
        """
        profile = Rough()

        self.assertAlmostEqual(0.0, profile.offset1(inner_angle=random.uniform(0, 360.0)))
        self.assertAlmostEqual(0.0, profile.offset2(inner_angle=random.uniform(0, 360.0)))

    # ------------------------------------------------------------------------------------------------------------------
    def test_on_child(self) -> None:
        """
        Test fillet for convex corners with sharp and oblique angles.
        """
        profile = Rough()
        negative, positive = profile.create_smooth_profiles(params=SmoothProfileParams(inner_angle=90.0,
                                                                                       normal_angle=45.0,
                                                                                       position=Vector2.origin))
        self.assertIsNone(negative)
        self.assertIsNone(positive)

    # ------------------------------------------------------------------------------------------------------------------
    def test_polygon(self) -> None:
        """
        Test the polygon of rough profile.
        """
        context = Context()
        profile = Rough()
        params = SmoothProfileParams(inner_angle=random.uniform(0.0, 360.0),
                                     normal_angle=random.uniform(0.0, 360.0),
                                     position=Vector2(random.uniform(0.0, 10.0), random.uniform(0.0, 10.0)))
        polygon = profile.create_polygon(context=context, params=params)

        self.assertTrue(polygon == [params.position])

# ----------------------------------------------------------------------------------------------------------------------
