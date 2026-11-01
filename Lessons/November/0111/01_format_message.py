"""Задача 1. Рядок повідомлення чату.

Напиши функцію, яка готує повідомлення до показу в терміналі у форматі:
    [role] text

Вимоги:
- role: прибрати пробіли по краях і перевести в нижній регістр;
- text: прибрати пробіли по краях, регістр не змінювати;
- функція повертає рядок через return і нічого не друкує.

Запуск: .venv/bin/python Lessons/November/0111/01_format_message.py
"""


def format_message(role: str, text: str) -> str:
    # raise NotImplementedError
    result = '['+ role.strip().lower() +']' + ' ' + text.strip()
    return result


assert format_message("user", "hello") == "[user] hello"
assert format_message(" USER ", "  Hello there  ") == "[user] Hello there"
assert format_message("Assistant", "What is a token?") == "[assistant] What is a token?"

print("OK: all checks passed")
