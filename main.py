import pytesseract
from gtts import gTTS

def image_to_speech(image1):
    text = pytesseract.image_to_string(image1)
    # Convert the text to speech.
    tts = gTTS(text=text, lang='en')
    audio_data = tts.get_audio()
    return audio_data



image_path = 'image1.jpg'
audio_data = image_to_speech(image_path)

# Save the audio data to a file.
with open('speech.mp3', 'wb') as f:
  f.write(audio_data)

# Play the audio file.
import winsound
winsound.PlaySound('speech.mp3', winsound.SND_FILENAME)
