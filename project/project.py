from faster_whisper import WhisperModel
from googletrans import Translator
from datetime import timedelta
import asyncio
import sys


model = WhisperModel("base", device="cpu", compute_type="int8")
translator = Translator()

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments.")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments.")
    bilingual = input("Do you want a bilingual transcription in both English and Chinese? (y/n): ")
    text = extract_text_from_speech(sys.argv[1])
    if "y" in bilingual.lower():
        asyncio.run(save_to_txt(text, True))
    else:
        asyncio.run(save_to_txt(text))


def extract_text_from_speech(audio):
    segments, _ = model.transcribe(
        audio,
        beam_size=5 # larger number leads to higher accurancy
    )
    full_text = []
    for segment in segments:
        start = format_timestamp(int(segment.start))
        text = start + " " + segment.text
        full_text.append(text)
    return full_text


async def save_to_txt(text, translation=False):
    with open("transcription.txt", "w", encoding="utf-8") as f:
        if translation:
            for t in text:
                f.write(f"{t}\n")
                ch = await translate_text(t[5:])
                f.write(f"{ch}\n")
        else:
            for t in text:
                f.write(f"{t}\n")
    print("Saved to transcription.txt")


async def translate_text(text, src="en", dest="zh-CN"):
    result = await translator.translate(text, src=src, dest=dest)
    return result.text


def format_timestamp(sec):
    """
    Format timestamp to minutes and seconds (MM:SS)
    Arg: second in integer, e.g. 65s
    Return: timestamp in 00:00, e.g. 01:05
    """
    tm = str(timedelta(seconds=sec)).split(".")[0]
    tm = tm[2:]
    return tm
    

if __name__ == "__main__":
    # audio = "03_Whats_for_Dinner.mp4"
    main()
    # text = extract_text_from_speech(audio)
    # asyncio.run(save_to_txt(text))
    # print(asyncio.run(translate_text("How are you", src="en", dest="zh-CN")))
    # print(format_timestamp(6.84))

    
