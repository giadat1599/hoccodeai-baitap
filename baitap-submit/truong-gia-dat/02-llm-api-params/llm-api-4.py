from openai import OpenAI


def generate_code(prompt):
    client = OpenAI(
        api_key="api_key"
    )

    system_prompt = """
        You are an expert in Python, user will provide you a question about coding and you will awnser to user's question
        Just awnser with the code only, please awnser without markdown
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = res.choices[0].message.content or ""

    return result


def write_to_file(awnser):        
    with open("final.py", "w") as file:
        file.write(awnser)


def main():
    user_input = input("User: ")
    answer = generate_code(user_input)    
    write_to_file(answer)


main()