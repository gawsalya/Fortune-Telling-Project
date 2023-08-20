'''functions required to run fortune code'''
from fortune_function import Horoscope, print_intro, starry, number_for_sign, fortune_today


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

    sign_number = str(number_for_sign(star_sign))
    reading = fortune_today(sign_number)
    print(reading)
    starry()
