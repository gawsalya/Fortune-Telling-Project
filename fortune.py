'''functions required to run fortune code'''
from fortune_function import Horoscope, print_intro, get_html, parse_fortunes_bs, starry, number_for_sign


if __name__ == '__main__':

    print_intro()

    first_name = input("Enter your first name: ")
    birthday = input("Enter birthdate (DD/MM/YYYY): ")

    individual = Horoscope(first_name, birthday)

    starry()
    print(f'Lifepath number is: {individual.lifepath_number}')
    print(f'Lifepath meaning - {individual.lifepath_meaning()}')

    starry()
    star_sign = individual.star_sign()
    print(f'Star Sign: {star_sign}')

    sign_number = number_for_sign(star_sign)
    horoscope_url = f"""https://www.horoscope.com/us/horoscopes/
                        general/horoscope-general-daily-today.aspx?sign={sign_number}"""
    horoscope_doc = get_html(horoscope_url)

    reading = parse_fortunes_bs(horoscope_doc)
    print(reading)
    starry()
