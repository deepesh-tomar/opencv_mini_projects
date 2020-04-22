import cv2
import datetime

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        date = str(datetime.datetime.now())
        frame = cv2.putText(frame, date, (10,50), font, 0.5, (255, 255, 255), 3, cv2.LINE_AA)
        cv2.imshow('live date and time', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
