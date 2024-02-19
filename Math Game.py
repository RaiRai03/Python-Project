import random

def generate_expression():
    operands = []
    operators = []
    operations = ['+', '-', '*', '/']
    expression = []
    operands_count = 0
    operators_count = 0
    for i in range(0, 3):
        operands.append(random.randint(0, 20))
    for i in range(0, 2):
        operators.append((random.choice(operations)))
    for i in range(0, len(operators) + len(operands)):
        if i % 2 == 0:
            expression.append(operands[operands_count])
            operands_count += 1
        else:
            expression.append(operators[operators_count])
            operators_count += 1
    expression = ''.join(str(x) for x in expression)
    return expression

def result(expression):
    return (int(eval(expression)))

def main():
    print("Welcome to the maths game !!!")
    print("Test your basic arithematic skills by playing this simple game.")
    print("With every 5 correct answers, the level increase, increasing the difficulty of the questions.")
    print("Remember : 1. Write only the integral part of the answer 2. Operator precedence applies 3. You have 3 lives.")
    score = 0
    level = 1
    lives = 3
    while lives != 0:
        print("LEVEL : ", level)
        question_expression = generate_expression()
        print(question_expression, end='')
        correct_answer = 0
        try:
            correct_answer = result(question_expression)
        except:
            print("OOPS ! I messed up ! Lets do it again !")
            continue
        answer = int(input(" = "))
        if correct_answer == answer:
            print("CORRECT ! ")
            score = score + 1
            if score != 0 and score % 5 == 0:
                level = level + 1
            print("SCORE = ", score, "LIVES = ", lives)
        else:
            print("WRONG ! ")
            lives = lives - 1
            print("SCORE = ", score, "LIVES = ", lives)
    print("GAME OVER !!!")
    print("Maximum Level = ", level, "SCORE = ", score)

main()