from slack_bolt import App

app = App(token="xoxb-8661595125730-8656744230565-8XCjor42KgY4TWcbiSl33RXC")

@app.event("message")
def handle_message(event, say):
    text = event.get("text", "").lower()
    if "hola" in text:
        say("¡Hola! ¿En qué puedo ayudarte?")

if __name__ == "__main__":
    app.start(port=3000)
