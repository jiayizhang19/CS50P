import speech_recognition as sr
from scipy.io.wavfile import write
import sounddevice as sd
import whisper

def main():
    audio = get_audio()
    recording = get_audio_until_enter()
    record_speech(recording)
    print(speech_to_text(recording))
    


def live_speech_to_text():
    ...

def recording_to_text(recording = "manual_recording.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(recording)
    print(result["text"])
    with open("transcript.txt", "a") as f:
        f.write(f'\n\n{result["text"]}')


def get_audio_until_enter(filename="manual_recording.wav", samplerate=16000):
    duration = 60  # maximum length fallback
    print("Recording... Press Enter to stop.")
    # Start recording
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    # Wait for user to stop
    input()
    # Stop the recording
    sd.stop()
    # Save to .wav file
    write(filename, samplerate, recording)
    print(f"Recording saved to {filename}")


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
    # main()
    # get_audio_until_enter()
    recording_to_text()

