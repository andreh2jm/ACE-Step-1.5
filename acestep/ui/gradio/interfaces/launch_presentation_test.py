"""Unit tests for Gradio 6 launch presentation helpers."""

import unittest
from unittest.mock import MagicMock

from acestep.ui.gradio.interfaces.launch_presentation import (
    attach_launch_presentation,
    get_launch_presentation,
)


class LaunchPresentationTests(unittest.TestCase):
    """Tests for attach/get launch presentation metadata."""

    def test_attach_and_get_round_trip(self):
        """Success path: attached theme/css/head should round-trip."""
        demo = MagicMock()
        theme = object()
        attach_launch_presentation(
            demo, theme=theme, css=".studio-hero{}", head="<script></script>"
        )
        payload = get_launch_presentation(demo)
        self.assertEqual(payload["theme"], theme)
        self.assertEqual(payload["css"], ".studio-hero{}")
        self.assertEqual(payload["head"], "<script></script>")

    def test_get_returns_empty_when_missing(self):
        """Edge case: demos without presentation metadata return {}."""
        demo = MagicMock(spec=[])
        self.assertEqual(get_launch_presentation(demo), {})


if __name__ == "__main__":
    unittest.main()
