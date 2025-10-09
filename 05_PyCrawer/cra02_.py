import requests
from bs4 import BeautifulSoup

# 定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive'
    }
# 目标URL
url = 'https://example.com'


def fetch_page(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        return response.text
    except requests.RequestException as e:
        print(f"请求出错: {e}")
        return None


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    # 获取页面标题
    title = soup.title.string if soup.title else '无标题'
    print(f"页面标题: {title}")
    # 获取所有链接
    links = []
    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        text = a_tag.get_text(strip=True)
        links.append((text, link))
    return links


def main():
    html_content = fetch_page(url)
    if html_content:
        links = parse_html(html_content)
        print("页面中的链接:")
        for text, link in links:
            print(f"{text}: {link}")


if __name__ == '__main__':
    main()
