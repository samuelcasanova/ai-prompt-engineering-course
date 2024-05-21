import openai
import getpass

with open('apikey.txt', 'r') as file:
    openai.api_key = file.read()

def complete(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
            "role": "user",
            "content": prompt
            }
        ],
    )
    return response.choices[0].message.content

complete("is this working?")