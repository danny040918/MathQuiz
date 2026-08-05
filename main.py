import json
import os
import sys

# --- [요구사항 4] Quiz 클래스 ---
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer  # 1~4 사이의 정수

    def display(self):
        print(f"\n문제: {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    def check_answer(self, user_answer):
        return self.answer == user_answer

# --- [요구사항 3] 공통 입력/예외 처리 함수 ---
def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        user_input = input(prompt).strip() # 공백 제거
        
        if not user_input: # 빈 입력 처리
            print("⚠️ 입력값이 없습니다. 다시 입력해주세요.")
            continue
            
        try:
            value = int(user_input)
            if min_val is not None and max_val is not None:
                if not (min_val <= value <= max_val):
                    print(f"⚠️ {min_val}에서 {max_val} 사이의 숫자를 입력해주세요.")
                    continue
            return value
        except ValueError: # 숫자 변환 실패 처리
            print("⚠️ 숫자로만 입력해주세요.")

# --- [요구사항 10] QuizGame 클래스 ---
class QuizGame:
    def __init__(self):
        self.file_name = "state.json"
        self.quizzes = []
        self.best_score = 0
        self.load_data()

    # --- [요구사항 11] 파일 불러오기 및 예외 처리 ---
    def load_data(self):
        if not os.path.exists(self.file_name):
            print("데이터 파일이 없습니다. 기본 수학 퀴즈를 불러옵니다.")
            self.quizzes = self.get_default_quizzes()
            return

        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                for q in data.get("quizzes", []):
                    self.quizzes.append(Quiz(q["question"], q["choices"], q["answer"]))
        except (json.JSONDecodeError, Exception):
            print("⚠️ 데이터 파일이 손상되었습니다. 기본 수학 퀴즈로 초기화합니다.")
            self.quizzes = self.get_default_quizzes()
            self.best_score = 0

    def save_data(self):
        data = {
            "best_score": self.best_score,
            "quizzes": [{"question": q.question, "choices": q.choices, "answer": q.answer} for q in self.quizzes]
        }
        try:
            with open(self.file_name, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"⚠️ 파일 저장 중 오류가 발생했습니다: {e}")

    # --- [요구사항 5] 기본 퀴즈 데이터 (수학 문제) ---
    def get_default_quizzes(self):
        return [
            Quiz("15 + 27 의 값은?", ["32", "42", "52", "62"], 2),
            Quiz("8 곱하기 7 은?", ["48", "54", "56", "64"], 3),
            Quiz("삼각형의 세 내각의 합은 몇 도일까요?", ["90도", "180도", "270도", "360도"], 2),
            Quiz("100의 양의 제곱근(루트 100)은?", ["5", "10", "50", "10000"], 2),
            Quiz("다음 중 소수(Prime number)가 아닌 숫자는?", ["2", "7", "9", "11"], 3)
        ]

    # --- [요구사항 6] 퀴즈 풀기 ---
    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해주세요.")
            return

        score = 0
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"\n--- [{i}/{len(self.quizzes)}] ---")
            quiz.display()
            user_ans = get_int_input("정답 번호를 입력하세요 (1~4): ", 1, 4)
            
            if quiz.check_answer(user_ans):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번 입니다.")

        print(f"\n결과: 총 {len(self.quizzes)}문제 중 {score}문제를 맞췄습니다!")
        
        if score > self.best_score:
            print("🎉 최고 점수 갱신!")
            self.best_score = score
        
        self.save_data()

    # --- [요구사항 7] 퀴즈 추가 ---
    def add_quiz(self):
        print("\n--- 새 퀴즈 추가 ---")
        question = input("문제를 입력하세요: ").strip()
        if not question:
            print("⚠️ 문제가 비어있습니다. 취소합니다.")
            return

        choices = []
        for i in range(1, 5):
            choice = input(f"{i}번 선택지: ").strip()
            if not choice:
                choice = f"선택지 {i}" # 빈 입력시 기본값
            choices.append(choice)

        answer = get_int_input("정답 번호를 입력하세요 (1~4): ", 1, 4)
        
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_data()
        print("✅ 퀴즈가 성공적으로 추가되었습니다!")

    # --- [요구사항 8] 퀴즈 목록 ---
    def show_list(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return
        
        print("\n--- 퀴즈 목록 ---")
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"{i}. {quiz.question}")

    # --- [요구사항 9] 점수 확인 ---
    def show_score(self):
        print(f"\n🏆 현재 최고 점수: {self.best_score}점")

    # --- [요구사항 2] 메뉴 기능 ---
    def run(self):
        while True:
            print("\n" + "="*30)
            print(" 🧮 수학 퀴즈 게임 🧮 ")
            print("="*30)
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록 확인")
            print("4. 최고 점수 확인")
            print("5. 종료")
            print("="*30)
            
            choice = get_int_input("메뉴를 선택하세요 (1~5): ", 1, 5)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_list()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                print("게임을 종료합니다. 안녕히 가세요!")
                self.save_data()
                break

if __name__ == "__main__":
    game = QuizGame()
    try:
        game.run()
    # --- [요구사항 3] 비정상 종료 방지 (Ctrl+C, EOF) ---
    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 프로그램이 강제 종료되었습니다. 데이터를 안전하게 저장합니다.")
        game.save_data()
        sys.exit(0)# 기본 퀴즈 데이터 추가 완료
# 메뉴 기능 추가 완료
