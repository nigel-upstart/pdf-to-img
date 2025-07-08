# /// script
# dependencies = [
#   "typer",
#   "pymupdf",
# ]
# ///
from pathlib import Path

import fitz  # PyMuPDF
import typer

app = typer.Typer(help="Convert PDF pages to images using PyMuPDF (fitz)")


@app.command()
def pdf_to_images(
    pdf_path: Path = typer.Argument(
        ..., exists=True, readable=True, help="Path to the input PDF file."
    ),
    output_dir: Path = typer.Argument(..., help="Directory to save output images."),
    prefix: str = typer.Option("slide_", help="Prefix for output image files."),
    image_format: str = typer.Option("png", help="Image format: png, jpg, etc."),
):
    """Convert all pages of a PDF to images and save them to the output directory."""
    try:
        if not output_dir.exists():
            output_dir.mkdir(parents=True, exist_ok=True)
        doc = fitz.open(str(pdf_path))
        for page_number in range(len(doc)):
            page = doc.load_page(page_number)
            pix = page.get_pixmap()
            out_path = output_dir / f"{prefix}{page_number + 1}.{image_format}"
            pix.save(str(out_path))
        typer.echo(f"Saved {len(doc)} images to {output_dir}")
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
