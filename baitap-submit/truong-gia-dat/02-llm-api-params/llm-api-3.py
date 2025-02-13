import requests
from bs4 import BeautifulSoup
from openai import OpenAI



def fetch_website_content(website):

    response = requests.get(website)
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.text, "html.parser")
        content_list = soup.find_all("p")
        content = " "
        for p in content_list:
            content += p.text.strip()
        return content
    
    return None


def ai_summary(content):
    client = OpenAI(
        api_key="api_key"
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are given a content of an article, please summarize the article in Vietnamese"
            },
            {
                "role": "user",
                "content": f"This is the content of the article: \n ### \n {content} \n ###"
            }
        ],
        model="gpt-4o-mini"
    )

    return response.choices[0].message.content



def main():
    user_input = input("website url: ")
    print(f"Fetching content of the website...")
    website_content = fetch_website_content(user_input)
    if website_content is not None:
        print(f"Finished fetching content of the website...")
        print("AI summarizing the article...")
        ai_response = ai_summary(website_content)
        print(ai_response)
    else:
        print(f"Unable to fetch content of {user_input}")
    

main()