import socketio
import eventlet
import numpy as np
from flask import Flask
from tensorflow.keras.models import load_model

import base64
from io import BytesIO
from PIL import Image
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError





sio = socketio.Server()

app = Flask(__name__) # '__main__'
speed_limit = 20

#  def greeting():
#      return 'Welcome!'

def img_preprocess(img):
  img = img[60:135, :, :] # cut non important img data
  img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV) # YUV for nvidia model
  img = cv2.GaussianBlur(img, (3, 3), 0)
  img = cv2.resize(img, (200, 66))
  img = img/255 # normalization
  return img

@sio.on("telemetry")
def telemetry(sid, data):
    speed = float(data["speed"])
    image = Image.open(BytesIO(base64.b64decode(data["image"])))
    image = img_preprocess(np.asarray(image))
    image = np.array([image])
    steering_angle = float(model.predict(image)) # predicted output
    throttle = 1.0 - speed/speed_limit # caps at speed_limit
    print(f"{steering_angle} {throttle} {speed}")
    send_control(steering_angle, throttle)

@sio.on("connect")
def connect(sid, environment):
    print("Connected")
    send_control(0, 1)

def send_control(steering_angle, throttle):
    sio.emit("steer", data = {
        "steering_angle": steering_angle.__str__(),
        "throttle": throttle.__str__()
    })

if __name__ == "__main__":
    model = load_model("model.h5", compile=False)  # Load the model without compilation
    model.compile(loss=MeanSquaredError())  # Recompile the model with the correct loss function
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(("", 4567)), app)