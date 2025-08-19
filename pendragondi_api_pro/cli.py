import typer
from pathlib import Path
from pendragondi_api_pro.core import get_event_log
from pendragondi_api_pro.export import export_json, export_csv, export_html

app = typer.Typer(help="PendragonDI API Pro – Export duplicate detection event logs")

@app.command()
def export(
    output: str = typer.Option("report.html", "-o", "--output", help="Output file path"),
    format: str = typer.Option("html", "-f", "--format", help="Report format: html, json, csv"),
):
    """Export duplicate events to a report."""
    events = get_event_log().snapshot()

    if format.lower() == "json":
        export_json(events, output)
    elif format.lower() == "csv":
        export_csv(events, output)
    else:
        export_html(events, output)

    typer.echo(f"Report saved to {Path(output).resolve()}")

def main():
    app()

if __name__ == "__main__":
    main()
