import ollama

from config.settings import LLM_MODEL, TEMPERATURE


def generate_answer(prompt):

    response = ollama.chat(
        model=LLM_MODEL,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        options={
            "temperature": TEMPERATURE
        }
    )

    return response["message"]["content"]