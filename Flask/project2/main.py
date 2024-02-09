# Live webcam streaming.

from flask import Flask,render_template, Response  
import cv2 

# Here to enable render_template you have to follow folder structure.
# You should create 
#               template
#                       index.html 

app = Flask(__name__)

cam = cv2.VideoCapture(0)

def stream_video():
    while True:
        ret, frame = cam.read()
        if not ret:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/video')
def video():
    return Response(stream_video(),
                    mimetype = 'multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True,  port=8080)