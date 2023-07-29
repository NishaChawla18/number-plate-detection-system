import pytesseract
import PIL
img = PIL.Image.open("teST.PNG")
for i in range(14):
    try:
        print(pytesseract.image_to_string(img, config='--psm 9'),"==>",i)
        
    except:
        print("ERR",i)