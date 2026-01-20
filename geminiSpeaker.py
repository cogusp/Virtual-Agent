import time, os
import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS
from playsound import playsound
#from pydub import AudioSegment
from dotenv import load_dotenv
from queue import Queue

# -----------------------
# 초기 설정
# -----------------------
load_dotenv()

# 환경 변수에(.env)에 저장된 API 키 불러오기
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables!!")

genai.configure(api_key = API_KEY)
model = genai.GenerativeModel('gemini-pro')    # Gemini-pro로 모델 설정
chat = model.start_chat(history=[])

# 음성 인식(마이크 및 녹음) 초기화
r = sr.Recognizer()
m = sr.Microphone()

# 오디오 처리 큐 (동시성 문제 방지용)
audio_queue = Queue()

# -----------------------
# AI 음성 출력을 위한 함수
# -----------------------
def speak(text):
    if not text:
        return
        
    print(f"[AI] {text}")
    file_name = f"voice_{int(time.time())}.mp3"    # 음성 파일명 설정
    tts = gTTS(text=text, lang='ko')               # TTS 변환 과정
    tts.save(file_name)                            # 음성 파일 저장
    try:
        playsound(file_name)                       # 음성 파일 재생
    finally:
        # Auto remove the voice.mp3 file
        if os.path.exists(file_name):
            os.remove(file_name)

    # Create audio to fast
    #audio_seg = AudioSegment.from_file(file_name)
    #audio_fast = audio_seg.speedup(playback_speed = 2.0)
    #audio_fast.export(file_name, format="mp3")

# -----------------------
# AI의 응답을 처리하는 함수
# -----------------------
def get_ai_response(prompt: str) -> str:        # 문자열 prompt가 들어오며 반환형은 문자열
    """" GEMINI API로부터 응답을 받아옵니다. """
    try:
        response = chat.send_message(prompt)    # 질문 전송 및 응답 저장
        return response.text.strip()            # 공백 제거 후 반
    except Exception as e:
        print(f"GEMINI API Error: {e}")
        return "죄송합니다. 현재 답변을 가져오지 못했습니다."

# -----------------------
# 사용자 음성에 따라 작업을 결정하는 함수
# -----------------------
def handle_user_input(text: str):
    if not text:
        speak("다시 한 번 말씀해주시겠어요?")
        return

    if '종료' in text:
        speak("다음에 또 만나요!")
        os._exit(0)
        
    answer = get_ai_response(text)
    speak(answer)

# -----------------------
# 사용자 음성을 텍스트로 바꾸는 함수
# -----------------------
def listen_callback(recognizer, audio):
    """ 백그라운드에서 마이크 입력을 계속 듣는 콜백 """
    try:
        text = recognizer.recognize_google(audio, language='ko')    # 사용자 음성을 한국어 텍스트로 변경
        print(f"[사용자] {text}")
        audio_queue.put(text)                                       # 사용자 음성 텍스트를 큐에 저장
    except sr.UnknownValueError:       # failed
        print("인식 실패")  
    except sr.RequestError as e:
        print(f"Google Speech API Error: {e}")  # API key Error (ex. Network)

# -----------------------
# 메인 루프 (비동기 음성 인식)
# -----------------------
def main():
    speak('무엇을 도와드릴까요?')
    # keep listening in background
    stop_listening = r.listen_in_background(m, listen)

    # Loop
    while True:
        try:
            if not audio_queue.empty():            # 사용자가 말한 경우
                user_input = audio_queue.get()     # 큐에서 텍스트를 꺼내
                handle_user_input(user_input)      # 작업을 결정하는 함수 호출
            time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n종료 요청 감지")
            stop_listening(wait_for_stop=False)
            break;
        except Exception as e:
            print(f"Main Loop Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()
