import numpy as np
import cv2
from flask import Flask, Response
try:
    from PIL import ImageGrab
except:
    import pyscreenshot as ImageGrab

app = Flask(__name__)

def gen():
    while True:
        img=ImageGrab.grab()
        img_np=np.array(img)
        frame=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
        image = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')

@app.route('/')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=True)