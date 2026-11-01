"""Задача 4. Рядок статистики запиту.

Поверни рядок у форматі:
    <model>: <tokens> tokens, $<cost>

Вимоги:
- tokens: сума prompt і completion, тисячі розділені комою (1,234,567);
- cost: вартість за формулою із задачі 3, завжди рівно 4 знаки після крапки ($0.0150);
- логіку обчислення винеси в окрему власну функцію, а не пиши все в одному виразі.

Форматування чисел шукай у лекції 0 CS50P, у частині про f-рядки.

Запуск: .venv/bin/python Lessons/November/0111/04_format_usage.py
"""

def estimate_cost(
    prompt_tokens: int, completion_tokens: int, price_per_1k: float
) -> float:
    return  round(((prompt_tokens + completion_tokens)/1000)*price_per_1k,4)

def format_usage(
    model: str, prompt_tokens: int, completion_tokens: int, price_per_1k: float
) -> str:
    # raise NotImplementedError
    # "qwen: 150 tokens, $0.0003"
    float_cost = estimate_cost(prompt_tokens, completion_tokens, price_per_1k)
    string_tokens = str(prompt_tokens+completion_tokens)
    result = f"{model}: {prompt_tokens+completion_tokens:,} tokens, ${float_cost:.4f}"
    return result


assert format_usage("qwen", 120, 30, 0.002) == "qwen: 150 tokens, $0.0003"
assert format_usage("llama", 1000, 500, 0.01) == "llama: 1,500 tokens, $0.0150"
assert format_usage("qwen", 1000000, 234567, 0.002) == "qwen: 1,234,567 tokens, $2.4691"

print("OK: all checks passed")
