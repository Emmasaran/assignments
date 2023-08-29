import requests

def get_weather_data(city, api_key):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def get_temperature(data, datetime):
    for entry in data['list']:
        if entry['dt_txt'] == datetime:
            return entry['main']['temp']
    return None

def get_wind_speed(data, datetime):
    for entry in data['list']:
        if entry['dt_txt'] == datetime:
            return entry['wind']['speed']
    return None

def get_pressure(data, datetime):
    for entry in data['list']:
        if entry['dt_txt'] == datetime:
            return entry['main']['pressure']
    return None

def main():
    api_key = "none"
    city = "Munich,De"
    data = get_weather_data(city, api_key)
    
    while True:
        print("\nOptions:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '0':
            break
        elif choice == '1':
            datetime = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature(data, datetime)
            if temperature is not None:
                print(f"Temperature at {datetime}: {temperature}°C")
            else:
                print("Data not found for the specified date and time.")
        elif choice == '2':
            datetime = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(data, datetime)
            if wind_speed is not None:
                print(f"Wind Speed at {datetime}: {wind_speed} m/s")
            else:
                print("Data not found for the specified date and time.")
        elif choice == '3':
            datetime = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(data, datetime)
            if pressure is not None:
                print(f"Pressure at {datetime}: {pressure} pressure")
            else:
                print("Data not found")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
