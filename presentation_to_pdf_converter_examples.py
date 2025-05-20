import slidize


# Basic conversion from a presentation file to PDF
def convert_basic():
    slidize.PresentationToPdfConverter.process("presentation.pptx", "presentation.pdf")


# Conversion with PDF/A-1b compliance level
def convert_with_compliance_level():
    options = slidize.PdfConverterOptions()
    options.compliance_level = slidize.PdfComplianceLevel.PDF_A1B
    slidize.PresentationToPdfConverter.process("presentation.pptx", "presentation.pdf", options)


# Embedding full fonts in the PDF
def convert_with_embedded_fonts():
    options = slidize.PdfConverterOptions()
    options.embed_full_fonts = True
    slidize.PresentationToPdfConverter.process("presentation.pptx", "presentation.pdf", options)


# Including hidden slides in the PDF
def convert_with_hidden_slides():
    options = slidize.PdfConverterOptions()
    options.show_hidden_slides = True
    slidize.PresentationToPdfConverter.process("presentation.pptx", "presentation.pdf", options)


# Exporting notes and comments in the PDF
def convert_with_notes_and_comments():
    slides_view_options = slidize.NotesCommentsViewOptions()
    slides_view_options.notes_position = slidize.NotesPositions.BOTTOM_FULL
    slides_view_options.comments_position = slidize.CommentsPositions.RIGHT
    options = slidize.PdfConverterOptions()
    options.slides_view_options = slides_view_options
    slidize.PresentationToPdfConverter.process("presentation.pptx", "presentation.pdf", options)


# Adjusting JPEG quality in the PDF
def convert_with_jpeg_quality():
    options = slidize.PdfConverterOptions()
    options.jpeg_quality = 85
    slidize.PresentationToPdfConverter.process("presentation.pptx", "presentation.pdf", options)


if __name__ == "__main__":
    convert_basic()
    convert_with_compliance_level()
    convert_with_embedded_fonts()
    convert_with_hidden_slides()
    convert_with_notes_and_comments()
    convert_with_jpeg_quality()
