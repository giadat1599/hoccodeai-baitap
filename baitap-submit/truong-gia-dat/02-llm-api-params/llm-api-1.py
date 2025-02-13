

from openai import OpenAI

client = OpenAI(
    api_key="api_key"
)


while True:
    user_input = input("-> You: ")
    chat = client.chat.completions.create(
        messages=[
            {
                "role": 'user',
                "content": user_input,
            }
        ],
        model="gpt-4o-mini",        
    )

    
    print(chat.choices[0].message.content or "", end="")
    



