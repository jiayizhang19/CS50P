
# import whisper
from faster_whisper import WhisperModel
import numpy as np
import pyaudio
import keyboard
from scipy.io import wavfile

def main():
    mode = input("Live Transcrption, Dialogue Transcription or Recording Transcription: ")
    if "dialogue" in mode.lower():
        dialogue_transcipt()
    elif "live" in mode.lower():
        live_transcript()

    
def live_transcript():
    """
    chunk_size: the number of samples
    sample_rate: the number of samples per second
    chunk_size / sample_rate = xx seconds, e.g. 2048 / 16000 = 0.128s
    """
    audio, stream, chunk_size = initialize_audio_stream(chunk_size=2048)
    audio_buffer = np.array([], dtype=np.int16)
    min_sample = 16000 * 2  # Buffer 2 seconds of audio
    print("Recording ... Press Enter to stop")
    print("> ", end="")
    try:
        while not keyboard.is_pressed("enter"):
            # Each data is a small NumPy array
            raw_data = stream.read(num_frames=chunk_size, exception_on_overflow=False)
            audio_chunk = np.frombuffer(raw_data, dtype=np.int16)
            audio_buffer = np.concatenate((audio_buffer, audio_chunk))
            # print(f"audio_buffer is {audio_buffer}")
            if len(audio_buffer) >= min_sample:
                text = transcript_audio(audio_buffer)
                audio_buffer = np.array([], dtype=np.int16)
                if text:
                    print(f"{text}", end=" ", flush=True)
    finally:
        clean_up_audio_stream(stream, audio)
        print("\n> End...")


def dialogue_transcipt():
    """
    Records audio in chunks until Enter key is pressed.
    Returns Numpy array of recorded audio data.
    """
    audio, stream, chunk_size = initialize_audio_stream()
    frames = []
    print("Recording ... Press Enter to stop")
    while not keyboard.is_pressed("enter"):
        # Each data is a small NumPy array
        data = stream.read(num_frames=chunk_size, exception_on_overflow=False)
        frames.append(np.frombuffer(data, dtype=np.int16))
    
    clean_up_audio_stream(stream=stream, audio=audio)
    # combine each small array to one long array for whisper
    audio_data = np.concatenate(frames)
    return transcript_audio(audio_data)


def wav_recording_transcript(file):
    """
    Load .wav file and convert to numpy array
    """
    _, audio_data = wavfile.read(file)
    if len(audio_data.shape) > 1:
        audio_data = audio_data.mean(axis=1)
    return transcript_audio(audio_data)


def transcript_audio(audio_data, model_size="base"):
    """
    Convert audio to text with Whisper
    Arg:
        audio_data: audio data in 16-bit integer type in numpy array, ranging from -32768 to 32727.
        Need to convert audio data from 16-bit int to 32-bit float ranging from -1.0 to 1.0, expected by most audio processing models.
        If the audio input is a recorded .wav, below line won't work, as the .wav file is a str type
    Returns:
        transcript
    """
    audio_float = audio_data.astype(np.float32) / 32768.0
    # =================================================================================== 
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> using whisper <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # model = whisper.load_model(model)
    # result = model.transcribe(audio_float, fp16=False) # fp16 is not supported on CPU but GPU, usinng fp32 byb default on CPU
    # return result["text"]
    # ===================================================================================
    model = WhisperModel(
        model_size, 
        device="cpu", 
        compute_type="int8"
        )
    segments, _ = model.transcribe(
        audio_float, 
        beam_size=3,
        vad_filter=True, # aviod wasting whisper's time and CPU on silence
        language="en"
        )
    return " ".join(segment.text for segment in segments)
    

def initialize_audio_stream(sample_rate=16000, chunk_size=1024):
    """
    Args:
        sample_rate: audio sample rate (default 16000)
        chunk_size: audio frames per buffer 
    """
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        input=True,
        rate=sample_rate,
        frames_per_buffer=chunk_size
    )
    return audio, stream, chunk_size


def clean_up_audio_stream(stream, audio):
    """
    Clean up stream and audio to release resources
    """
    stream.stop_stream()
    stream.close()
    audio.terminate()


if __name__ == "__main__":
    # main()
    # print(wav_recording_transcript("manual_recording.wav"))
    # print(dialogue_transcipt())
    live_transcript()
    
