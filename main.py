import requests

# Ссылка на API
bored_api_url = "http://www.boredapi.com/api/activity"

# Функция для получения случайной активности
def get_random_activity():
    response = requests.get(bored_api_url)
    data = response.json()
    return data["activity"]

# Получение случайной активности
activity = get_random_activity()

# Вывод полученной активности
print(activity)
