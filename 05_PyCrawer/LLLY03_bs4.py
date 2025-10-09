import requests
import bs4

cont = requests.get("https://www.example.com/")
soup = bs4.BeautifulSoup(cont.text, "html.parser")
