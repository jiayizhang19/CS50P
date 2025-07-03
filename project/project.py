
# import whisper
from faster_whisper import WhisperModel
import numpy as np
import pyaudio
import keyboard

def main():
    mode = input("Live Transcrption or Dialogue Transcription: ")
    if "dialogue" in mode.lower():
        audio = dialogue_transcript()
        print(transcript_audio(audio))
    else:
        real_time_transcript()

    
def real_time_transcript():
    """
 
    """
    audio, stream, chunk_size = initialize_audio_stream(chunk_size=2048)
    print("Recording ... Press Enter to stop")

    try:
        while not keyboard.is_pressed("enter"):
            # Each data is a small NumPy array
            raw_data = stream.read(num_frames=chunk_size, exception_on_overflow=False)
            audio_chunk = np.frombuffer(raw_data, dtype=np.int16)
            text = transcript_audio(audio_chunk, model_size="tiny")
            if text:
                print(f"> {text}", end="\r", flush=True)
    finally:
        clean_up_audio_stream(stream, audio)
        print("\nStopped")


def dialogue_transcript():
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
    return np.concatenate(frames)


def transcript_audio(audio, model_size="base"):
    """
    Convert audio to text with Whisper
    Arg:
        audio: audio data in 16-bit integer type, ranging from -32768 to 32727.
        Need to convert audio data from 16-bit int to 32-bit float ranging from -1.0 to 1.0, expected by most audio processing models.
        If the audio input is a recorded .wav, below line won't work, as the .wav file is a str type
    Returns:
        transcript
    """
    audio_float = audio.astype(np.float32) / 32768.0

    # ============================================================================== 
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> using whisper <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # model = whisper.load_model(model)
    # fp16 is not supported on CPU but GPU, usinng fp32 byb default on CPU
    # result = model.transcribe(audio, fp16=False)
    # return result["text"]
    # ==============================================================================
    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, _ = model.transcribe(audio_float, beam_size=5, language="en")
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
    main()
    
