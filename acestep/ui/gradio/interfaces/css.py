"""Assemble Gradio interface CSS for the studio redesign."""

from acestep.ui.gradio.help_content import HELP_MODAL_CSS
from acestep.ui.gradio.interfaces.css_controls import CONTROLS_CSS
from acestep.ui.gradio.interfaces.css_studio import STUDIO_CSS
from acestep.ui.gradio.interfaces.css_tooltips import TOOLTIPS_CSS


def build_interface_css() -> str:
    """Concatenate studio, controls, tooltip, and help-modal CSS.

    Returns:
        A single CSS string suitable for ``gr.Blocks(css=...)``.
    """

    return "\n".join(
        (
            STUDIO_CSS,
            CONTROLS_CSS,
            TOOLTIPS_CSS,
            HELP_MODAL_CSS,
        )
    )
