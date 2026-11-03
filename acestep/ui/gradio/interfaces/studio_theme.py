"""Suno-like dark music-studio Gradio theme for ACE-Step."""

from __future__ import annotations

from collections.abc import Iterable

import gradio as gr
from gradio.themes.utils import colors, fonts, sizes


def build_studio_theme() -> gr.themes.Base:
    """Build a dark studio theme with deep neutrals and a green accent.

    Uses emerald primary (not purple Soft defaults) and zinc neutrals so the
    UI reads as a music-creation product rather than a dense control panel.

    Returns:
        A Gradio theme configured for both light and dark modes with an
        always-dark studio palette.
    """

    theme = gr.themes.Base(
        primary_hue=colors.emerald,
        secondary_hue=colors.zinc,
        neutral_hue=colors.zinc,
        spacing_size=sizes.spacing_md,
        radius_size=sizes.radius_lg,
        text_size=sizes.text_md,
        font=_studio_sans_fonts(),
        font_mono=_studio_mono_fonts(),
    )
    return theme.set(
        # Shared / light (forced studio dark values for a consistent look)
        body_background_fill=_BG,
        body_background_fill_dark=_BG,
        body_text_color=_TEXT,
        body_text_color_dark=_TEXT,
        body_text_color_subdued=_MUTED,
        body_text_color_subdued_dark=_MUTED,
        background_fill_primary=_SURFACE,
        background_fill_primary_dark=_SURFACE,
        background_fill_secondary=_SURFACE_RAISED,
        background_fill_secondary_dark=_SURFACE_RAISED,
        border_color_primary=_BORDER,
        border_color_primary_dark=_BORDER,
        block_background_fill=_SURFACE,
        block_background_fill_dark=_SURFACE,
        block_border_width="1px",
        block_border_width_dark="1px",
        block_border_color=_BORDER,
        block_border_color_dark=_BORDER,
        block_label_background_fill=_SURFACE_RAISED,
        block_label_background_fill_dark=_SURFACE_RAISED,
        block_label_text_color=_MUTED,
        block_label_text_color_dark=_MUTED,
        block_title_text_color=_TEXT,
        block_title_text_color_dark=_TEXT,
        block_radius="16px",
        block_shadow="none",
        block_shadow_dark="none",
        input_background_fill=_INPUT,
        input_background_fill_dark=_INPUT,
        input_border_color=_BORDER,
        input_border_color_dark=_BORDER,
        input_border_width="1px",
        input_radius="12px",
        button_large_radius="999px",
        button_large_text_weight="600",
        button_primary_background_fill=_ACCENT,
        button_primary_background_fill_dark=_ACCENT,
        button_primary_background_fill_hover=_ACCENT_HOVER,
        button_primary_background_fill_hover_dark=_ACCENT_HOVER,
        button_primary_text_color="#04140a",
        button_primary_text_color_dark="#04140a",
        button_primary_border_color=_ACCENT,
        button_primary_border_color_dark=_ACCENT,
        button_secondary_background_fill=_SURFACE_RAISED,
        button_secondary_background_fill_dark=_SURFACE_RAISED,
        button_secondary_background_fill_hover=_SURFACE_HOVER,
        button_secondary_background_fill_hover_dark=_SURFACE_HOVER,
        button_secondary_text_color=_TEXT,
        button_secondary_text_color_dark=_TEXT,
        button_secondary_border_color=_BORDER,
        button_secondary_border_color_dark=_BORDER,
        checkbox_background_color=_INPUT,
        checkbox_background_color_dark=_INPUT,
        checkbox_background_color_selected=_ACCENT,
        checkbox_background_color_selected_dark=_ACCENT,
        checkbox_border_color=_BORDER,
        checkbox_border_color_dark=_BORDER,
        checkbox_label_background_fill=_SURFACE,
        checkbox_label_background_fill_dark=_SURFACE,
        checkbox_label_text_color=_TEXT,
        checkbox_label_text_color_dark=_TEXT,
        slider_color=_ACCENT,
        slider_color_dark=_ACCENT,
        color_accent=_ACCENT,
        color_accent_soft=_ACCENT_SOFT,
        link_text_color=_ACCENT,
        link_text_color_dark=_ACCENT,
        shadow_drop="none",
        shadow_drop_lg="0 18px 40px rgba(0, 0, 0, 0.45)",
    )


def _studio_sans_fonts() -> Iterable[fonts.Font | str]:
    """Return display/body sans fonts for the studio theme."""

    return (
        fonts.GoogleFont("Sora", weights=(400, 500, 600, 700)),
        "ui-sans-serif",
        "system-ui",
        "sans-serif",
    )


def _studio_mono_fonts() -> Iterable[fonts.Font | str]:
    """Return monospace fonts for codes and metadata."""

    return (
        fonts.GoogleFont("IBM Plex Mono", weights=(400, 500, 600)),
        "ui-monospace",
        "Consolas",
        "monospace",
    )


_BG = "#0b0d10"
_SURFACE = "#12161c"
_SURFACE_RAISED = "#181d26"
_SURFACE_HOVER = "#222833"
_INPUT = "#0f1319"
_BORDER = "#2a313c"
_TEXT = "#f3f4f6"
_MUTED = "#9aa3b2"
_ACCENT = "#1ed760"
_ACCENT_HOVER = "#17c653"
_ACCENT_SOFT = "#143524"
