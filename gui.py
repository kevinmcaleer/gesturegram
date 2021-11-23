from guizero import App, Text, PushButton

def choose_name():
    print("button pressed")

app = App(title="Hello World")
message = Text(app, text="Welcome to Gesturegram")
button = PushButton(app, choose_name, text="Tell me!")
app.display()
