import pathlib

from fpdf import FPDF
from pathlib import Path
from glob import glob

filepaths = glob("files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")
for filepath in filepaths:
    pdf.add_page()
    pdf.set_font(family="Times", size=18, style="B")
    filename = pathlib.Path(filepath).stem.title()
    pdf.cell(w=0, h=8, txt=filename)

pdf.output("output.pdf")
