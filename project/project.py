import speech_recognition as sr

def main():
    ...


def record_speech():
    audio = get_audio()
    with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())


def speech_to_text():
    audio = get_audio()
    recognizer = sr.Recognizer()
    text= recognizer.recognize_google(audio)
    return text


def get_audio():
    recognizer = sr.Recognizer()
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{index}: {name}")
    with sr.Microphone(device_index=1) as source:
        print("Recording ...")
        audio = recognizer.listen(source)
    return audio


if __name__ == "__main__":
    record_speech()
