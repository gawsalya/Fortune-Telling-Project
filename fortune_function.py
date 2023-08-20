'''libraries required for fortune functions'''
import csv
import datetime
import math
from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup


class Horoscope:
    '''Horoscope class containing information about a person's astrology information'''

    def __init__(self, name: str, birthday: int):
        if name.strip() == " ":
            raise ValueError("Name cannot be empty!")
        if name.isalpha() is not True:
            raise ValueError("Name can only be letters!")

        self.name = name.title()

        try:
            self.datetime_format = datetime.datetime.strptime(
                birthday, '%d/%m/%Y')
            self.birthday = birthday
        except ValueError:
            print("Birthdate not valid, please enter in format dd/mm/yyyy")

        self.lifepath_number = self.lifepath()

    def lifepath(self):
        '''function to calculate lifepath number from date of birth'''
        numbers = int(self.birthday.replace('/', ''))

        total = 0
        while (numbers > 0 or total > 9):
            if numbers == 0:
                numbers = total
                total = 0

            total += numbers % 10
            numbers = math.floor(numbers/10)

        return total

    def lifepath_meaning(self):
        '''function to return lifepath meaning from csv depending on number'''
        with open('life_path.csv', 'r', encoding='utf-8') as f_obj:
            meanings = csv.reader(f_obj, delimiter=';')
            next(meanings)
            for meaning in meanings:
                if int(meaning[0]) == self.lifepath_number:
                    return meaning[1]
        return None

    def star_sign(self):
        '''function to find star sign based of birth'''
        dataframe = pd.read_csv('star_sign.csv', parse_dates=[
            'date_from', 'date_to'], date_format='%d/%m')

        date_of_birth = datetime.datetime.strptime(
            self.birthday, '%d/%m/%Y')

        date_to_bool = dataframe['date_to'] > f'1900-{date_of_birth.month}-{date_of_birth.day}'
        date_to_dates = dataframe.loc[date_to_bool == True]
        date_from_dates = date_to_dates['date_from'] < f'1900-{date_of_birth.month}-{date_of_birth.day}'
        horoscope = date_to_dates.loc[date_from_dates == True]

        return horoscope['star_sign'].iat[0]


def print_intro():
    '''function to print the introduction ASCII art'''
    print(r"      .--.   _,")
    print(r"  .--;    \ /(_")
    print(r" /    '.   |   '-._    . ' .")
    print(r"|       \  \    ,-.)  -= * =- Welcome to Kausi Fortune Telling! ")
    print(r" \ /\_   '. \((` .(    '/. '  We thank you for your visit ~ ~ ~")
    print(r"  )\ /     \ )\  _/   _/")
    print(r" /  \\    .-'   '--.  /_")
    print(r"|    \\_.' ,        \/||")
    print(r"\     \_.-';,_) _)'\ \||")
    print(r" '.       /`\   (   '._/")
    print(r"   `\   .;  |  . '.")
    print(r"     ).'  )/|      /")
    print(r"     `    ` |  \|   |")
    print(r"             \  |   |")
    print(r"              '.|   |")
    print(r"                 \  '\__")
    print(r"                  `-._  '. _")
    print(r"                     \`;-.` `._")
    print(r"                      \ \ `'-._")
    print(r"                       \ |")
    print(r"                        \ )")
    print(r"                         \_")


def starry():
    '''function to print starry line breaks'''
    print('   *  .  . *       *    .        .        .   *    .    *        .       .      .        .            *      *          .     *      *        *    .     *  . ')


def get_html(url):
    '''function to open the url and get the information'''
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf_8")
    return html


def parse_fortunes_bs(html):
    '''function to find the fortune information from the url'''
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.p
    today_horoscope = tags.get_text()

    return today_horoscope


def number_for_sign(sign: str):
    '''function to find the corresponding number for the star sign required for the url'''
    dataframe = pd.read_csv('star_sign.csv')
    number = (dataframe[dataframe['star_sign'] == sign]
              ['number']).to_string(index=False)
    return number


def fortune_today(sign_number: str) -> str:
    horoscope_url = f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={sign_number}"
    horoscope_doc = get_html(horoscope_url)

    reading = parse_fortunes_bs(horoscope_doc)
    return reading
