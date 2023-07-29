import cv2
import pytesseract

# Read the image


img = cv2.imread(r'C:\Users\HP\Downloads\Number-plate-recognition-using-images-captured-from-drones-main\Number-plate-recognition-using-images-captured-from-drones-main\Data\1.png')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Apply median blur
gray = cv2.medianBlur(gray, 3)

# Find contours
contours = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\Tesseract-OCR\tesseract.exe'

# Loop over the contours
for contour in contours:
    # Get the bounding rectangle
    x, y, w, h = cv2.boundingRect(contour)

    # Crop the image to the bounding rectangle
    roi = img[y:y + h, x:x + w]


    # Apply OCR using Tesseract
    
    text = pytesseract.image_to_string(roi, config='--psm 11')

    # Print the recognized text
    print(text)
