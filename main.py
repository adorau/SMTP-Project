import pandas
import datetime
import random
import smtplib
from tkinter import *
from tkinter import messagebox

window = Tk()
window.withdraw()
anna_password = "***"
maria_mail = "maria.poczta2@outlook.com"
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

data = pandas.read_csv('data_bday.csv', delimiter=';')
dict_data = data.to_dict('records')
print(dict_data)

time = datetime.datetime.now()
now_day = time.day
now_month = time.month

for i in dict_data:
    if i["day"] == now_day and i["month"] == now_month:
        letter_choice = random.choice(letters)
        with open(letter_choice, "r") as file:
            data = file.read()
        data = data.replace("[NAME]", i["name"])
        with open(letter_choice, "w") as file:
            file.write(data)

        with smtplib.SMTP("smtp-mail.outlook.com") as connection:
            connection.starttls()  # connection secured
            connection.login(user=maria_mail, password=anna_password)
            connection.sendmail(from_addr=maria_mail, to_addrs=i["email"], msg=f"Subject:BDAY \n\n{data}")
        with open(letter_choice, "r") as file:
            data = file.read()
        data = data.replace(i["name"], "[NAME]")
        with open(letter_choice, "w") as file:
            file.write(data)
        messagebox.showinfo(title="Info", message=f"Message was sent to {i['name']}")
