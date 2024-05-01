import speech_recognition as sr

# listen to voice from mic
r = sr.Recognizer()
with sr.Microphone() as source:
    print('듣고 있어요')
    audio = r.listen(source)

# read the voice form file (wav, aiff, aiff-c, flac: O / mp3: X)
#r = sr.Recognizer()
#with sr.AudioFile('smaple.wav') as source:
#    audio = r.record(source)

try:
    # google API (50 per day)
    # English
    #text = r.recognize_google(audio, language='en-US')
    #print(text)

    # Korean
    text = r.recognize_google(audio, language='ko')
    print(text)

except sr.UnknownValueError:
    print('인식 실패')  # failed
except sr.RequestError as e:
    print('요청 실패 : {0}'.format(e))  # API key Error (ex. Network)