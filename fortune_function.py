import csv
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

        self.lifepath = self.lifepath()

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

    def lifepath_meaning(self):
        with open('life_path.csv', 'r') as f_obj:
            meanings = csv.reader(f_obj, delimiter=';')
            next(meanings)
            for meaning in meanings:
                if int(meaning[0]) == self.lifepath:
                    return meaning[1]

    def star_sign(self):
        df = pd.read_csv('star_sign.csv', parse_dates=[
                         'date_from', 'date_to'], date_format='%d/%m')

        date_to_bool = df['date_to'] > '1900-08-18'
        date_to_dates = df.loc[date_to_bool == True]
        date_from_dates = date_to_dates['date_from'] < '1900-08-18'
        horoscope = date_to_dates.loc[date_from_dates == True]

        return horoscope['star_sign'].iat[0]


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


def starry():
    print('   *  .  . *       *    .        .        .   *    .    *        .       .      .        .            *      *          .     *      *        *    .     *  . ')


def get_html(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf_8")
    return html


def parse_fortunes_bs(html):
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.p
    today_horoscope = tags.get_text()

    return today_horoscope


def number_for_sign(sign: str):
    df = pd.read_csv('star_sign.csv')
    number = (df[df['star_sign'] == 'Leo']['number']).to_string(index=False)
    return number
