from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget

from super_scad_smooth_profile.SmoothProfile import SmoothProfile


class Rough(SmoothProfile):
    """
    Applies no finish to the vertices at a node (a.k.a. edge).
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, child: ScadWidget):
        """
        Object constructor.

        :param child: The child object which will be left rough.
        """
        SmoothProfile.__init__(self, args=locals(), child=child)

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD widget.

        :param context: The build context.
        """
        return self.child

# ----------------------------------------------------------------------------------------------------------------------
