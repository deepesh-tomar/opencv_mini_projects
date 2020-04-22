import cv2 
import datetime as dt

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    r, frame = cap.read()
    if r == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        RGB_to_BGR = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        date = str(dt.datetime.now())
        frame = cv2.putText(frame, date, (10,50), font, 1, (255, 255, 255), 2 , cv2.LINE_AA)
        gray = cv2.putText(gray, date, (10,50), font, 1, (255, 255, 255), 3, cv2.LINE_AA)
        HSV = cv2.putText(HSV, date, (10,50), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        RGB_to_BGR = cv2.putText(RGB_to_BGR, date, (10,50), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        
        cv2.imshow('live date and time-original', frame)
        cv2.imshow('live date and time-gray', gray)
        cv2.imshow('live date and time-hsv', HSV)
        cv2.imshow('live date and time- RGB2BGR', RGB_to_BGR)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
