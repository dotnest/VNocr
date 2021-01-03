try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

image_name = "0.png"

print(pytesseract.image_to_string(Image.open(image_name), lang="jpn"))

for i in range(10):
    text = pytesseract.image_to_string(Image.open(f"{i}.png"), lang="jpn")
    newlines = text.count("\n")
    print("new lines:", newlines)
    text = text.replace(" ", "").replace("\n", "")
    print(f"{i}.png :")
    print(text)
    print()

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
# print(pytesseract.image_to_string(image_name))

# Batch processing with a single file containing the list of multiple image file paths
# print(pytesseract.image_to_string("images.txt"))