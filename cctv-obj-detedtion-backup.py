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


if __name__ == "__main__":

    # Initiate Connection to DeepStack
    config = ServerConfig("http://localhost:3000")
    detection = Detection(config)

    # Initiate Connection to iPhone IP Camera
    capture = cv2.VideoCapture(
        'rtsp://admin:Hopelovemws_59@192.168.1.50:554/11')

    while(True):
        # Capture the video frame
        # by frame
        ret, frame = capture.read()

        if not frame is None:
            if ret:
                # Detect the Frame with DeepStack using the Python SDK
                detections = detection.detectObject(frame,output=None)

                # Draw the detections on the frame
                frame = draw_detections(frame, detections)

                # Display the frame and the detections
                cv2.imshow('frame', frame)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap detectionect
    capture.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
