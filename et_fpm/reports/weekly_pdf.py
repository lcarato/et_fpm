"""Weekly PDF report generation."""

from __future__ import annotations

from jinja2 import Template
from weasyprint import HTML

HTML_TEMPLATE = """
<html>
<body>
<h1>Weekly Report</h1>
<p>{{ macro }}</p>
<p>KPI: {{ kpi }}</p>
<p>Regime: {{ regime }}</p>
</body>
</html>
"""


def build_report(macro: str, kpi: str, regime: str) -> bytes:
    """Render HTML template and convert to PDF bytes."""
    html = Template(HTML_TEMPLATE).render(macro=macro, kpi=kpi, regime=regime)
    return HTML(string=html).write_pdf()
