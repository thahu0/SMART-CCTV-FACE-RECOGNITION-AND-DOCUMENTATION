import cv2
import pandas as pd
import numpy as np
from datetime import datetime
from ultralytics import YOLO
from tracker import *

model = YOLO('yolov8s.pt')

area1 = [(312, 388), (289, 390), (474, 469), (497, 462)]
area2 = [(279, 392), (250, 397), (423, 477), (454, 469)]

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture('peoplecounteryolov8-main\peoplecount1.mp4')

my_file = open("peoplecounteryolov8-main/coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")

count = 0   
tracker = Tracker()
people_entering = set()
people_exiting = set()

while True:    
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 2 != 0:
        continue
    frame = cv2.resize(frame, (1020, 500))
    
    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
    list = []
             
    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        c = class_list[d]
        if 'person' in c:
            list.append([x1, y1, x2, y2])
    
    bbox_id = tracker.update(list)
    for bbox in bbox_id:
        x3, y3, x4, y4, id = bbox
        result1 = cv2.pointPolygonTest(np.array(area1, np.int32), ((x4, y4)), False)
        result2 = cv2.pointPolygonTest(np.array(area2, np.int32), ((x4, y4)), False)
        if result1 >= 0:
            if id not in people_entering:
                people_entering.add(id)
            cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 2)
        elif result2 >= 0:
            if id in people_entering:
                people_exiting.add(id)
                people_entering.remove(id)
            cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 255, 0), 2)
      
    cv2.polylines(frame, [np.array(area1, np.int32)], True, (255, 0, 0), 2)
    cv2.putText(frame, "Entering: {}".format(len(people_entering)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.polylines(frame, [np.array(area2, np.int32)], True, (255, 0, 0), 2)
    cv2.putText(frame, "Exiting: {}".format(len(people_exiting)), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    # Get current date and time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # Overlay date and time onto the frame
    cv2.putText(frame, dt_string, (frame.shape[1] - 200, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

