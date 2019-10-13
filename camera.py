import cv2

def video():
    video_capture = cv2.VideoCapture(0)
    # Check success
    if not video_capture.isOpened():
        raise Exception("Could not open video device")
    # Read picture. ret === True on success
    ret, frame = video_capture.read()
    # Close device
    video_capture.release()
    cv2.imwrite("static/simplecv.png", frame)