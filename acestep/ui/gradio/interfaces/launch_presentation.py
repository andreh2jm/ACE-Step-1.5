"""Gradio 6 launch presentation helpers for theme/css/head.

In Gradio 6, ``theme``, ``css``, and ``head`` must be passed to
``Blocks.launch()`` rather than the ``Blocks`` constructor.
"""

from __future__ import annotations

from typing import Any

import gradio as gr

_PRESENTATION_ATTR = "_acestep_launch_presentation"


def attach_launch_presentation(
    demo: gr.Blocks,
    *,
    theme: Any,
    css: str,
    head: str,
) -> gr.Blocks:
    """Attach theme/css/head so callers can forward them to ``launch()``.

    Args:
        demo: Gradio Blocks instance to annotate.
        theme: Gradio theme object.
        css: Custom CSS string.
        head: Extra HTML/JS for the document head.

    Returns:
        The same ``demo`` instance for fluent use.
    """

    setattr(
        demo,
        _PRESENTATION_ATTR,
        {
            "theme": theme,
            "css": css,
            "head": head,
        },
    )
    return demo


def get_launch_presentation(demo: gr.Blocks) -> dict[str, Any]:
    """Return theme/css/head kwargs previously attached to ``demo``.

    Args:
        demo: Gradio Blocks instance that may carry presentation metadata.

    Returns:
        A dict suitable for ``demo.launch(**kwargs)``. Empty when unset.
    """

    payload = getattr(demo, _PRESENTATION_ATTR, None)
    if not isinstance(payload, dict):
        return {}
    return {
        key: payload[key]
        for key in ("theme", "css", "head")
        if key in payload and payload[key] is not None
    }
