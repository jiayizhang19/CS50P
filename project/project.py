
# ===============================================
# implement live speech transciption with whisper
# ===============================================

import whisper
import numpy as np
import pyaudio
import keyboard

def main():
    ...
    

def record_until_keypress(sample_rate=16000, chunk_size=1024):
    """
    Record live audio in chunks until Enter key is pressed

    Args:
        sample_rate: audio sample rate (default 16000)
        chunk_size: audio frames per buffer 
    
    Returns:
        Numpy array of recorded audio data
    """
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        input=True,
        rate=sample_rate,
        frames_per_buffer=chunk_size
    )
    ...


def real_time_transcription(audio):
    """
    
    """
    if len(audio) > 0:
        print("Transcription:")
        transcript_audio(audio)


def transcript_audio(audio):
    """
    Convert audio to text with Whisper
    
    Arg:
        audio: audio data in 16-bit integer type

    Returns:
        transcript
    """
    ...
    model = whisper.load_model("base")
    # To convert audio data from 16-bit int to 32-bit float, as whisper expects floating-point input 
    # If the audio input is a recorded .wav, below line won't work, as the .wav file is a str type
    audio = audio.astype(np.float32) / 32768.0
    # fp16 is not supported on CPU but GPU, usinng fp32 byb default on CPU
    result = model.transcribe(audio, fp16=False)
    print(result["text"])

real_time_transcription("manual_recording.wav")



# ===================================================
# implement recorded speech transciption with whisper
# =================================================== 

from scipy.io.wavfile import write
import sounddevice as sd

def recorded_speech_to_text(recording = "manual_recording.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(recording)
    print(f'>> {result["text"]}')
    with open("transcript.txt", "a") as f:
        f.write(f'\n\n{result["text"]}')


def save_audio_until_enter(filename="manual_recording.wav", samplerate=16000):
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



# =================================
# implement with speech_recognition
# =================================

import speech_recognition as sr

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
    ...

