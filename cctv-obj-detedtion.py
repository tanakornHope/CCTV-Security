import cv2
import threading
import numpy as np
# Import DeepStack's Python SDK
from deepstack_sdk import ServerConfig, Detection

class globalBS():
    bsA = None
    bsB = None

# Function to draw detections and object names on camera frames
def draw_detections(img, detections):
    for detection in detections:
        output_font_scale = 0.8e-3 * img.shape[0]
        label = detection.label
        img = cv2.rectangle(
            img,
            (detection.x_min, detection.y_min),
            (detection.x_max, detection.y_max),
            (0, 146, 224),
            2
        )
        img = cv2.putText(
            img=img,
            text=label + " ( " + str(100*detection.confidence)+"% )",
            org=(detection.x_min-10, detection.y_min-10),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=output_font_scale,
            color=(0, 146, 224),
            thickness=2
        )

    return img


def objDetectionProcessor():
    while(True):
        if not globalBS.bsA is None:
            detections = detection.detectObject(globalBS.bsA,output=None)
            processedframe = draw_detections(globalBS.bsA, detections)
            # Display the frame and the detections
            cv2.imshow('frame', processedframe)
            cv2.waitKey(1)

def video_stream():
    while(True):
        ret, frame = capture.read()
        globalBS.bsA = frame
        # f = frame
        """ if cv2.waitKey(1) & 0xFF == ord('q'):
            break """

    """ capture.release()
    cv2.destroyAllWindows() """

if __name__ == "__main__":

    # Initiate Connection to DeepStack
    config = ServerConfig("http://localhost:3000")
    global detection 
    detection = Detection(config)
    global capture, f

    capture = cv2.VideoCapture(
        'rtsp://admin:Hopelovemws_59@192.168.1.51:554/11')

    # do thread video stream right here.
    t1 = threading.Thread(target=video_stream, args=())
    t1.start()
    # do thread as image processing right here.
    t2 = threading.Thread(target=objDetectionProcessor, args=())
    t2.start()




