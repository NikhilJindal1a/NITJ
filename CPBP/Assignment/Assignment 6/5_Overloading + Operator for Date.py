# 5. Write a program that overloads the + operator so that it can add a specified number of days to a given date.

from datetime import datetime, timedelta

class Date:
    def __init__(self, day, month, year):
        self.date = datetime(year, month, day)

    def __add__(self, days):
        new_date = self.date + timedelta(days=days)
        return Date(new_date.day, new_date.month, new_date.year)

    def display(self):
        print(self.date.strftime("%d-%m-%Y"))

# Example usage
date = Date(10, 11, 2024)
new_date = date + 5
new_date.display()
