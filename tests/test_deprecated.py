from pysankey import sankey
from tests.generic_test import TestFruit


class TestErrorCase(TestFruit):

    """Test sankey's deprecation warnings."""

    def test_deprecated_parameters(self) -> None:
        """Test if deprecation warnings are correctly triggered"""
        with self.assertWarns(DeprecationWarning):
            sankey(
                self.data["true"],
                self.data["predicted"],
                colorDict=self.colorDict,
                figureName=self.figure_name,
            )

        with self.assertWarns(DeprecationWarning):
            sankey(
                self.data["true"],
                self.data["predicted"],
                colorDict=self.colorDict,
                closePlot=True,
            )

        with self.assertWarns(DeprecationWarning):
            sankey(
                self.data["true"],
                self.data["predicted"],
                colorDict=self.colorDict,
                figSize=(8, 8),
            )
