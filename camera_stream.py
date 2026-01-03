import time
from flask import Flask, Response
from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput

app = Flask(__name__)
picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))

class StreamingOutput(FileOutput):
    def __init__(self):
        super().__init__()
        self.frame = None
        self.lock = threading.Lock()

    def write(self, buf):
        with self.lock:
            self.frame = buf

def generate_frames():
    output = StreamingOutput()
    picam2.start_recording(JpegEncoder(), output)
    try:
        while True:
            with output.lock:
                frame = output.frame
            if frame:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            time.sleep(0.03) # Adjust for desired frame rate
    finally:
        picam2.stop_recording()

@app.route('/')
def index():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    import threading
    app.run(host='0.0.0.0', port=8000, threaded=True) # Run on all interfaces, port 8000
