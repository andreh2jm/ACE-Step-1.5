"""On-hover tooltip CSS for Gradio info labels."""

TOOLTIPS_CSS = """
/* --- On-hover Tooltips --- */
.has-info-container {
    overflow: visible !important;
    contain: none !important;
}

.row:has(.has-info-container),
.column:has(.has-info-container),
.form:has(.has-info-container),
.accordion:has(.has-info-container),
.tabs:has(.has-info-container),
.gr-block:has(.has-info-container),
.gr-box:has(.has-info-container),
.gr-group:has(.has-info-container),
.styler:has(.has-info-container) {
    overflow: visible !important;
    contain: none !important;
}

.has-info-container span[data-testid="block-info"] + div,
.has-info-container span[data-testid="block-info"] + span,
.checkbox-container + div {
    visibility: hidden;
    opacity: 0;
    transition: opacity 0.1s ease, visibility 0.1s ease;
    transition-delay: 0.08s;
    position: absolute;
    background: rgba(18, 22, 28, 0.98);
    color: #f3f4f6;
    padding: 12px 16px;
    border-radius: 10px;
    font-size: 0.85rem;
    z-index: 999999;
    max-width: 320px;
    min-width: 180px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.5);
    pointer-events: none;
    line-height: 1.5;
    margin-top: 6px;
    border: 1px solid rgba(255,255,255,0.12);
    backdrop-filter: blur(10px);
    left: 0;
    font-weight: 400;
    text-transform: none;
}

.no-tooltip span[data-testid="block-info"] + div,
.no-tooltip span[data-testid="block-info"] + span {
    display: block !important;
    position: static !important;
    background: none !important;
    padding: 0 !important;
    border: none !important;
    box-shadow: none !important;
    backdrop-filter: none !important;
    max-width: none !important;
    min-width: 0 !important;
    z-index: auto !important;
    pointer-events: auto !important;
    margin-top: 0 !important;
    color: inherit !important;
    font-size: inherit !important;
    line-height: inherit !important;
    font-weight: inherit !important;
    text-transform: inherit !important;
    border-radius: 0 !important;
}
.no-tooltip span[data-testid="block-info"]::after {
    display: none !important;
}

.has-info-container span[data-testid="block-info"]:hover + div,
.has-info-container span[data-testid="block-info"]:hover + span,
.has-info-container span[data-testid="block-info"] + div:hover,
.has-info-container span[data-testid="block-info"] + span:hover,
.checkbox-container:hover + div,
.checkbox-container + div:hover {
    visibility: visible !important;
    opacity: 1 !important;
    transition-delay: 0s;
}

.has-info-container span[data-testid="block-info"]::after,
.checkbox-container:has(+ div) .label-text::after {
    content: "";
    display: inline-block;
    width: 14px;
    height: 14px;
    margin-left: 8px;
    vertical-align: middle;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%231ed760' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='10'/%3E%3Cline x1='12' y1='16' x2='12' y2='12'/%3E%3Cline x1='12' y1='8' x2='12.01' y2='8'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-size: contain;
    opacity: 0.6;
    transition: opacity 0.2s, transform 0.2s;
    cursor: help;
}

.has-info-container span[data-testid="block-info"] svg,
.has-info-container span[data-testid="block-info"]::before {
    display: none !important;
}

.has-info-container span[data-testid="block-info"]:hover::after,
.checkbox-container:hover .label-text::after {
    opacity: 1;
    transform: scale(1.15);
}

.has-info-container span[data-testid="block-info"]:hover + div,
.has-info-container span[data-testid="block-info"]:hover + span,
.has-info-container span[data-testid="block-info"] + div:hover,
.has-info-container span[data-testid="block-info"] + span:hover,
.checkbox-container:hover + div,
.checkbox-container + div:hover {
    max-height: 40vh;
    overflow-y: auto;
    pointer-events: auto;
}

.has-info-container.tooltip-flip span[data-testid="block-info"] + div,
.has-info-container.tooltip-flip span[data-testid="block-info"] + span {
    bottom: 100%;
    top: auto;
    margin-top: 0;
    margin-bottom: 6px;
}
"""
