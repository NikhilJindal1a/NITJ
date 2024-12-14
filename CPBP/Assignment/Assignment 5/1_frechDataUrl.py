# 1. Write a program that fetches data from a specific URL and print it on screen.
import requests

# Fetch data from URL
url = input("Enter the URL: ")
try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Data fetched from URL:")
        print(response.text)
    else:
        print("Failed to fetch data. HTTP Status Code:", response.status_code)
except Exception as e:
    print("Error occurred:", e)
