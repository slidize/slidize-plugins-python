import slidize


# Basic conversion from a presentation file to JPEG images
def convert_basic():
    slidize.PresentationToJpegConverter.process("presentation.pptx", "slide.jpg")


# Conversion with custom image dimensions
def convert_with_custom_dimensions():
    options = slidize.ImageConverterOptions()
    options.image_width = 1024
    options.image_height = 768
    slidize.PresentationToJpegConverter.process("presentation.pptx", "slide.jpg", options)


# Scaling images by a factor
def convert_with_image_scaling():
    options = slidize.ImageConverterOptions()
    options.image_scale = 1.5
    slidize.PresentationToJpegConverter.process("presentation.pptx", "slide.jpg", options)


# Setting a default font for text rendering
def convert_with_default_font():
    options = slidize.ImageConverterOptions()
    options.default_regular_font = "Arial"
    slidize.PresentationToJpegConverter.process("presentation.pptx", "slide.jpg", options)


# Including speaker notes in the output images
def convert_with_speaker_notes():
    slides_view_options = slidize.NotesCommentsViewOptions()
    slides_view_options.notes_position = slidize.NotesPositions.BOTTOM_FULL
    options = slidize.ImageConverterOptions()
    options.slides_view_options = slides_view_options
    slidize.PresentationToJpegConverter.process("presentation.pptx", "slide.jpg", options)


# Including comments in the output images
def convert_with_comments():
    slides_view_options = slidize.NotesCommentsViewOptions()
    slides_view_options.comments_position = slidize.CommentsPositions.RIGHT
    options = slidize.ImageConverterOptions()
    options.slides_view_options = slides_view_options
    slidize.PresentationToJpegConverter.process("presentation.pptx", "slide.jpg", options)


if __name__ == "__main__":
    convert_basic()
    convert_with_custom_dimensions()
    convert_with_image_scaling()
    convert_with_default_font()
    convert_with_speaker_notes()
    convert_with_comments()
