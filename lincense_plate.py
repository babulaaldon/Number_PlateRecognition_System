import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR'

cascade= cv2.CascadeClassifier('haarcascade_russian-plate_number.xml')
states={"RJ":"Rajasthan" , "WB":"West Bengal"}

def extract_numbers(img):
    global read
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    nplate=cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in nplate:
        a,b = (int(0.02*img.shape[0]),int(0.02*img.shape[1]))
        plate = img[y:y+h, x:x+w]


        ##img processing
        kernal = np.ones((5,5),np.uint8)
        plate = cv2.dilate(plate,kernal,iterations=1)
        plate = cv2.erode(plate,kernal,iterations=1)
        plate_gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        (thresh, plate) = cv2.threshold(plate_gray, 127, 255, cv2.THRESH_BINARY)

        ##use of ocr
        read = pytesseract.image_to_string(plate)
        print(read)
        read = ''.join(e for e in read if e.isalnum())
        stat = read[0:4]
        try:
            print('Car Belongs to', states[stat])
        except:
            print('State not recognised:(')
        print(read)
        cv2.rectangle(img,(x,y),(x+w,y+h),(51,51,255),2)
        cv2.rectangle(img,(x,y - 40), (x+w,y),(51,51,255), -1)
        cv2.putText(img, read, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (51,51,255))
        cv2.imshow('Plate',plate)

    cv2.imshow('Result',img)
    cv2.imwrite('result.jph',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

extract_numbers('img1.jpg')

