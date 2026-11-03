"""Unit tests for Gradio interface CSS assembly."""

import unittest
from unittest.mock import patch


class BuildInterfaceCssTests(unittest.TestCase):
    """Tests for ``build_interface_css``."""

    def test_includes_studio_and_help_selectors(self):
        """Assembled CSS should include studio, tooltip, and help selectors."""
        with patch(
            "acestep.ui.gradio.interfaces.css.HELP_MODAL_CSS",
            ".help-modal-overlay {}",
        ):
            from acestep.ui.gradio.interfaces.css import build_interface_css

            css = build_interface_css()

        self.assertIn(".studio-hero", css)
        self.assertIn(".studio-workspace", css)
        self.assertIn(".create-studio", css)
        self.assertIn(".library-panel", css)
        self.assertIn("#acestep-generate-btn", css)
        self.assertIn(".has-info-container", css)
        self.assertIn(".instrumental-row", css)
        self.assertIn(".help-modal-overlay", css)

    def test_avoids_purple_ai_slop_background(self):
        """Studio CSS should not introduce purple/indigo gradient backgrounds."""
        from acestep.ui.gradio.interfaces.css_studio import STUDIO_CSS

        lowered = STUDIO_CSS.lower()
        self.assertNotIn("purple", lowered)
        self.assertNotIn("#7c3aed", lowered)
        self.assertNotIn("indigo", lowered)


class StudioHeaderTests(unittest.TestCase):
    """Tests for the studio hero header HTML."""

    def test_brand_is_hero_signal(self):
        """Header HTML should feature ACE-Step as the primary brand heading."""
        with patch(
            "acestep.ui.gradio.interfaces.studio_header.t",
            side_effect=lambda key: {
                "app.subtitle": "Open-source music generation",
            }[key],
        ):
            from acestep.ui.gradio.interfaces.studio_header import (
                build_studio_header_html,
            )

            html = build_studio_header_html()

        self.assertIn('class="studio-hero-brand"', html)
        self.assertIn("ACE-Step", html)
        self.assertIn("Open-source music generation", html)
        self.assertIn("studio-hero-glow", html)


if __name__ == "__main__":
    unittest.main()
