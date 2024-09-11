 Weather App 🌦️

A simple Weather Application built using Python, PyQt5, and the OpenWeatherMap API. The app allows users to search for the current weather of any city, displaying the temperature, weather condition, and a relevant emoji representing the weather.

## Features
- Fetch current weather data for any city using the OpenWeatherMap API.
- Display weather conditions, temperature in Fahrenheit, and a relevant weather emoji.
- User-friendly graphical interface built with PyQt5.
- Error handling for invalid cities, API errors, and connectivity issues.

## Requirements
To run the project, you'll need the following:
- Python 3.x
- PyQt5 library
- Requests library

### Install dependencies:
```bash
pip install PyQt5 requests
```

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/weather-app.git
    ```
2. Navigate into the project directory:
    ```bash
    cd weather-app
    ```
3. Add your OpenWeatherMap API key to the `get_weather` function in `WeatherApp.py`:
    ```python
    api_key = "your_api_key_here"
    ```
4. Run the application:
    ```bash
    python weather_app.py
    ```

## Usage
1. Enter the name of the city.
2. Click "Get Weather".
3. The app will display the current temperature in Fahrenheit, a weather description, and an emoji corresponding to the weather condition.

## Error Handling
The app handles a variety of potential errors:
- Invalid city names
- API errors (bad requests, unauthorized access, etc.)
- Internet connection issues

## Weather Emojis 🌥️

The app shows different emojis based on the weather conditions:
- ⛈️ Thunderstorm
- 🌧️ Drizzle
- 🌦️ Rain
- ❄️ Snow
- 🌫️ Fog/Mist
- ☀️ Clear sky
- 🌤️ Few clouds
- ⛅ Scattered clouds
- ☁️ Overcast clouds
- ❓ Unknown conditions


## API Used

- [OpenWeatherMap API](https://openweathermap.org/api)


## Contributions
Feel free to open issues or submit pull requests if you'd like to contribute to the project.
