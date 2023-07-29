import cv2
import numpy as np
from PIL import Image,ImageEnhance
import pytesseract

plat_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
video = cv2.VideoCapture(r'C:\Users\HP\Downloads\Number-plate-recognition-using-images-captured-from-drones-main\Number-plate-recognition-using-images-captured-from-drones-main\Data\vid.mp4')

if(video.isOpened()==False):
 print('Error Reading Video')

while True:
    ret,frame = video.read() 
    gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plate = plat_detector.detectMultiScale(gray_video,scaleFactor=1.2,minNeighbors=5,minSize=(25,25))


    for (x,y,w,h) in plate:
        
        
        img = Image.fromarray(frame[y:y+h,x:x+w]).convert("RGBA")
        img = ImageEnhance.Sharpness(img).enhance(5)
        text = pytesseract.image_to_string(img, config='--psm 9')
        # print(text)
        img.save("teST.PNG")
        # break 
        # frame[y:y+h,x:x+w] =  cv2.blur(frame[y:y+h,x:x+w],ksize=(10,10))
        cv2.rectangle(frame,(x,y), (x+w,y+h), (255,0,0),2)
        cv2.putText(frame,text=text,org=(x-3,y+10+h),fontFace=cv2.FONT_HERSHEY_COMPLEX,color=(0,0,255),thickness=1,fontScale=0.4)
        cv2.putText(frame,text='License Plate',org=(x-3,y-3),fontFace=cv2.FONT_HERSHEY_COMPLEX,color=(0,0,255),thickness=1,fontScale=0.6)
        

        # Print the recognized text
    
        if ret == True:
            cv2.imshow('Video', frame)

        if cv2.waitKey(50) & 0xFF == ord("q"):
            break
        else:
            break
    # break;
video.release()
cv2.destroyAllWindows()

