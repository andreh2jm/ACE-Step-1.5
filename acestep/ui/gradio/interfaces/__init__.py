"""
Gradio UI Components Module
Contains all Gradio interface component definitions and layouts

Layout:
  ┌──────────────────────────────────────┐
  │  Studio hero (brand)                 │
  ├──────────────────────────────────────┤
  │  Dataset Explorer (hidden accordion) │
  ├──────────────────────────────────────┤
  │  ┌─ Generation ─┬─ Training ──────┐  │
  │  │ Create | Library               │  │
  │  │ (workspace columns)            │  │
  │  └────────────────────────────────┘  │
  ├──────────────────────────────────────┤
  │  Settings (accordion, collapsed)     │
  └──────────────────────────────────────┘
"""
import gradio as gr
from acestep.ui.gradio.i18n import get_i18n, t
from acestep.ui.gradio.interfaces.dataset import create_dataset_section
from acestep.ui.gradio.interfaces.generation import (
    create_advanced_settings_section,
    create_generation_tab_section,
)
from acestep.ui.gradio.interfaces.audio_player_preferences import (
    get_audio_player_preferences_head,
)
from acestep.ui.gradio.interfaces.user_preferences import (
    get_user_preferences_head,
    wire_preference_restore,
)
from acestep.ui.gradio.interfaces.result import create_results_section
from acestep.ui.gradio.interfaces.training import create_training_section
from acestep.ui.gradio.events import setup_event_handlers, setup_training_event_handlers
from acestep.ui.gradio.help_content import create_help_button
from acestep.ui.gradio.interfaces.css import build_interface_css
from acestep.ui.gradio.interfaces.launch_presentation import (
    attach_launch_presentation,
)
from acestep.ui.gradio.interfaces.studio_header import (
    TOOLTIP_FLIP_SCRIPT,
    build_studio_header_html,
)
from acestep.ui.gradio.interfaces.studio_theme import build_studio_theme

# Re-export for callers that need Gradio 6 launch kwargs.
from acestep.ui.gradio.interfaces.launch_presentation import (  # noqa: E402
    get_launch_presentation,
)

__all__ = ["create_gradio_interface", "get_launch_presentation"]


def create_gradio_interface(
    dit_handler,
    llm_handler,
    dataset_handler,
    init_params=None,
    language: str = "en",
) -> gr.Blocks:
    """Create the ACE-Step Gradio Blocks interface.

    Theme/CSS/head are attached for Gradio 6 ``launch()`` via
    ``get_launch_presentation(demo)``.

    Args:
        dit_handler: DiT handler instance.
        llm_handler: LM handler instance.
        dataset_handler: Dataset handler instance.
        init_params: Optional initialization parameters and state.
        language: UI language code ('en', 'zh', 'ja', default: 'en').

    Returns:
        Gradio Blocks instance.
    """

    get_i18n(language)
    service_mode = init_params is not None and init_params.get("service_mode", False)
    theme = build_studio_theme()
    css = build_interface_css()
    head = (
        get_audio_player_preferences_head()
        + ("" if service_mode else get_user_preferences_head())
        + TOOLTIP_FLIP_SCRIPT
    )

    with gr.Blocks(title=t("app.title")) as demo:
        gr.HTML(build_studio_header_html())
        create_help_button("getting_started")

        dataset_section = create_dataset_section(dataset_handler)

        # Create + Library lead the composition; Settings stays available below.
        with gr.Tabs():
            with gr.Tab(t("generation.tab_title")):
                with gr.Row(elem_classes=["studio-workspace"]):
                    with gr.Column(scale=6, elem_classes=["create-studio"]):
                        gen_section = create_generation_tab_section(
                            dit_handler,
                            llm_handler,
                            init_params=init_params,
                            language=language,
                        )
                    with gr.Column(
                        scale=5,
                        visible=True,
                        elem_classes=["library-panel"],
                    ) as results_wrapper:
                        results_section = create_results_section(dit_handler)
                gen_section["results_wrapper"] = results_wrapper

            with gr.Tab(t("training.tab_title"), visible=not service_mode):
                training_section = create_training_section(
                    dit_handler, llm_handler, init_params=init_params
                )

        settings_section = create_advanced_settings_section(
            dit_handler, llm_handler, init_params=init_params, language=language
        )

        generation_section: dict = {}
        generation_section.update(settings_section)
        generation_section.update(gen_section)

        setup_event_handlers(
            demo,
            dit_handler,
            llm_handler,
            dataset_handler,
            dataset_section,
            generation_section,
            results_section,
        )
        setup_training_event_handlers(
            demo, dit_handler, llm_handler, training_section
        )
        wire_preference_restore(
            demo, generation_section, service_mode=service_mode
        )

    attach_launch_presentation(demo, theme=theme, css=css, head=head)
    return demo
