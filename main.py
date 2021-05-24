import cv2
import pytesseract
import emailDelivery
#import UI

#Reading the image file
#UI.start()
#image=cv2.imread(UI.imname)
#image=cv2.imread('car2.jpg')

# Convert to Grayscale Image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale Image", gray_image)

gg=cv2.bilateralFilter(gray_image,11,17,17)
cv2.imshow("Smoother Image", gg)
#cv2.waitKey(0)

#Canny Edge Detection
canny_edge = cv2.Canny(gg, 170, 200)
cv2.imshow("Canny edge", canny_edge)
cv2.waitKey(0)

# Find contours based on Edges
contours, new  = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours=sorted(contours, key = cv2.contourArea, reverse = True)[:30]
image1=image.copy()
cv2.drawContours(image1, contours,-1, (0,255,0),3)
cv2.imshow("Contoured image", image1)
cv2.waitKey(0)

# Initialize license Plate contour and x,y coordinates
contour_with_license_plate = None
license_plate = None
x = None
y = None
w = None
h = None
# Find the contour with 4 potential corners and creat ROI around it
for contour in contours:
    # Find Perimeter of contour and it should be a closed contour
    perimeter = cv2.arcLength(cotour, True)
    approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)
    if len(approx) == 4: #see whether it is a Rect
        contour_with_license_plate = approx
        x, y, w, h = cv2.boundingRect(contour)
        license_plate = gray_image[y:y + h, x:x + w]
        break
#Text Recognition
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(license_plate)
text=text.lstrip()
text=text.rstrip()
print(text)
emailDelivery.send_emails(text)

#Draw License Plate and write the Text
#image = cv2.rectangle(image, (x,y), (x+w,y+h), (0,0,255), 3) 
#image = cv2.putText(image, text, (x-50,y-50), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0), 6, cv2.LINE_AA)

#cv2.imshow("License Plate Detection",image)
#cv2.waitKey(0)


























