<!-- Title -->
  <div align='center'>
    <h1>AI Professor Prototype</h1>
  </div>

  <br>

  <!-- Introduce -->
  <h4> 👾 2D 모니터 환경에서 사용하기 위해 Gemini API와 Meta Human을 연동하여 제작된 AI 교수 프로그램 프로토타입입니다. </h4>
  <h4> 🛠️ 3인 개발</h4>
  <h4> 👩‍🔧 역할: Python으로 Gemini API가 연동된 AI 스피커 제작 </h4>
  <h4> 📆 2025.01~2025.02 (1개월)</h4>
  
  <!-- Link -->
  <h4> 🔗 https://drive.google.com/drive/folders/1EgbDVwatFQKg3a7Dz0egHLqMvwImLZQ- </h4>
  <h4> 📽️ https://youtu.be/YjeXpHNuxLM </h4>

  <br><br>

  <!-- Tools -->
  <h2> Engine </h2>
  <h4> 👾 Unreal Engine 5.4 </h4>

  <h2> Tool </h2>
  <h4> 🛠️ Gemini API </h4>
  <h4> 🛠️ Python </h4>
  <h4> 🛠️ Meta Human </h4>

  <br>
  
  <h2> Flow </h2>
  Python으로 Gemini API와 연동된 AI 스피커를 제작했습니다.<br>
  사용자의 질문은 Unreal Engine에서 녹음 및 저장했습니다.<br>
  Python에서 이를 STT(Speech to Text) 과정을 통해 Gemini에게 전송하고, 답변은 TTS(Text to Speech) 과정을 통해 음성 파일로 저장됩니다.<br>
  Local에 저장된 음성 파일은 Unreal Engine에서 재생했으며, 립싱크를 구현했습니다.<br>
<h4>
- speak(text)<br>
AI의 응답을 음성 파일로 생성하고, 재생한 뒤에 삭제하는 함수입니다.
</h4>
<h4>
- get_ai_response(prompt)<br>
사용자의 질문을 Gemini AI에게 전송하고 응답을 문자열로 받아오는 함수입니다.
</h4>
<h4>
- handle_user_input(text)<br>
사용자의 요청에 따라 무엇을 할지(질문, 종료) 결정하는 함수입니다.
</h4>
<h4>
- listen_callback(recognizer, audio)<br>
사용자의 음성을 한국어 텍스트로 변환하고,  audio_queue에 저장하는 함수입니다.
</h4>
<h4>
- main()<br>
마이크를 계속 켜 두고 사용자가 말하면 audio_queue에서 텍스트를 꺼내 처리하는 함수입니다.<br>
</h4>

<h2> TroubleShooting </h2>

<h4>
- 문제 배경<br>
1. 사용자 음성 인식 중에는 다음 코드가 진행되지 않는 문제가 발생했습니다.<br>
2. AI의 응답이 중간에 끊기는 문제가 발생했습니다.
</h4>
<h4>
- 해결 방법<br>
1. 프로그램을 멈추지 않고 계속 듣는 비동기 방식을 사용했습니다. 백그라운드에서 마이크가 음성을 계속 듣고, 음성이 들어오면 자동으로 콜백 함수를 실행했습니다.<br>
2. Queue를 사용하여 입력을 차례대로 처리했습니다. 음성 인식 스레드에서는 put만, 메인 루프에서는 get만 수행하도록 수정했습니다.
</h4>

<h2> Result </h2>

<img width="445" height="283" alt="image" src="https://github.com/user-attachments/assets/2073f131-adcc-48c0-8d4d-4921d92727f6" />
