import random


def generate_math_question(a: int, b: int) -> str:
    number1 = random.randint(a, b)
    number2 = random.randint(a, b)
    operators = ['+', '-', '*', '/']
    chosen_operator = random.choice(operators)
    return f'{number1} {chosen_operator} {number2}'


def check_answer(question: str, user_answer: str) -> bool:
    try:
        user_answer = float(user_answer)
        return user_answer == eval(question)
    except ValueError:
        return False


def math_quiz(number_of_questions: int = 5) -> None:
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        question = generate_math_question(1, 5)
        answer = input(question + ' = ')
        is_correct = check_answer(question, answer)
        if is_correct:
            correct_answers += 1

    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

    # if correct_answers / number_of_questions == 1:
    #     print("Великолепно! Вы получаете оценку S.")
    if correct_answers / number_of_questions >= 0.8:
        print("Отлично! Вы получаете оценку A.")
    elif correct_answers / number_of_questions >= 0.6:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")


math_quiz()