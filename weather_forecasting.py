import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can use "imperial" for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        
        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("Error fetching weather data")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    city = input("Enter city name: ")
    
    get_weather(api_key, city)



    