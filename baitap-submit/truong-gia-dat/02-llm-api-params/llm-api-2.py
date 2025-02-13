

from openai import OpenAI

client = OpenAI(
    api_key="api_key"
)

messages = []

while True:
    print("\n")
    print(messages)
    print("\n")
    user_input = input("-> You: ")
    messages.append({"role": "user", "content": user_input})

    chat = client.chat.completions.create(
        messages=messages,
        model="gpt-4o-mini",
        stream=True
    )

    assistant_output = ""
    for chunk in chat:
        assistant_output += chunk.choices[0].delta.content or ""
        print(chunk.choices[0].delta.content or "", end="", flush=True)
    
    
    messages.append({"role": "assistant", "content": assistant_output})


