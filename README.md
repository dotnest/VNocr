# VNocr
OCR script for Visual Novels/general text on images

## How it works (requirements/installation)

1. `xfce4-screenshooter`  
screenshots a region and saves it to ~/ocr.png  
swap it to your own screenshot program if it doesn't work  
1. `tesseract`  
processes that image and outputs the text it finds to ~/ocr.txt  
install [tesseract](https://github.com/tesseract-ocr/tesseract) (I used `sudo apt install tesseract-ocr` on xubuntu)  
and [download](https://github.com/tesseract-ocr/tessdata_best) and put trained models for the language you need where they belong (it was `/usr/share/tesseract-ocr/4.00/tessdata` for me)  
1. `tr`  
cleans up output text from tesseract  
1. `xclip`  
passes text in clipboard with where it is caught by yomichan  
that opens a popup with that text where you can look up word definitions  
make sure to check "Enable native popups when copying Japanese text" in yomichan options  
(be careful when copying big texts that can contain kana/kanji in them)  

## Usage

- Bind `ocr_script` to a hotkey
- Press the hotkey
- Select a region with text
- Text extracted by OCR will be copied to clipboard

### Additional links

[Tesseract Docs - Improving Recognition Quality](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html)
[StackOverflow - Remove background text and noise from an image using image processing with OpenCV](https://stackoverflow.com/questions/60145306/remove-background-text-and-noise-from-an-image-using-image-processing-with-openc/60404579#60404579)
[StackOverflow - How to remove background noise in image without damaging text?](https://stackoverflow.com/questions/57241151/how-to-remove-background-noise-in-image-without-damaging-text)
[StackOverflow - Background image cleaning for OCR](https://stackoverflow.com/questions/58636157/background-image-cleaning-for-ocr)