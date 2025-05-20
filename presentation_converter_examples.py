import slidize


# Convert a legacy PowerPoint presentation (PPT) to the modern PPTX format
def convert_ppt_to_pptx():
    slidize.PresentationConverter.process("input.ppt", "output.pptx")


# Convert a PowerPoint presentation (PPTX) to the OpenDocument Presentation format (ODP)
def convert_pptx_to_odp():
    slidize.PresentationConverter.process("input.pptx", "output.odp")


# Convert a presentation to a PowerPoint template format (POTX)
def convert_to_potx():
    slidize.PresentationConverter.process("input.pptx", "output.potx")


# Convert a presentation to a macro-enabled PowerPoint format (PPTM)
def convert_to_pptm():
    slidize.PresentationConverter.process("input.pptx", "output.pptm")


# Convert a presentation to a PowerPoint Show format (PPSX)
def convert_to_ppsx():
    slidize.PresentationConverter.process("input.pptx", "output.ppsx")


# Convert a presentation to a macro-enabled PowerPoint Show format (PPSM)
def convert_to_ppsm():
    slidize.PresentationConverter.process("input.pptx", "output.ppsm")


# Convert a presentation to an OpenDocument Flat XML Presentation format (FODP)
def convert_to_fodp():
    slidize.PresentationConverter.process("input.pptx", "output.fodp")


# Convert a presentation to an OpenDocument Presentation Template format (OTP)
def convert_to_otp():
    slidize.PresentationConverter.process("input.pptx", "output.otp")


# Convert a presentation to a PowerPoint XML Presentation format
def convert_to_xml():
    slidize.PresentationConverter.process("input.pptx", "output.xml")


# Convert a presentation using streams instead of file paths
def convert_using_streams():
    with open("input.pptx", "rb") as input_stream, open("output.pptx", "wb") as output_stream:
        slidize.PresentationConverter.process(input_stream, output_stream, slidize.ConvertFormat.PPTX)


if __name__ == "__main__":
    convert_ppt_to_pptx()
    convert_pptx_to_odp()
    convert_to_potx()
    convert_to_pptm()
    convert_to_ppsx()
    convert_to_ppsm()
    convert_to_fodp()
    convert_to_otp()
    convert_to_xml()
    convert_using_streams()
