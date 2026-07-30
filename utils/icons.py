"""
utils/icons.py
--------------
Inline SVG icon library for PulseHR.
All icons are based on the Lucide icon design system (2px stroke, rounded ends).
Use get_icon(name, size, colour) to embed SVG inline in st.markdown() HTML.

Usage
-----
from utils.icons import icon

st.markdown(f'''
  <div style="display:flex;align-items:center;gap:8px;">
    {icon("brain")}
    <h3>Model Explainability</h3>
  </div>
''', unsafe_allow_html=True)
"""


# ── SVG path data (Lucide icon paths, 24×24 viewBox) ────────
_PATHS: dict[str, str] = {
    # Navigation
    "home": (
        'M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z">'
        '</path><polyline points="9 22 9 12 15 12 15 22'
    ),
    "bar-chart": (
        'M12 20V10M18 20V4M6 20v-6'
    ),
    "target": (
        'M12 22a10 10 0 1 0 0-20 10 10 0 0 0 0 20z" />'
        '<circle cx="12" cy="12" r="6" /><circle cx="12" cy="12" r="2'
    ),
    "brain": (
        'M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 '
        '4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z" />'
        '<path d="M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 '
        '4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z" />'
        '<path d="M15 13a4.5 4.5 0 0 1-3-4 4.5 4.5 0 0 1-3 4'
    ),
    "trending-up": (
        'M22 7l-8.5 8.5-5-5L2 17'
    ),
    "file-text": (
        'M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />'
        '<polyline points="14 2 14 8 20 8" />'
        '<line x1="16" y1="13" x2="8" y2="13" />'
        '<line x1="16" y1="17" x2="8" y2="17" />'
        '<polyline points="10 9 9 9 8 9'
    ),
    "lightbulb": (
        'M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 '
        '.2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5" />'
        '<path d="M9 18h6" /><path d="M10 22h4'
    ),
    "alert-triangle": (
        'M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 '
        '3.86a2 2 0 0 0-3.42 0z" />'
        '<line x1="12" y1="9" x2="12" y2="13" />'
        '<line x1="12" y1="17" x2="12.01" y2="17'
    ),
    "shield-check": (
        'M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />'
        '<path d="M9 12l2 2 4-4'
    ),
    "user": (
        'M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />'
        '<circle cx="12" cy="7" r="4'
    ),
    "download": (
        'M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />'
        '<polyline points="7 10 12 15 17 10" />'
        '<line x1="12" y1="15" x2="12" y2="3'
    ),
    "zap": (
        'M13 2L3 14h9l-1 8 10-12h-9l1-8z'
    ),
    "search": (
        'M11 17.25a6.25 6.25 0 1 1 0-12.5 6.25 6.25 0 0 1 0 12.5z" />'
        '<line x1="16" y1="16" x2="22" y2="22'
    ),
    "activity": (
        'M22 12h-4l-3 9L9 3l-3 9H2'
    ),
    "pie-chart": (
        'M21.21 15.89A10 10 0 1 1 8 2.83" />'
        '<path d="M22 12A10 10 0 0 0 12 2v10z'
    ),
    "cpu": (
        'M4 4m0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z'
        '" /><path d="M9 9h6v6H9z'
    ),
    "check-circle": (
        'M22 11.08V12a10 10 0 1 1-5.93-9.14" />'
        '<polyline points="22 4 12 14.01 9 11.01'
    ),
    "x-circle": (
        'M22 12a10 10 0 1 1-20 0 10 10 0 0 1 20 0z" />'
        '<line x1="15" y1="9" x2="9" y2="15" />'
        '<line x1="9" y1="9" x2="15" y2="15'
    ),
    "info": (
        'M22 12a10 10 0 1 1-20 0 10 10 0 0 1 20 0z" />'
        '<line x1="12" y1="16" x2="12" y2="12" />'
        '<line x1="12" y1="8" x2="12.01" y2="8'
    ),
    "settings": (
        'M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z" />'
        '<path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06'
        'a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09'
        'A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83'
        'l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09'
        'A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83'
        'l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09'
        'a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83'
        'l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09'
        'a1.65 1.65 0 0 0-1.51 1z'
    ),
    "clock": (
        'M22 12a10 10 0 1 1-20 0 10 10 0 0 1 20 0z" />'
        '<polyline points="12 6 12 12 16 14'
    ),
    "database": (
        'M12 2C8.13 2 5 3.34 5 5s3.13 3 7 3 7-1.34 7-3-3.13-3-7-3z" />'
        '<path d="M5 5v4c0 1.66 3.13 3 7 3s7-1.34 7-3V5" />'
        '<path d="M5 9v4c0 1.66 3.13 3 7 3s7-1.34 7-3V9'
    ),
    "arrow-up-right": (
        'M7 17L17 7M7 7h10v10'
    ),
}


def icon(
    name: str,
    size: int = 18,
    colour: str = "currentColor",
    style: str = "",
    class_name: str = "",
) -> str:
    """
    Return an inline SVG string for the given icon name.

    Parameters
    ----------
    name   : key from _PATHS dict (e.g. "brain", "bar-chart")
    size   : pixel size (applied to width and height)
    colour : CSS colour string
    style  : extra inline CSS to add to the <svg> element
    """
    path_data = _PATHS.get(name, _PATHS["info"])
    class_attr = f'class="{class_name}"' if class_name else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        f'viewBox="0 0 24 24" fill="none" stroke="{colour}" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
        f'style="flex-shrink:0;vertical-align:middle;{style}" {class_attr}>'
        f'<path d="{path_data}" /></svg>'
    )


def icon_badge(name: str, colour: str = "#38bdf8", bg: str = "rgba(56,189,248,0.12)", size: int = 16) -> str:
    """Return an icon wrapped in a coloured circular badge — matches .kpi-icon-wrapper style."""
    return (
        f'<div style="width:36px;height:36px;border-radius:10px;'
        f'background:{bg};border:1px solid {colour}33;'
        f'display:flex;align-items:center;justify-content:center;flex-shrink:0;">'
        f'{icon(name, size=size, colour=colour)}'
        f'</div>'
    )
