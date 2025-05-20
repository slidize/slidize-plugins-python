import slidize


# Merge multiple presentations into a single presentation file
def merge_presentations():
    input_paths = ["presentation1.pptx", "presentation2.pptx", "presentation3.pptx"]
    output_path = "merged_presentation.pptx"

    slidize.PresentationMerger.process(input_paths, output_path)


if __name__ == "__main__":
    merge_presentations()
