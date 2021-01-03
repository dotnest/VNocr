# thanks to nathancy from stackoverflow for this
# https://stackoverflow.com/a/60404579
import cv2
import pytesseract
import numpy as np

# path to tesseract.exe if you're on windows
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def process_image(image_stub, to_ocr=False, to_dissect=False):
    image_stub = str(image_stub)

    # Load image, grayscale, Otsu's threshold
    image = cv2.imread(f"{image_stub}.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph open to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

    # Find contours and remove small noise
    cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        area = cv2.contourArea(c)
        if area < 50:
            cv2.drawContours(opening, [c], -1, 0, -1)

    # Invert and apply slight Gaussian blur
    result = 255 - opening
    result = cv2.GaussianBlur(result, (3, 3), 0)

    if to_ocr:
        # Perform OCR
        text = pytesseract.image_to_string(result, lang="jpn", config="--psm 6")
        text = text.replace(" ", "").replace("\n", "").replace("\x0c", "")
        # print(repr(text))
        print(text)

    if to_dissect:
        cv2.imshow("thresh", thresh)
        cv2.imshow("opening", opening)
        cv2.imshow("result", result)
        cv2.waitKey()

    cv2.imwrite(f"{image_stub}_result.png", result)


# for i in range(11):
#     process_image(i)

process_image(12)
