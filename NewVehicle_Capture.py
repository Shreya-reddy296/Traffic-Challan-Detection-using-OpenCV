from cv2 import cv2
import os

path='C:/Users/New/Desktop/ALPR Project'
def captureImage(name):
    vc=cv2.VideoCapture(0)
    while(True):
        check,frame=vc.read()
        #print(frame)
        frame=cv2.flip(frame,1)
        #print("hi")
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('New Enrollment( Enter C to capture)',frame)

        key=cv2.waitKey(1)
        if key==ord('c'):
            cv2.imwrite(os.path.join(path,name+'.jpg'),frame)
            print("success")
            break
    vc.release()
    cv2.destroyAllWindows()
#captureImage('proj')