from ultralytics import YOLO
import cv2

img = cv2.imread('photo.jpg')

model = YOLO('best.pt')
class_names = model.names

results = model(img, stream=True)
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        conf = round(box.conf[0].item(),2)
        class_name = class_names[int(box.cls[0])]

        if conf > 0.5:
            cv2.rectangle(img, (x1,y1), (x2,y2), (186, 154, 65), 2)
            cv2.putText(img, class_name, (x1, y1-20), 1, 2, (186, 154, 65), 2)

cv2.imshow('Result', img)

cv2.waitKey(0)