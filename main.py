##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import datetime as dt
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv('.env')

EMAIL = os.getenv('email')
PASSWORD = os.getenv('password')

birthday_file = pd.read_csv('birthdays.csv')
now = dt.datetime.now()
year, month, day = now.year, now.month, now.day


birthday_info = {value.person : [value.year, value.month, value.day] for (key, value) in birthday_file.iterrows()}

for name in birthday_info:
    if birthday_info[name] == [year, month, day]:
        print('hey')

        PLACEHOLDER = "[NAME]"
        letter1 = 'letter_1.txt'
        letter2 = 'letter_2.txt'
        letter3 = 'letter_3.txt'


        with open(random.choice([letter1, letter2, letter3])) as letter_file:
            letter_contents = letter_file.read()
            new_letter = letter_contents.replace(PLACEHOLDER, name)
            with open(f"letter_for_{name}.txt", mode="w") as completed_letter:
                completed_letter.write(new_letter)


        message = f'subject: Happy Birthday\n\n {new_letter}'
        
        with smtplib.SMTP_SSL(os.getenv('smtp'), os.getenv('port')) as connection:
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(EMAIL, "examplemail@mail.com", message)
