from gtts import gTTS
import os

def generate_tts_report(report_text):
    tts = gTTS(text=report_text, lang='hi')
    filename = "sentiment_report.mp3"
    tts.save(filename)
    return filename
