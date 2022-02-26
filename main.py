import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/Cellar/tesseract/5.0.1/bin/tesseract'
tessdata_dir_config = '/opt/homebrew/Cellar/tesseract/5.0.1/share/tessdata'
img = cv2.imread('5.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img, config=tessdata_dir_config, lang='tha'))

###Detection
#print(pytesseract.image_to_boxes(img, config=tessdata_dir_config))
hImg,wImg,_ = img.shape
boxs = pytesseract.image_to_boxes(img, config=tessdata_dir_config)
for i in boxs.splitlines():
    i = i.split()
    print(i)
    x, y, w, h = int(i[1]), int(i[2]), int(i[3]), int(i[4])
    cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 2)


extract = pytesseract.image_to_string(Image.open('5.png'), lang='tha').replace(' ', '')
print(extract)

cv2.imshow('Result', img)
cv2.waitKey(0)