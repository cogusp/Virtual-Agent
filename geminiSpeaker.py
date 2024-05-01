import time, os
import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
from playsound import playsound
#from pydub import AudioSegment
from dotenv import load_dotenv

# Voice
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[사용자] ' + text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패')  # failed
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e))  # API key Error (ex. Network)

# Answer
def answer(input_text):
    answer_text = ''

    if '종료' in input_text:
        answer_text = '다음에 또 만나요'
        stop_listening(wait_for_stop=False) # stop the listening
    elif input_text == '':
        answer_text = '다시 한 번 말씀해주시겠어요?'
    else:
        response = chat.send_message(input_text)
        answer_text = response.text

    speak(answer_text)

# Speak (TTS)
def speak(text):
    print('[인공지능] ' + text)
    file_name = f"voice_{int(time.time())}.mp3"
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)

    # Create audio to fast
    #audio_seg = AudioSegment.from_file(file_name)
    #audio_fast = audio_seg.speedup(playback_speed = 2.0)
    #audio_fast.export(file_name, format="mp3")

    playsound(file_name)

    #time.sleep(5)
    
    # Remove the voice.mp3 file
    if os.path.exists(file_name):
        os.remove(file_name)

load_dotenv()

API_KEY = 'AIzaSyDTI8yu2bU2WDSK1MlqXlLN5WBPuIUTV3A'

genai.configure(
    api_key = API_KEY
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
# keep listening in background
stop_listening = r.listen_in_background(m, listen)

# Loop
while True:
    time.sleep(0.1)