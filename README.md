# 🧮 수학 퀴즈 게임 (Math Quiz Game)

## 1. 프로젝트 개요
파이썬(Python)을 활용하여 콘솔 환경에서 동작하는 퀴즈 게임입니다. 객체지향 프로그래밍(OOP)을 적용하여 클래스를 분리하였으며, 파일 입출력을 통해 데이터를 영구적으로 보관합니다.

## 2. 퀴즈 주제와 선정 이유
* **주제:** 기초 수학 문제
* **선정 이유:** 일상생활에서 자주 쓰이는 사칙연산, 도형의 기본 성질, 소수 개념 등을 퀴즈를 통해 재미있게 복습하고 두뇌를 단련하기 위해 선정했습니다.

## 3. 실행 방법
1. Python 3.x 버전이 설치되어 있어야 합니다.
2. 터미널(또는 명령 프롬프트)에서 프로젝트 폴더로 이동합니다.
3. 아래 명령어를 입력하여 게임을 실행합니다.
   ```bash
   python main.py

   하이하이하이요

## - git log 또는 커밋 스크린샷

<img width="752" height="220" alt="스크린샷 2026-08-05 오후 5 42 10" src="https://github.com/user-attachments/assets/0df22ff4-88bf-4475-bfa2-e9e2614efa0c" />


## - git log와 merge 기록 스크린샷

<img width="1036" height="281" alt="스크린샷 2026-08-05 오후 5 56 20" src="https://github.com/user-attachments/assets/f7cdb330-5508-49f3-bb87-39e96b356779" />

## - README에 clone/pull 절차 및 결과 스크린샷

* **clone**
<img width="809" height="215" alt="a1" src="https://github.com/user-attachments/assets/16682595-8aeb-408d-9915-0b6b6c39b140" />

* **pull**
<img width="810" height="110" alt="a2" src="https://github.com/user-attachments/assets/ebc47fca-6476-46ae-875d-c69d22bf7ca2" />

## 🎮 클래스 역할 설명 (책임 분리)
이 게임은 코드를 깔끔하게 관리하기 위해 두 개의 클래스로 역할을 나누어(책임 분리) 만들었습니다.

- **`Quiz` 클래스 (문제 담당)**
  - 역할: 수학 문제 1개를 만드는 역할만 집중해서 맡습니다.
  - 기능: 랜덤으로 숫자를 뽑아 문제를 만들고, 진짜 정답을 계산하며, 플레이어가 쓴 답이 맞는지 틀렸는지 검사합니다.

- **`QuizGame` 클래스 (게임 진행 담당)**
  - 역할: 게임의 전체적인 흐름과 점수를 관리하는 매니저 역할을 합니다.
  - 기능: `Quiz` 클래스에게 "문제 하나 줘!"라고 부탁해서 화면에 보여주고, 플레이어의 점수를 기록하며, 게임 시작과 종료를 관리합니다.
