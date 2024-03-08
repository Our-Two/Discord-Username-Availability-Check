import requests
import os
from dotenv import load_dotenv

load_dotenv()

def req(url, headers=None, payload=None):
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    user = input("Input Username..\n")
    url = 'https://discord.com/api/v9/users/@me/pomelo-attempt'
    custom_headers = {'Authorization': os.getenv("AUTH")}
    custom_payload = {'username': user}

    response_data = req(url, headers=custom_headers, payload=custom_payload)
    if response_data:
        if response_data == {'taken': False}:
            print(f'Username "{user}" is Available')
        elif response_data == {'taken': True}:
            print(f'Username "{user}" is Taken')

if __name__ == "__main__":
    main()
