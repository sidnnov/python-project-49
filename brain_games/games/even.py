from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 100
RULES_OF_THE_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2


def get_task_and_answer():
    number = randint(MIN_NUMBER, MAX_NUMBER)
    result = is_even(number)
    correct_answer = ['yes', 'no'][result]
    task = str(number)

    return task, correct_answer
