import cv2

video=cv2.VideoCapture(0) #for camera
while True:
    ret,frame = video.read() #for frame
    cv2.imshow("Frame",frame)
    k=cv2.waitkey(1)
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
    