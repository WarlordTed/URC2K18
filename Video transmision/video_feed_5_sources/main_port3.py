
from flask import Flask, render_template, Response
from camera_port3 import VideoCamera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_port3.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():

    title="Video feed of camera"
    pageType='camerafeed'
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=5800)
