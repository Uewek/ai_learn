"""Задача 3. Вартість запиту до моделі.

Ціна задана за 1000 токенів (price_per_1k).
Вартість запиту = усі токени (prompt + completion), поділені на 1000,
помножені на ціну.

Поверни число з плаваючою крапкою, округлене до 4 знаків після крапки.

Запуск: .venv/bin/python Lessons/November/0111/03_estimate_cost.py
"""


def estimate_cost(
    prompt_tokens: int, completion_tokens: int, price_per_1k: float
) -> float:
    return  round(((prompt_tokens + completion_tokens)/1000)*price_per_1k,4)


assert estimate_cost(1000, 500, 0.002) == 0.003
assert estimate_cost(250, 250, 0.01) == 0.005
assert estimate_cost(0, 0, 0.5) == 0.0
assert estimate_cost(1000000, 234567, 0.002) == 2.4691

print("OK: all checks passed")
