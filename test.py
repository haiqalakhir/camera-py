import cv2
import imutils

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    resized_frame = imutils.resize(frame, width=800)

    cv2.imshow('RC', resized_frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    if cv2.getWindowProperty('RC', cv2.WND_PROP_VISIBLE)<1:
        break

cam.release()
cv2.destroyAllWindows()