from guizero import App, Text, PushButton
from guizero.Drawing import Drawing
from cv2 import VideoCapture
import cv2
from tkinter import PhotoImage
from pil import Image
# from picamera import PiCamera
camera = VideoCapture(0)

def choose_name():
    print("button pressed")

def draw_meme(top_text, bottom_text, meme):
    meme.clear()
    ret, image = camera.read()
    b,g,r = cv2.split(image)
    img = cv2.merge((r,g,b))
    # img = PhotoImage()
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im) 
    meme.image(0,0,image)
    meme.text(20,20, top_text.value)
    meme.text(20,320, bottom_text.value)

app = App(title="Hello World")
message = Text(app, text="Welcome to Gesturegram")
button = PushButton(app, choose_name, text="Tell me!")

meme = Drawing(app, width="fill", height="fill")
draw_meme(top_text="top_text", bottom_text="bottom_text", meme=meme)
app.display()
