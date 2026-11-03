"""Atmospheric studio CSS for the Suno-like Gradio redesign."""

STUDIO_CSS = """
/* --- Studio shell --- */
.gradio-container {
    max-width: 1280px !important;
    margin-left: auto !important;
    margin-right: auto !important;
}
.gradio-container,
.gradio-container .main,
.gradio-container .wrap {
    background: transparent !important;
}
body,
.dark,
gradio-app {
    background:
        radial-gradient(ellipse 90% 55% at 12% -10%, rgba(30, 215, 96, 0.16), transparent 55%),
        radial-gradient(ellipse 70% 45% at 92% 8%, rgba(56, 189, 248, 0.10), transparent 50%),
        radial-gradient(ellipse 60% 40% at 50% 100%, rgba(20, 53, 36, 0.35), transparent 55%),
        linear-gradient(180deg, #0b0d10 0%, #0e1218 45%, #0b0d10 100%) !important;
    background-attachment: fixed !important;
    color: #f3f4f6 !important;
}

/* --- Hero brand --- */
.studio-hero {
    position: relative;
    text-align: left;
    padding: 1.75rem 0 1.25rem;
    margin-bottom: 0.75rem;
    overflow: hidden;
}
.studio-hero-glow {
    position: absolute;
    inset: -20% auto auto -8%;
    width: min(420px, 70vw);
    height: 180px;
    background: radial-gradient(circle, rgba(30, 215, 96, 0.22), transparent 70%);
    filter: blur(8px);
    pointer-events: none;
    animation: studio-glow-pulse 6s ease-in-out infinite;
}
.studio-hero-eyebrow {
    position: relative;
    margin: 0 0 0.4rem;
    font-size: 0.75rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #9aa3b2;
    font-weight: 500;
}
.studio-hero-brand {
    position: relative;
    margin: 0;
    font-size: clamp(2.4rem, 5vw, 3.6rem);
    line-height: 1.05;
    font-weight: 700;
    letter-spacing: -0.03em;
    color: #f8fafc;
    text-shadow: 0 0 40px rgba(30, 215, 96, 0.18);
}
.studio-hero-tagline {
    position: relative;
    margin: 0.65rem 0 0;
    max-width: 36rem;
    font-size: 1.02rem;
    line-height: 1.45;
    color: #9aa3b2;
}
@keyframes studio-glow-pulse {
    0%, 100% { opacity: 0.75; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.05); }
}

/* --- Workspace: create + library --- */
.studio-workspace {
    gap: 1.25rem !important;
    align-items: flex-start !important;
}
.create-studio,
.library-panel {
    background: rgba(18, 22, 28, 0.72) !important;
    border: 1px solid rgba(42, 49, 60, 0.9) !important;
    border-radius: 20px !important;
    padding: 1rem 1rem 1.15rem !important;
    backdrop-filter: blur(10px);
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.28);
}
.create-studio {
    position: relative;
}
.create-studio::before {
    content: "Create";
    display: block;
    margin: 0 0 0.85rem;
    font-size: 0.72rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #1ed760;
    font-weight: 600;
}
.library-panel::before {
    content: "Library";
    display: block;
    margin: 0 0 0.85rem;
    font-size: 0.72rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #9aa3b2;
    font-weight: 600;
}
.library-accordion {
    border: none !important;
    background: transparent !important;
}

/* Prominent generate CTA */
#acestep-generate-btn,
#acestep-generate-btn button {
    min-height: 56px !important;
    border-radius: 999px !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.02em !important;
    box-shadow: 0 0 0 1px rgba(30, 215, 96, 0.25), 0 10px 28px rgba(30, 215, 96, 0.22) !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
}
#acestep-generate-btn:hover,
#acestep-generate-btn button:hover {
    transform: translateY(-1px);
    box-shadow: 0 0 0 1px rgba(30, 215, 96, 0.35), 0 14px 34px rgba(30, 215, 96, 0.3) !important;
}

/* Tabs read as product navigation, not a dense dashboard */
.tabs > .tab-nav {
    border-bottom: 1px solid #2a313c !important;
    gap: 0.25rem;
    margin-bottom: 0.85rem;
}
.tabs > .tab-nav button {
    border-radius: 999px !important;
    padding: 0.55rem 1rem !important;
    color: #9aa3b2 !important;
}
.tabs > .tab-nav button.selected {
    background: rgba(30, 215, 96, 0.12) !important;
    color: #1ed760 !important;
    border: 1px solid rgba(30, 215, 96, 0.35) !important;
}

/* Settings stay secondary */
.section-header {
    background: linear-gradient(90deg, rgba(30, 215, 96, 0.85), rgba(20, 160, 90, 0.75));
    color: #04140a;
    padding: 10px;
    border-radius: 10px;
    margin: 10px 0;
}

@media (max-width: 960px) {
    .studio-workspace {
        flex-direction: column !important;
    }
    .studio-hero {
        text-align: left;
        padding-top: 1.1rem;
    }
    .studio-hero-brand {
        font-size: 2.2rem;
    }
    .create-studio,
    .library-panel {
        padding: 0.85rem !important;
    }
}
"""
