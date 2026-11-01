"""Задача 5. Заглушка функції ask.

Поки LM Studio не налаштований, зроби заглушку майбутньої функції ask(question).

fake_ask:
- прибирає пробіли по краях питання;
- повертає рядок: Model is offline. You asked: "<question>"
  (подвійні лапки мають бути частиною результату);
- нічого не друкує.

main:
- питає в користувача текст через input();
- передає його у fake_ask;
- друкує результат.
curl http://192.168.0.104:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "google/gemma-4-e4b", "messages": [{"role": "user", "content": "What day is today?"}]}'
Після проходження перевірок програма чекатиме на твоє введення в терміналі.

Запуск: .venv/bin/python Lessons/November/0111/05_fake_ask.py
"""


def fake_ask(question: str) -> str:
    return f'Model is offline. You asked: "{question.strip()}"'



def main() -> None:
    incoming = input('Enter your question:')
    processed_input = fake_ask(incoming)
    print(processed_input)


assert fake_ask("hello") == 'Model is offline. You asked: "hello"'
assert fake_ask("  what is a token?  ") == 'Model is offline. You asked: "what is a token?"'

print("OK: all checks passed")

main()
