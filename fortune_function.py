import datetime
import math
import sys
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Horoscope:
    '''Video class containing information about video'''

    def __init__(self, name: str, birthday: int):
        if name.strip() == " ":
            raise ValueError("Name cannot be empty!")
        elif name.isalpha() is not True:
            raise ValueError("Name can only be letters!")
        else:
            self.name = name

        try:
            self.datetime_format = datetime.datetime.strptime(
                birthday, '%d/%m/%Y')
            self.birthday = birthday
        except ValueError:
            print("Birthdate not valid, please enter in format dd/mm/yyyy")

    def lifepath(self):
        numbers = int(self.birthday.replace('/', ''))

        total = 0
        while (numbers > 0 or total > 9):
            if (numbers == 0):
                numbers = total
                total = 0

            total += numbers % 10
            numbers = math.floor(numbers/10)

        return total

    def star_sign(self):
        df = pd.read_csv('star_sign.csv', parse_dates=[
                         'date_from', 'date_to'], date_format='%d/%m')
        # Get an array containing each row as a tuple
        print(df.dtypes)

        # print(self.datetime_format)


def random_name(first_name):
    # function taking the input string name and return a random number between 0-50
    # create a hash function that will use the letters in their first name to create a random number
    name = first_name.lower()
    sum_name = sum(map(ord, name))
    return sum_name % 9


def fortune(fortune_num):
    fortune_data = pd.read_csv(sys.argv[1], delimiter=';', header=0)
    fd = fortune_data.to_dict('records')
    for fortunes in fd:
        if fortunes['number'] == fortune_num:
            return (fortunes['fortune'])


def print_intro():
    print("      .--.   _,")
    print("  .--;    \ /(_")
    print(" /    '.   |   '-._    . ' .")
    print("|       \  \    ,-.)  -= * =- Welcome to Sigma Labs Fortune Telling! ")
    print(" \ /\_   '. \((` .(    '/. '  We thank you for your visit ~ ~ ~")
    print("  )\ /     \ )\  _/   _/")
    print(" /  \\    .-'   '--.  /_")
    print("|    \\_.' ,        \/||")
    print("\     \_.-';,_) _)'\ \||")
    print(" '.       /`\   (   '._/")
    print("   `\   .;  |  . '.")
    print("     ).'  )/|      /")
    print("     `    ` |  \|   |")
    print("             \  |   |")
    print("              '.|   |")
    print("                 \  '\__")
    print("                  `-._  '. _")
    print("                     \`;-.` `._")
    print("                      \ \ `'-._")
    print("                       \ |")
    print("                        \ )")
    print("                         \_")


def get_html(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf_8")
    return html


def parse_fortunes_bs(domain_url, html):
    stories = []
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.p
    today_horoscope = tags.get_text()

    return today_horoscope
