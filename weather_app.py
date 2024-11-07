import requests

API_KEY = '30279a47b5d664c56ada5bba6e425f45'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        main = data["main"]
        wind = data["wind"]
        weather = data["weather"][0]

        print(f"Weather in {city.capitalize()}:")
        print(f"Temperature: {main['temp']}°C")# alt 0176
        print(f"Weather: {weather['description'].capitalize()}")
        print(f"Humidity:{main['humidity']}%")
        print(f"Wind Speed:{wind['speed']}m/s")



    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"City '{city}' not found. Please check the spelling or try different way")
        else:
            print(f"HTTP error occured: {http_err}")
    except Exception as err:
        print(f"An error occured: {err}")


def main():
    print("Welcome Weather App")

    while True:
        city = input("\n Enter the name of the city (or type exit to quit): ").strip()
        if city.lower()=="exit":
            print("Exiting the weather app")
            break

        get_weather(city)


if __name__ == "__main__":
    main()


       