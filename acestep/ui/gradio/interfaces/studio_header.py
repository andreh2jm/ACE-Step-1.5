"""Studio hero header HTML for the Gradio Blocks shell."""

from acestep.ui.gradio.i18n import t


def build_studio_header_html() -> str:
    """Build the hero brand header for the create workspace.

    Keeps the product name as the dominant first-viewport signal and uses the
    existing i18n subtitle for the supporting line.

    Returns:
        HTML string for ``gr.HTML``.
    """

    subtitle = t("app.subtitle")
    return f"""
    <div class="studio-hero">
        <div class="studio-hero-glow" aria-hidden="true"></div>
        <p class="studio-hero-eyebrow">Music studio</p>
        <h1 class="studio-hero-brand">ACE-Step</h1>
        <p class="studio-hero-tagline">{subtitle}</p>
    </div>
    """


TOOLTIP_FLIP_SCRIPT = """
<script>
/* Flip tooltips upward when they would overflow the viewport bottom.
   Handles both .has-info-container and .checkbox-container elements. */
document.addEventListener('mouseover', function(e) {
    var el = e.target.closest('.has-info-container, .checkbox-container');
    if (!el) return;
    var rect = el.getBoundingClientRect();
    if (rect.bottom > window.innerHeight * 0.65) {
        el.classList.add('tooltip-flip');
    } else {
        el.classList.remove('tooltip-flip');
    }
});
</script>
"""
