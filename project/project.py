import speech_recognition as sr

def main():
    ...


def record_speech(audio):
    with open("recorded.wav", "wb") as f:
        f.write(audio.get_wav_data())


def speech_to_text(audio):
    recognizer = sr.Recognizer()
    text = recognizer.recognize_google(audio)
    return text


def get_audio():
    recognizer = sr.Recognizer()
    device = get_input_device()
    with sr.Microphone(device_index=device) as source:
        print("Recording ...")
        audio = recognizer.listen(source)
    return audio


def get_input_device():
     mic_devices = sr.Microphone.list_microphone_names()
     for index, device in enumerate(mic_devices):
          if "mapper" not in device.lower() and "virtual" not in device.lower():
               return index


if __name__ == "__main__":
    record_speech(get_audio())
