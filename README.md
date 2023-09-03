![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=300&section=header&text=DreamLand%20Project&fontSize=90)

- Prompter days 프로젝트
- https://www.prompterday.com/main
- 프로젝트 기간 : 2023.08.21 ~ 2023.09.03

## 📋 목차
1. [서비스 소개](#-서비스-소개)
2. [주요 서비스 기능](#-주요-서비스-기능)
3. [파일 구조](#-파일-구조)
4. [팀원 및 역할](#-팀원-및-역할)
5. [기술 스택](#-기술-스택)
<br>

## 💡 서비스 소개
#### 1. 주제 선정 배경
- 아이들의 창의력과 상상력을 상호작용을 통해 발전해나갈 수 있는 서비스를 만들고자 함
- 아이들이 만들어낸 그림은 상상력이 풍부하나 이에 대해 어른들과 소통하고자 하면 공감에 한계가 있음
- 따라서, 아이들의
  - <b>상상 친구를 그려주고</b>
  - <b>상상 친구와 소통하고</b>
  - <b>아이의 그림이나 사진을 동화로 만드는</b> 창의력 발전 웹 서비스를 만들고자함.
#### 2. 기대효과
- 편의성 : 아이들 역시 복잡한 Prompt 없이 ChatGPT와 DALLE-2를 활용하여 창작을 할 수 있음.
- 언어 학습 : 상상 친구와 지속적인 대화를 통해 다양한 소통이 가능해짐.
- 상상력 자극 : 다양한 이미지와 사진을 통해 동화를 창작하고 나만의 친구를 그리면서 상상력이 풍부해짐
<br>

## ❗ 주요 서비스 기능
#### 1. 상상 친구 생성 서비스
- 어떤 친구를 그릴 것인지 간단한 정보 입력만으로 친구를 그릴 수 있음
- 추가적인 드로잉을 통해 친구를 꾸밀 수 있음
- 친구에 대한 정보와 나에 대한 정보를 입력함으로써 친구의 페르소나를 생성할 수 있음
- 친구와 Chatting을 통해 대화를 나눌 수 있음
#### 2. 동화 생성 서비스
- 자신의 그림이나 사진을 업로드하여 동화를 생성할 수 있음
- 업로드된 이미지 위에 추가적인 드로잉을 통해 꾸밀 수 있음
- (연속된 동화를 보여주는 웹페이지를 제작 예정)
<br>

## 📂 파일 구조
```
📁 Prompter_days
├── 📃 README.md
├── 📁 config               --- DreamLand Service 
│   ├── 📁 config           --- 사이트 관리
│   ├── 📁 dream            --- 메인 페이지
│   ├── 📁 setting_persona  --- 친구 생성 및 chatting 서비스
│   ├── 📁 static           
│   ├── 📁 story            --- 동화 생성
│   ├── 📁 templates    
│   └── 📃 manage.py 
├── requirements.txt         --- Window
```
<br>

## 🧑‍🤝‍🧑 팀원 및 역할
<table>
  <tbody>
    <tr>
      <td align="center">
        <a href="https://github.com/ttoro-lee">
          <img src="https://avatars.githubusercontent.com/u/80229922?v=4" width="100px;">  <br>
          <sub><b>이운문</b></sub>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/ayocado">
          <img src="https://avatars.githubusercontent.com/u/89889583?v=4" width="100px;">  <br>
          <sub><b>윤용완</b></sub>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/EunchanJeong">
          <img src="https://avatars.githubusercontent.com/u/89077219?v=4" width="100px;">  <br>
          <sub><b>정은찬</b></sub>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/waterbean0143">
          <img src="https://avatars.githubusercontent.com/u/102143428?v=4"><br>
          <sub><b>배수빈</b></sub>
        </a>
      </td>
    </tr>
    <tr>
      <td align="center">BE & Infra</td>
      <td align="center">FE, BE</td>
      <td align="center">BE</td>
      <td align="center">기획</td>
    </tr>
  </tbody>
</table>
<br>

## 💻 기술 스택
<table>
  <thead>
    <tr>
      <th align='center'>영역</th>
      <th align='center'>기술</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align='center'><strong>프론트엔드</strong></td>
      <td align='center'>
        <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">
        <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">
        <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white">
        <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">
      </td>
    </tr>
    <tr>
      <td align='center'><strong>백엔드</strong></td>
      <td align='center'>
        <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
        <img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
      </td>
    </tr>
    <tr>
      <td align='center'><strong>AI, API</strong></td>
      <td align='center'>
        <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
        <img src="https://img.shields.io/badge/openai-412991?style=for-the-badge&logo=openai&logoColor=white">
        <img src="https://img.shields.io/badge/google-4285F4?style=for-the-badge&logo=google&logoColor=white">
      </td>
    </tr>
    <tr>
      <td align='center'><strong>인프라</strong></td>
      <td align='center'>
        <img src="https://img.shields.io/badge/pythonanywhere-1D9FD7?style=for-the-badge&logo=pythonanywhere&logoColor=white"/>
      </td>
    </tr>
    <tr>
      <td align='center'><strong>UI/UX</strong></td>
      <td align='center'>
        <img src="https://img.shields.io/badge/figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white">
      </td>
    </tr>
    <tr>
      <td align='center'><strong>협업</strong></td>
      <td align='center'>
        <img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white">
        <img src="https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white">
        <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
      </td>
    </tr>
  </tbody>
</table>
