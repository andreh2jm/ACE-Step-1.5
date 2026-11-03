"""Unit tests for the Suno-like Gradio studio theme."""

import unittest

import gradio as gr

from acestep.ui.gradio.interfaces.studio_theme import build_studio_theme


class BuildStudioThemeTests(unittest.TestCase):
    """Tests for ``build_studio_theme``."""

    def test_returns_gradio_theme_instance(self):
        """Success path: builder should return a Gradio Base theme."""
        theme = build_studio_theme()
        self.assertIsInstance(theme, gr.themes.Base)

    def test_uses_dark_studio_palette_not_soft_purple(self):
        """Theme tokens should prefer emerald studio accents over Soft purple."""
        theme = build_studio_theme()
        self.assertEqual(theme.button_primary_background_fill, "#1ed760")
        self.assertEqual(theme.body_background_fill, "#0b0d10")
        self.assertEqual(theme.body_background_fill_dark, "#0b0d10")
        self.assertEqual(theme.primary_500, "#10b981")
        css = theme._get_theme_css()
        self.assertIn("#1ed760", css)
        self.assertNotIn("#7c3aed", css)
        self.assertTrue(
            any("Sora" in sheet for sheet in theme._stylesheets),
            "expected Sora display font stylesheet",
        )


if __name__ == "__main__":
    unittest.main()
