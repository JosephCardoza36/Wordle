import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.rockpapershotgun.com/wordle-past-answers')
soup = BeautifulSoup(response.text, "html.parser")
words = soup.find_all(class_='inline')

word_list = [word.text.lower().split('\n') for word in words]
word_list[0].remove('')
word_list[0].pop()
