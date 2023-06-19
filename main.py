from fpdf import FPDF
from pathlib import Path
from glob import glob

# Create a list of text filepaths
filepaths = glob("files/*.txt")
# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Iterate through each text file
for filepath in filepaths:
    # Add a page to PDF for each text file
    pdf.add_page()

    # Get the filename without extension and title it
    filename = Path(filepath).stem.title()

    # Add the filename to the PDF
    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=50, h=8, txt=filename, ln=1)

    # Get the content of each file
    with open(filepath, 'r') as txt_file:
        content = txt_file.read()

    pdf.set_font(family="Times", size=11)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("output.pdf")
