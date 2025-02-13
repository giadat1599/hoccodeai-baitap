from openai import OpenAI



def translate(prompt):
    client = OpenAI(
        api_key="api_key"
    )

    system_prompt = """
        You are going to translate a text from English to Vietnamese. I want the translated version to be very funny but also include a bit of sadness
        Please keep the original format when translating
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



def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()
    
    translated = ""    
    print("AI translating...")
    for line in lines:
        if line == '\n':
            translated += line
        else:
            translated += translate(line)
    
    print("AI finished translating...")
    with open("output.txt", "w") as file:
        file.write(translated)



main()