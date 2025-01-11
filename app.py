from flask import Flask, render_template, render_template_string, Response
from datetime import datetime
from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import pygame
import mysql.connector
from twilio.rest import Client


app = Flask(__name__)

audio_path = "music/2.wav"

# Twilio's credentials (replace with your own)   {CX69UDTU1BNQYZHZU3U8FSR3}
account_sid = 'ACa79a8cdf892ddabc4bace5ec290a52ef'
auth_token = 'd520f51db5dd2c5ccde144614339ba4c'
twilio_phone_number = '+17175849972'
recipient_phone_number = '+917439463606'

# Initialize the YOLO model and other required variables
model = YOLO("YOLO_Weights/facehand.pt")
classNames = ['Not Wild', 'Wild']

cap = cv2.VideoCapture(0)
cap.set(3, 4096)
cap.set(4, 2160)


def send_sms(message):
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )


# Helper function to count hands
def count_hands(frame):
    count = 0
    results = model(frame, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            class_type = classNames[cls]
            conf = math.ceil((box.conf[0] * 100)) / 100
            if class_type == "Wild" and conf > 0.65:
                count += 1
    return count


def get_db_cursor():
    mydb = mysql.connector.connect(
        host="localhost",
        user="shayan",
        password="apple.CLOUD@2001",
        database="wild_life"
    )
    return mydb.cursor()




@app.route('/home')
def home():
    return render_template('Home.html')


def generate_frames():
    while True:
        success, img = cap.read()

        # Check if the frame is not successful
        if not success:
            send_sms("Camera is not working or blocked!")
            status_box_color = (0, 0, 255)  # Red when camera is blocked
        else:
            # Calculate the mean brightness of the frame
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            mean_brightness = gray_img.mean()

            # Check if the brightness is below a threshold (indicating the camera is dark)
            if mean_brightness < 50:  # Adjust the threshold as needed
                send_sms("Camera is dark or blocked!")
                status_box_color = (0, 0, 255)  # Red when the camera is dark or blocked
            else:
                status_box_color = (0, 255, 0)  # Green when the camera is working

        # Draw the status box in the video (top left corner)
        cv2.rectangle(img, (10, 10), (500, 50), status_box_color, -1)  # Draw a filled rectangle
        cv2.putText(img, "Camera Status: " + ("Blocked" if status_box_color == (0, 0, 255) else "Working"),
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                cls = int(box.cls[0])
                class_type = classNames[cls]
                conf = math.ceil((box.conf[0] * 100)) / 100

                # Count hands in the current frame
                hand_count = count_hands(img)
                print("Number of hands detected:", hand_count)

                if conf > 0.60:
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
                    cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

                if classNames[cls] == "Wild" and conf > 0.65:
                    pygame.mixer.init()
                    pygame.mixer.music.load(audio_path)
                    pygame.mixer.music.play(-1)
                    pygame.time.wait(100)
                else:
                    pygame.mixer.init()
                    pygame.mixer.music.stop()

        # Convert the frame to JPEG
        _, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/points')
def points():
    return render_template_string("{% include 'Signals.html' %}")


@app.route('/dataset')
def creator():
    return render_template_string("{% include 'DataSet.html' %}")


@app.route('/research-paper')
def research():
    return render_template_string("{% include 'Research_paper.html' %}")


@app.route('/')
def login():
    return render_template_string("{% include 'Login.html' %}")


if __name__ == '__main__':
    app.run()