import cv2
import numpy as np

from servo_motor import ServoMotor
import time
servoMotors = []

servoMotors.append(ServoMotor(Channel=0, ZeroOffset=0))
servoMotors.append(ServoMotor(Channel=1, ZeroOffset=0))
cap = cv2.VideoCapture(0)
x = 90
y = 90

########################################    
def access_pixels(img):
    number = 0
    height = img.shape[0]        #将tuple中的元素取出，赋值给height，width，channels
    width = img.shape[1]
    for row in range(height):    #遍历每一行
        for col in range(width): #遍历每一列   #遍历每个通道（二值化后只有一个通道）
                val = img[row][col]
                if (val) != 0:
                    number =number + 1
    return number
                    
                    
       

#################################################################3
while(True):
    servoMotors[0].setAngle(x)
    servoMotors[1].setAngle(y)
    # Capture frame-by-frame
    img1 = cv2.imread('./Lenna.jpg')
    #img1 = cv2.imread('./Parrots.jpg')
    img2 = cv2.imread('./Parrots.jpg')
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    #img1 = cv2.imread('./Parrots.jpg')
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
   
 
    # Display the resulting frame
    
    #cv2.imshow('Lenna.jpeg', img1)
    #cv2.imshow('Parrots.jpeg', img2)
    #print(img2.shape)
    #print(img1.shape)
    dst  = cv2.absdiff(img1, img2)
    cv2.imwrite('diff.jpg',dst)

    wide = dst.shape[0]
    depth = dst.shape[1]
    cropped_image = dst[0:(wide//2), 0:(depth//2)]
    cropped_image1 = dst[(wide//2):wide, 0:(depth//2)]
    cropped_image2 = dst[0:(wide//2), (depth//2):depth]
    cropped_image3 = dst[(wide//2):wide, (depth//2):depth]
    
    cv2.imshow("cropped", cropped_image)
    cv2.imshow("cropped1", cropped_image1)
    cv2.imshow("cropped2", cropped_image2)
    cv2.imshow("cropped3", cropped_image3)
    cv2.imshow('dst', dst)
    cropped_image_number = access_pixels(cropped_image)
    cropped_image_number1 = access_pixels(cropped_image1)
    cropped_image_number2 = access_pixels(cropped_image2)
    cropped_image_number3 = access_pixels(cropped_image3)

    if  (cropped_image_number + cropped_image_number1 > cropped_image_number2 + cropped_image_number3):
    
        if y <= 180:
            print('up +',end = '')
            y = y + 1
    else:
        if y >= 0:
            print('down +',end = '')
            y = y - 1
    if  (cropped_image_number + cropped_image_number2 > cropped_image_number1 + cropped_image_number3):

        if x >= 0:
            print('left')
            x = x - 1
    else:
        
        if x <= 180:
            print('right')
            x = x  + 1
        
    

#     print(dst.shape[1])
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows()
 
# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()
#img1 = cv2.imread('./Lenna.jpeg')
#cv2.imshow('Lenna',img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows