"""Legacy Gradio control-layout CSS preserved during the studio redesign."""

CONTROLS_CSS = """
.lm-hints-row {
    align-items: stretch;
}
.lm-hints-col {
    display: flex;
}
.lm-hints-col > div {
    flex: 1;
    display: flex;
}
.lm-hints-btn button {
    height: 100%;
    width: 100%;
}
/* Position Audio time labels lower to avoid scrollbar overlap */
.component-wrapper > .timestamps {
    transform: translateY(15px);
}
/* Equal-height row for instrumental checkbox + enhance lyrics button */
.instrumental-row {
    align-items: stretch !important;
}
.instrumental-row > div {
    display: flex !important;
    align-items: stretch !important;
}
.instrumental-row > div > div {
    flex: 1;
    display: flex;
    align-items: center;
}
.instrumental-row button {
    height: 100% !important;
    min-height: 42px;
}
.instrumental-row > div > button {
    height: 100% !important;
    min-height: 42px;
}
/* Two-line icon buttons: emoji on top, text below */
.icon-btn-wrap button, .icon-btn-wrap > button {
    word-spacing: 100vw;
    text-align: center;
    line-height: 1.4;
}

/* --- Auto-toggle checkbox row --- */
.auto-toggles-row {
    margin-top: -8px !important;
    margin-bottom: 0 !important;
    padding: 0 !important;
    gap: 16px !important;
    min-height: 0 !important;
}
.auto-toggle {
    text-align: center !important;
}
.auto-toggle label {
    font-size: 0.8rem !important;
    gap: 4px !important;
    white-space: nowrap !important;
    cursor: pointer !important;
    opacity: 0.5;
    transition: opacity 0.15s;
    justify-content: center !important;
}
.auto-toggle:hover label {
    opacity: 1;
}
.auto-toggle input[type="checkbox"] {
    width: 13px !important;
    height: 13px !important;
}
"""
