import requests

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def main():
    urls = [
        "http://httpbin.org/get",
        "http://httpbin.org/ip",
        "http://httpbin.org/user-agent"
    ]
    for url in urls:
        html = get_html(url)
        print(html)

if __name__ == "__main__":
    main()