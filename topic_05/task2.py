import requests
response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")
currency = input("Введіть валюту (USD, EUR, PLN): ")
amount = float(input("Введіть суму: "))
for elem in response.json():
    if elem["cc"] == currency:
        result = amount * elem["rate"]
        print("Результат:", result, "грн")
        break
else:
    print("Невідома валюта")