import cv2
import threading
# Import DeepStack's Python SDK
from deepstack_sdk import ServerConfig, Detection


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


def video_stream():
    while(True):
        ret, frame = capture.read()
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":

    # Initiate Connection to DeepStack
    config = ServerConfig("http://localhost:3000")
    detection = Detection(config)

    # Initiate Connection to iPhone IP Camera
    capture = cv2.VideoCapture(
        'rtsp://admin:Hopelovemws_59@192.168.1.51:554/11')

    # do thread video stream right here.
    videoStreamThread = threading.Thread(target=video_stream, args=())
    videoStreamThread.start()

    # After the loop release the cap detectionect
    capture.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
