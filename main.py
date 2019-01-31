import json
from text_to_speech import Speech
from speech_to_text import Recognizer
from watson import Watson
import datetime


def load_config():
    with open('config.json') as f:
        return json.load(f)


def init_services():
    global assistant, tts, recognizer
    print("Initializing conversation...")
    assistant = Watson()
    print("Initializing voice...")
    tts = Speech()
    print("Initializing speech recognition...")
    recognizer = Recognizer()
    print("Initializing web server...")


def update_data():
    delay_ms = 500
    global next_update
    td = (next_update - datetime.datetime.now()).total_seconds() * 1000
    if td < 0:
        next_update = datetime.datetime.now() + datetime.timedelta(milliseconds=delay_ms)


if __name__ == "__main__":
    next_update = datetime.datetime.min
    config = load_config()
    init_services()

    print("Watson:", assistant.message(""))
    while True:
        update_data()

    # if buttonPressed:
    # message = assistant.message(recognizer.listen())
    # print("Watson:", message)
    # tts.say(message)
