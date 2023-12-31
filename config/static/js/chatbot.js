// 채팅 메시지를 표시할 DOM
const chatMessages = document.querySelector("#chat-messages");
// 사용자 입력 필드
const userInput = document.querySelector("#user-input input");
// 전송 버튼
const sendButton = document.querySelector("#user-input button");

// 발급받은 OpenAI API 키를 변수로 저장
let apiKey;

document.addEventListener("DOMContentLoaded", () => {
  fetch("/setting_persona/get_sensitive_data/") // 서버의 API 엔드포인트로 요청 보내기
    .then((response) => response.json()) // JSON 응답 파싱
    .then((data) => {
      // 받아온 데이터에서 api_key 값을 변수에 저장
      apiKey = data.api_key;

      // apiKey 값을 페이지의 특정 요소에 표시
    })
    .catch((error) => {
      console.error("Error fetching API key:", error);
    });
});
// const secrets = require('../../secrets.json');
// const apiKey = secrets.OPENAI_KEY;
// OpenAI API 엔드포인트 주소를 변수로 저장
const apiEndpoint = "https://api.openai.com/v1/chat/completions";
function addMessage(sender, message) {
  // 새로운 div 생성
  const messageElement = document.createElement("div");
  // 생성된 요소에 클래스 추가
  if (sender == "나") {
    messageElement.className = "bs-toast toast my-message show bg-success";
    // 채팅 메시지 목록에 새로운 메시지 추가
    messageElement.textContent = `${sender}: ${message}`;
    chatMessages.prepend(messageElement);
  } else {
    messageElement.className = "bs-toast toast ai-message show bg-primary";
    // 채팅 메시지 목록에 새로운 메시지 추가
    const otherImage = document.getElementById("ai_chat"); // 예시: ID를 사용한 선택

    if (otherImage) {
      // 이미지 엘리먼트가 존재하는 경우
      const otherImageUrl = otherImage.src; // 이미지 엘리먼트의 src 속성 값을 가져옵니다.

      const imageElement = document.createElement("img");
      imageElement.src = otherImageUrl; // 이미지 데이터 URL 설정
      imageElement.alt = "프로필 이미지";
      imageElement.className = "profile-image";
      imageElement.id = "ai_chat";
      messageElement.appendChild(imageElement);
      const textElement = document.createElement("span");
      textElement.textContent = `${sender}: ${message}`;
      messageElement.appendChild(textElement);
      chatMessages.prepend(messageElement);
    } else {
      console.log("이미지를 찾을 수 없습니다.");
      const imageElement = document.createElement("img");
      imageElement.src = null; // 이미지 데이터 URL 설정
      imageElement.alt = "프로필 이미지";
      imageElement.className = "profile-image";
      imageElement.id = "ai_chat";
      messageElement.appendChild(imageElement);
      const textElement = document.createElement("span");
      textElement.textContent = `${sender}: ${message}`;
      messageElement.appendChild(textElement);
      chatMessages.prepend(messageElement);
    }
  }
}
// ChatGPT API 요청
async function fetchAIResponse(prompt) {
  const name = document.getElementById("name").textContent;
  const age = document.getElementById("age").textContent;
  const gender = document.getElementById("gender").textContent;
  const likes = document.getElementById("likes").textContent;
  const dislikes = document.getElementById("dislikes").textContent;
  console.log(name, age, gender, likes, dislikes);

  const user_name = document.getElementById("user_name").textContent;
  const user_age = document.getElementById("user_age").textContent;
  const user_gender = document.getElementById("user_gender").textContent;
  console.log(user_name, user_age, user_gender);

  // API 요청에 사용할 옵션을 정의
  const requestOptions = {
    method: "POST",
    // API 요청의 헤더를 설정
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify({
      model: "gpt-4", // 사용할 AI 모델
      messages: [
        {
          role: "system", // 메시지 역할을 system로 설정
          content:
            "I want you to act as my friend. I will tell you what is happening in my life and you will reply with something helpful and supportive." +
            " Do not write long explanations, just reply with the bright, cheerful words. Please help me stay positive and bright. You are child. " +
            " Your name is " +
            name +
            ". Your age is " +
            age +
            ". Your gender is " +
            gender +
            ". You like " +
            likes +
            ". you dislike " +
            dislikes +
            ". My name is " +
            user_name +
            ". My age is " +
            user_age +
            ". My gender is " +
            user_gender +
            ". I am child.", // 사용자가 입력한 메시지
          // content:
          //   "Answer kindly and simply, as if you were talking to a child, user name is not" +
          //   name +
          //   "and " +
          //   age +
          //   " " +
          //   gender +
          //   " " +
          //   likes +
          //   " " +
          //   dislikes, // 사용자가 입력한 메시지
        },
        {
          role: "user",
          content: prompt,
        },
        {
          role: "system", // 메시지 역할을 system로 설정
          content:
          "I am a child counselor. When I receive a question from you, I will explain about myself as if I'm talking to a child." +
            " Do not write long explanations, just reply with the bright, cheerful words. Please help me stay positive and bright. You are child. "
        },
        {
          role: "user",
          content: prompt,
        },
      ],
      temperature: 0.8, // 모델의 출력 다양성
      max_tokens: 1024, // 응답받을 메시지 최대 토큰(단어) 수 설정
      top_p: 1, // 토큰 샘플링 확률을 설정
      frequency_penalty: 0.5, // 일반적으로 나오지 않는 단어를 억제하는 정도
      presence_penalty: 0.5, // 동일한 단어나 구문이 반복되는 것을 억제하는 정도
      stop: ["Human"], // 생성된 텍스트에서 종료 구문을 설정
    }),
  };
  // API 요청후 응답 처리
  try {
    const response = await fetch(apiEndpoint, requestOptions);
    const data = await response.json();
    const aiResponse = data.choices[0].message.content;
    return aiResponse;
  } catch (error) {
    console.error("OpenAI API 호출 중 오류 발생:", error);
    return "OpenAI API 호출 중 오류 발생";
  }
}
// 전송 버튼 클릭 이벤트 처리
sendButton.addEventListener("click", async () => {
  // 사용자가 입력한 메시지
  const message = userInput.value.trim();
  // 메시지가 비어있으면 리턴
  if (message.length === 0) return;
  // 사용자 메시지 화면에 추가
  addMessage("나", message);
  userInput.value = "";
  //ChatGPT API 요청후 답변을 화면에 추가
  const aiResponse = await fetchAIResponse(message);
  const name = document.getElementById("name").textContent;
  console.log(name);
  addMessage(name, aiResponse);
});
// 사용자 입력 필드에서 Enter 키 이벤트를 처리
userInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    sendButton.click();
  }
});
