import slidize


# Basic conversion from a presentation file to JPEG images
def convert_basic():
    slidize.PresentationToSvgConverter.process("presentation.pptx", "slide.svg")


# Setting a default font for text rendering
def convert_with_default_font():
    options = slidize.SvgConverterOptions()
    options.default_regular_font = "Arial"
    slidize.PresentationToSvgConverter.process("presentation.pptx", "slide.svg", options)


# Managing the compression level of pictures
def convert_with_picture_compression():
    options = slidize.SvgConverterOptions()
    options.pictures_compression = slidize.PicturesCompressionLevel.DPI150
    slidize.PresentationToSvgConverter.process("presentation.pptx", "slide.svg", options)


# Vectorizing text for improved quality
def convert_with_vectorized_text():
    options = slidize.SvgConverterOptions()
    options.vectorize_text = True
    slidize.PresentationToSvgConverter.process("presentation.pptx", "slide.svg", options)


# Adjusting JPEG quality in the SVG
def convert_with_jpeg_quality():
    options = slidize.SvgConverterOptions()
    options.jpeg_quality = 85
    slidize.PresentationToSvgConverter.process("presentation.pptx", "slide.svg", options)


# Controlling the resolution of rasterized metafiles
def convert_with_metafile_rasterization_dpi():
    options = slidize.SvgConverterOptions()
    options.metafile_rasterization_dpi = 150
    slidize.PresentationToSvgConverter.process("presentation.pptx", "slide.svg", options)


if __name__ == "__main__":
    convert_basic()
    convert_with_default_font()
    convert_with_picture_compression()
    convert_with_vectorized_text()
    convert_with_jpeg_quality()
    convert_with_metafile_rasterization_dpi()
