import requests
import json

def main():
    url = "https://us-central1-my-project-71081-1696363517843.cloudfunctions.net/test-function"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        titles = data.get('titles', [])
        
        if titles:
            for index, title in enumerate(titles, start=1):
                print(f"{index}. {title}")
        else:
            print("Herhangi bir başlık bulunamadı.")

    except requests.exceptions.RequestException as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    main()