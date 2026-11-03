"""Layout contract tests for the studio Gradio shell."""

import ast
import unittest
from pathlib import Path


_INIT_PATH = Path(__file__).with_name("__init__.py")
_RESULT_PATH = Path(__file__).with_name("result.py")
_GEN_TAB_PATH = Path(__file__).with_name("generation_tab_section.py")


def _source(path: Path) -> str:
    """Read a layout module source file.

    Args:
        path: Path to the Python module.

    Returns:
        Full source text.
    """

    return path.read_text(encoding="utf-8")


class StudioShellSourceContractTests(unittest.TestCase):
    """Static contracts for create/library presentation without launching Gradio."""

    def test_init_uses_studio_theme_and_css_helpers(self):
        """Facade should wire studio theme, CSS, and hero header helpers."""
        source = _source(_INIT_PATH)
        self.assertIn("build_studio_theme", source)
        self.assertIn("build_interface_css", source)
        self.assertIn("build_studio_header_html", source)
        self.assertIn("attach_launch_presentation", source)
        self.assertNotIn("gr.themes.Soft()", source)
        # Gradio 6: theme/css/head belong on launch(), not Blocks().
        self.assertNotIn("theme=build_studio_theme()", source)
        self.assertNotIn("css=build_interface_css()", source)

    def test_init_defines_create_library_workspace(self):
        """Generation tab should place create and library columns in one workspace."""
        source = _source(_INIT_PATH)
        self.assertIn('elem_classes=["studio-workspace"]', source)
        self.assertIn('elem_classes=["create-studio"]', source)
        self.assertIn('elem_classes=["library-panel"]', source)
        self.assertIn('gen_section["results_wrapper"] = results_wrapper', source)

    def test_results_section_marks_library_accordion(self):
        """Results accordion should expose a library styling hook."""
        source = _source(_RESULT_PATH)
        self.assertIn('elem_classes=["library-accordion"]', source)

    def test_generation_tab_marks_create_panel(self):
        """Generation controls group should expose a create-panel class."""
        source = _source(_GEN_TAB_PATH)
        self.assertIn('elem_classes=["create-panel"]', source)

    def test_init_module_stays_under_loc_cap(self):
        """Facade module should stay within the hard LOC policy after CSS extraction."""
        lines = [line for line in _source(_INIT_PATH).splitlines() if line.strip()]
        self.assertLessEqual(len(lines), 200)

    def test_init_parses_as_valid_python(self):
        """Regression: redesigned facade must remain syntactically valid."""
        ast.parse(_source(_INIT_PATH))


if __name__ == "__main__":
    unittest.main()
