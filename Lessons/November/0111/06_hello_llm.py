"""Лаба тижня 1. Hello, LLM: перший запит до LM Studio з Python.

Функція ask(question) надсилає питання моделі й повертає текст відповіді.
Форма та сама, що у fake_ask: рядок на вході, рядок на виході, без друку всередині.

ask:
1. Прочитай адресу, модель і ключ із .env через os.getenv
   (LLM_BASE_URL, LLM_MODEL, LLM_API_KEY). Нічого не пиши в коді напряму.
2. Створи клієнт OpenAI, передавши йому адресу і ключ.
3. Надішли запит chat completions: ті самі model і messages, що у твоєму curl.
4. Поверни лише текст відповіді моделі, а не весь об'єкт.

main:
- бере питання через input(), викликає ask, друкує результат.

Куди дивитися: приклад chat completions у README https://github.com/openai/openai-python
Зверни увагу на параметр base_url: саме він спрямовує клієнт на LM Studio.

Перевірок через assert тут немає: модель щоразу відповідає по-різному.
Готово, коли питаєш у терміналі, а реальна модель відповідає текстом.

Запуск: .venv/bin/python Lessons/November/0111/06_hello_llm.py
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def ask(question: str) -> str:
    base_url = os.getenv('LLM_BASE_URL')
    model = os.getenv('LLM_MODEL')
    api_key = os.getenv('LLM_API_KEY')
    client = OpenAI(base_url=base_url, api_key=api_key)
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Give a short answer"},
            {"role": "user", "content": question}
        ],
        temperature=0.7,
    )
    llm_answer = completion.choices[0].message.content
    if llm_answer:
        result = llm_answer
    else:
        result = 'Empty answer!'
    return result


def main() -> None:
    question = input('My question is: ')
    answer = ask(question)
    print(answer)



main()
