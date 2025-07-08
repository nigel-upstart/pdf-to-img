# PDF to Image CLI

A simple Python CLI tool to convert all pages of a PDF file into images using [Typer](https://typer.tiangolo.com/) and [PyMuPDF](https://pymupdf.readthedocs.io/) (imported as `fitz`).

- **No project setup required**: Uses PEP 723 inline dependencies and can be run directly with [uv](https://docs.astral.sh/uv/guides/scripts/#running-a-script-with-dependencies).
- **Fast and easy**: Converts each page of a PDF to an image file in your chosen format.

---

## Features
- Convert every page of a PDF to an image (PNG, JPG, etc.)
- Specify output directory and filename prefix
- Simple CLI interface powered by Typer
- No need for a virtual environment or requirements file

---

## Requirements
- Python 3.8+
- [uv](https://docs.astral.sh/uv/) (for running with inline dependencies)

---

## Installation

No installation required! Just clone/download this repo and run the script with `uv`:

```sh
uv run main.py pdf-to-images input.pdf output_dir
```

- `input.pdf`: Path to your PDF file
- `output_dir`: Directory where images will be saved (created if it doesn't exist)

### Optional arguments
- `--prefix`: Prefix for output image files (default: `slide_`)
- `--image-format`: Image format (default: `png`)

#### Example:
```sh
uv run main.py pdf-to-images slides.pdf images/ --prefix page_ --image-format jpg
```

---

## Usage

```sh
uv run main.py pdf-to-images <PDF_PATH> <OUTPUT_DIR> [--prefix PREFIX] [--image-format FORMAT]
```

Example output files:
- `output_dir/slide_1.png`
- `output_dir/slide_2.png`
- ...

---

## Why `fitz` and not `pymupdf`?

- The package is installed as `pymupdf`, but for historical reasons, you import it as `fitz` in your Python code. As of PyMuPDF 1.24.3+, you can also use `import pymupdf`, but `import fitz` remains widely supported and is used in most examples. [Read more here.](https://artifex.com/blog/pymupdf-1.24.3-and-farewell-to-fitz)

---

## Contributing

Pull requests and issues are welcome! Please open an issue to discuss any major changes before submitting a PR.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
