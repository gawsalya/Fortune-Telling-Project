# 🧑‍💻 Fortune Telling

Hello! Welcome to Kausi Fortune Telling!

This project is designed to take a user's name and date of birth to calculate their lifepath number and provide the meaning of this. Additionally calculates the star sign and returns their fortune for the day. I have web-scraped from an existing fortune telling website to give an accurate reading.

I have chosen to do this project due to my interest in horoscopes and astrology. \***\*Key highlights** of the code design is using classes to define Horoscope details and Web-scraping code to pull out the relevant fortune. I enjoyed creating the class and found that it helped organise the relevant details I wanted it to return and kept these functions separate from others. Web-scraping used Beautiful Soup to read the HTML tags which I previously inspected on the website to find the relevant tag I would need.

## Applications:

Aspects of this code can be used to create different programs. For example utilising **classes** in bigger projects would be very useful in being able to find where an error is and can be useful in creating derivations of the same class, for example if we wanted to use a different method to calculate lifepath we can keep the same methods and just re-write this one.

**Web-scraping** can be useful in picking out certain information from a website you want -- though please be mindful of the current legal advice!

## 🛠️ Getting Setup

1. **Fork** this Repository to your Github Account
2. **Clone** your Repository to your laptop
3. **Open** this folder in VSCode

## Installation and Running

1. Consider using a virtual environment (venv)
2. Install requirements
   - `pip install -r requirements.txt`
3. Run the script
   - `python3 fortune.py`

## 🗂️ Files Explained

In this Repository you will find all scripts required to run the code.

- `README.md`
  - This is the file you are currently reading
- `.gitignore`
  - This file is used to tell Git what files to ignore for any changes. This can be safely ignored.
- `requirements.txt`
  - This file contains all the relevant libraries needed to run the code
- `life_path.csv`
  - CSV file containing the life path numbers and their corresponding meaning
- `star_sign.csv`
  - CSV file containing the 12 different star signs and the number required to scrape that specific sign from the website
- `fortune.py`
  - The main script to run the code
- `fortune_function.py`
  - This file contains all the functions required in the main code.
- `test_fortune.py`
  - This file contains a few tests to make sure the code is running as needed.
