import slidize


# Basic conversion from a presentation file to TIFF images
def convert_basic():
    slidize.PresentationToTiffConverter.process("presentation.pptx", "slide.tiff")


# Conversion with custom image dimensions
def convert_with_custom_dimensions():
    options = slidize.TiffConverterOptions()
    options.image_width = 1024
    options.image_height = 768
    slidize.PresentationToTiffConverter.process("presentation.pptx", "slide.tiff", options)


# Creating a multipage TIFF from the presentation
def convert_with_multi_page_tiff():
    options = slidize.TiffConverterOptions()
    options.multi_page = True
    slidize.PresentationToTiffConverter.process("presentation.pptx", "presentation.tiff", options)


# Setting a default font for text rendering
def convert_with_default_font():
    options = slidize.TiffConverterOptions()
    options.default_regular_font = "Arial"
    slidize.PresentationToTiffConverter.process("presentation.pptx", "slide.tiff", options)


# Including speaker notes in the output images
def convert_with_speaker_notes():
    slides_view_options = slidize.NotesCommentsViewOptions()
    slides_view_options.notes_position = slidize.NotesPositions.BOTTOM_FULL
    options = slidize.TiffConverterOptions()
    options.slides_view_options = slides_view_options
    slidize.PresentationToTiffConverter.process("presentation.pptx", "slide.tiff", options)


# Applying LZW compression to the TIFF images
def convert_with_lzw_compression():
    options = slidize.TiffConverterOptions()
    options.compression_type = slidize.TiffCompressionTypes.LZW
    slidize.PresentationToTiffConverter.process("presentation.pptx", "slide.tiff", options)


if __name__ == "__main__":
    convert_basic()
    convert_with_custom_dimensions()
    convert_with_multi_page_tiff()
    convert_with_default_font()
    convert_with_speaker_notes()
    convert_with_lzw_compression()
