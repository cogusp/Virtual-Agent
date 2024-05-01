from gtts import gTTS
from playsound import playsound

file_name = 'sample.mp3'    # file name

# English
#text = 'Can I help you?'    # text
#tts_en = gTTS(text=text, lang='en') # create a .mp3
#tts_en.save(file_name)  # save the .mp3
#playsound(file_name)    # play the .mp3 file

#Korean
#text = '오늘의 요리는 비빔밥입니다.'
#tts_ko = gTTS(text=text, lang='ko')
#tts_ko.save(file_name)
#playsound(file_name)

#long sentence (read the text from file)
with open('sample.txt', 'r', encoding='utf8') as f:
    text = f.read()

tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name)