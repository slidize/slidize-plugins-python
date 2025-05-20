import io
import slidize


# Basic conversion from file paths
def convert_basic():
    slidize.PresentationToHtmlConverter.process("presentation.pptx", "presentation.html")


# Stream-based conversion
def convert_stream_based():
    with open("presentation.pptx", "rb") as input_stream, io.BytesIO() as output_stream:
        slidize.PresentationToHtmlConverter.process(input_stream, output_stream)


# Conversion with default font setting
def convert_with_default_font():
    options = slidize.HtmlConverterOptions()
    options.default_regular_font = "Arial"
    slidize.PresentationToHtmlConverter.process("presentation.pptx", "presentation.html", options)


# Adjusting picture compression level
def convert_with_picture_compression():
    options = slidize.HtmlConverterOptions()
    options.pictures_compression = slidize.PicturesCompressionLevel.DPI150
    slidize.PresentationToHtmlConverter.process("presentation.pptx", "presentation.html", options)


# Removing cropped areas of images
def convert_without_cropped_areas():
    options = slidize.HtmlConverterOptions()
    options.delete_pictures_cropped_areas = True
    slidize.PresentationToHtmlConverter.process("presentation.pptx", "presentation.html", options)


# Setting JPEG image quality
def convert_with_jpeg_quality():
    options = slidize.HtmlConverterOptions()
    options.jpeg_quality = 85
    slidize.PresentationToHtmlConverter.process("presentation.pptx", "presentation.html", options)


# Customizing slide view options
def convert_with_slide_view():
    slides_view_options = slidize.HandoutViewOptions()
    slides_view_options.handout = slidize.HandoutViewType.HANDOUTS_4_HORIZONTAL
    options = slidize.HtmlConverterOptions()
    options.slides_view_options = slides_view_options
    slidize.PresentationToHtmlConverter.process("presentation.pptx", "presentation.html", options)


# Handling different presentation formats
def convert_odp_to_html():
    slidize.PresentationToHtmlConverter.process("presentation.odp", "presentation.html")


if __name__ == "__main__":
    convert_basic()
    convert_stream_based()
    convert_with_default_font()
    convert_with_picture_compression()
    convert_without_cropped_areas()
    convert_with_jpeg_quality()
    convert_with_slide_view()
    convert_with_slide_view()
    convert_odp_to_html()
