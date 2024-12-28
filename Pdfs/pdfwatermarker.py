from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def merge_pdfs(pdf1_path, pdf2_path, merged_pdf_output):
    writer = PdfWriter()
    for pdf_path in (pdf1_path, pdf2_path):
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)

    with open(merged_pdf_output, "wb") as merged_file:
        writer.write(merged_file)
    print(f"Merged PDF saved as: {merged_pdf_output}")

def create_watermark(watermark_text, watermark_file):
    c = canvas.Canvas(watermark_file, pagesize=letter)
    c.setFont("Helvetica", 40)
    c.setFillGray(0.5, 0.5)  # Light gray text
    c.drawString(200, 500, watermark_text)
    c.save()

def add_watermark(input_pdf_path, output_pdf_path, watermark_pdf):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    watermark_reader = PdfReader(watermark_pdf)
    watermark_page = watermark_reader.pages[0]

    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output_pdf_path, "wb") as watermarked_file:
        writer.write(watermarked_file)
    print(f"Watermarked PDF saved as: {output_pdf_path}")

if __name__ == "__main__":
    pdf1 = "file1.pdf"
    pdf2 = "file2.pdf"
    merged_pdf = "merged.pdf"
    final_pdf = "watermarked_merged.pdf"
    watermark_pdf = "watermark.pdf"

    # Merge PDFs
    merge_pdfs(pdf1, pdf2, merged_pdf)

    # Create watermark
    create_watermark("Confidential", watermark_pdf)

    # Add watermark to merged PDF
    add_watermark(merged_pdf, final_pdf, watermark_pdf)
