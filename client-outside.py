#!/usr/bin/env python3

import cv2
from pprint import pprint

cap = cv2.VideoCapture('rtsp://10.0.250.10:554/user=admin&password=&channel=2&stream=1.sdp?real_stream')

while True:

    ret, frame = cap.read()
    cv2.imshow("Outside",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
