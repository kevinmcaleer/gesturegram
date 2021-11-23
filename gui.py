from guizero import App, Text, PushButton
from guizero.Drawing import Drawing
from picamera import PiCamera

def choose_name():
    print("button pressed")

def draw_meme(top_text, bottom_text, meme):
    meme.clear()
    meme.image(0,0,"")
    meme.text(20,20, top_text.value)
    meme.text(20,320, bottom_text.value)

app = App(title="Hello World")
message = Text(app, text="Welcome to Gesturegram")
button = PushButton(app, choose_name, text="Tell me!")

meme = Drawing(app, width="fill", height="fill")
draw_meme(top_text="top_text", bottom_text="bottom_text", meme=meme)
app.display()
