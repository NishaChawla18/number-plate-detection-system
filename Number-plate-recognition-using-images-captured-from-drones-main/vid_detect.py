import cv2
import pytesseract

# Read the video file
cap = cv2.VideoCapture(r'C:\Users\HP\Downloads\Number-plate-recognition-using-images-captured-from-drones-main\Number-plate-recognition-using-images-captured-from-drones-main\Data\vid.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    # Apply image segmentation on each frame to extract the number plate
    # Use OCR (Optical Character Recognition) to recognize the characters on the license plate
    # Display the resulting frame
    cv2.imshow('Frame',frame)
    text = pytesseract.image_to_string(frame, config='--psm 11')

    # Print the recognized text
    print(text)
    # Press Q on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  # Break the loop
  else: 
    break
   

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
