# main.py

from flask import Flask, render_template, Response
from camera_port2 import VideoCamera1

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_port2.html')

def gen1(camera):
    while True:
        frame1 = camera.get_frame1()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame1 + b'\r\n\r\n')



@app.route('/video_feed1')


def video_feed1():

    pageType='video_feed1'
    

    title="Video feed of saved file"
    return Response(gen1(VideoCamera1()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=5600)
