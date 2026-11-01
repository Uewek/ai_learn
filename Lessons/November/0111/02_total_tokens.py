"""Задача 2. Сума токенів із введення користувача.

Значення токенів приходять рядками, як результат input().
Напиши функцію, яка повертає їхню суму як ціле число.

Перш ніж писати код, подумай: що поверне "120" + "30"?

Запуск: .venv/bin/python Lessons/November/0111/02_total_tokens.py
"""


def total_tokens(prompt_tokens: str, completion_tokens: str) -> int:
    return int(prompt_tokens) + int(completion_tokens)


assert total_tokens("120", "30") == 150
assert total_tokens(" 7 ", "8") == 15
assert total_tokens("0", "0") == 0

print("OK: all checks passed")
