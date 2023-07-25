import requests

def get_weather_data(city, api_key):
    BASE_URL = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={city}&appid={api_key}"
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error in fetching weather data.")
        return None

def get_temperature(data, input_date):
    for forecast in data['list']:
        if forecast['dt_txt'] == input_date:
            return forecast['main']['temp']
    return None

def get_wind_speed(data, input_date):
    for forecast in data['list']:
        if forecast['dt_txt'] == input_date:
            return forecast['wind']['speed']
    return None

def get_pressure(data, input_date):
    for forecast in data['list']:
        if forecast['dt_txt'] == input_date:
            return forecast['main']['pressure']
    return None

def main():
    API_KEY = "b6907d289e10d714a6e88b30761fae22"
    CITY = "London,us"

    data = get_weather_data(CITY, API_KEY)
    if data is None:
        return

    while True:
        print("\nMenu:")
        print("1. Get weather temperature")
        print("2. Get wind speed")
        print("3. Get pressure")
        print("0. Exit")

        choice = input("Enter your choice (0-3): ")

        if choice == '1':
            input_date = input("Enter the date in the format 'YYYY-MM-DD HH:MM:SS': ")
            temperature = get_temperature(data, input_date)
            if temperature is not None:
                print(f"Temperature at {input_date}: {temperature} K")
            else:
                print("Invalid or no data available for the input date.")

        elif choice == '2':
            input_date = input("Enter the date in the format 'YYYY-MM-DD HH:MM:SS': ")
            wind_speed = get_wind_speed(data, input_date)
            if wind_speed is not None:
                print(f"Wind Speed at {input_date}: {wind_speed} meter/sec")
            else:
                print("Invalid or no data available for the input date.")

        elif choice == '3':
            input_date = input("Enter the date in the format 'YYYY-MM-DD HH:MM:SS': ")
            pressure = get_pressure(data, input_date)
            if pressure is not None:
                print(f"Pressure at {input_date}: {pressure} hPa")
            else:
                print("Invalid or no data available for the input date.")

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
