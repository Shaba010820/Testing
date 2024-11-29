import csv
import requests
from bs4 import BeautifulSoup


def count_animal_with_letter(url):
    animal_counts = {}

    if url:
        data = requests.get(url)
        soup = BeautifulSoup(data.text, "html.parser")

        items = soup.find_all("div", class_="mw-category-group")
        for item in items:
            links = item.find_all("a")
            for link in links:
                name = link.text.strip()
                if name:
                    first_letter = name[0].upper()
                    if first_letter.isalpha():
                        if first_letter not in animal_counts:
                            animal_counts[first_letter] = 0
                        animal_counts[first_letter] += 1

        next_page = soup.find("a", string="Следующая страница")
        if next_page:
            url = "https://ru.wikipedia.org" + next_page["href"]
        else:
            url = None

    with open("beasts.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for letter, count in sorted(animal_counts.items()):
            writer.writerow([letter, count])


url = ('https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:'
       '%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83')

count_animal_with_letter(url)

