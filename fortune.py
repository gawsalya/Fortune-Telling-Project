

from fortune_function import Horoscope, random_name, print_intro, fortune, get_html, parse_fortunes_bs


def main():

    print_intro()

    first_name = input("Enter your first name: ")
    birthday = input("Enter birthdate (DD/MM/YYYY): ")

    individual = Horoscope(first_name, birthday)

    star_sign = random_name(individual.name)

    # print(f'Lifepath number is: {individual.lifepath()}')

    print(f'star_sign: {individual.star_sign()}')

    # horoscope_url = "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=2"
    # horoscope_doc = get_html(horoscope_url)

    # reading = parse_fortunes_bs(horoscope_url, horoscope_doc)
    # print(reading)


main()
