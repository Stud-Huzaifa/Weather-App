import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # Create the necessary UI elements
        self.city_label = QLabel("Enter City Name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        # Initialize the UI
        self.initUI()

    def initUI(self):
        # Set window title
        self.setWindowTitle("Weather App")

        # Create a vertical box layout
        vbox = QVBoxLayout()

        # Add widgets to the layout
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        # Set the layout for the QWidget
        self.setLayout(vbox)

        # Aligning the QLabel elements
        self.city_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Adding object names for styling purposes
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # Set stylesheet
        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: Calibri;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: 'Segoe UI Emoji';
            }
            QLabel#description_label {
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "your_api_key_here"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Ensure that HTTP errors are caught
            data = response.json()
            if data["cod"] == 200:
                self.display_weather(data)
            else:
                self.display_error(f"Error: {data['message']}")
        except requests.exceptions.HTTPError as http_error:
            status_code = response.status_code
            self.handle_http_error(status_code)
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error\n Check your internet connection.")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error: The request timed out.")
        except requests.TooManyRedirects:
            self.display_error("Too Many Redirects: Check the URL.")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error: {req_error}")

    def handle_http_error(self, status_code):
        error_messages = {
            400: "Bad Request: Please check your input.",
            401: "Unauthorized: Invalid API Key.",
            403: "Forbidden: Access is denied.",
            404: "City not found.",
            500: "Internal Server Error. Please try again later.",
            502: "Bad Gateway: Invalid response from the server.",
            503: "Service Unavailable: Server is down.",
            504: "Gateway Timeout: No response from the server."
        }
        self.display_error(error_messages.get(status_code, f"HTTP error occurred: {status_code}"))

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"]["temp"]
        temperature_f = (temperature_k - 273.15) * 9/5 + 32  # Convert Kelvin to Fahrenheit
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temperature_f:.0f}°F")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"  # Thunderstorm
        elif 300 <= weather_id <= 321:
            return "🌧️"  # Drizzle
        elif 500 <= weather_id <= 531:
            return "🌦️"  # Rain
        elif 600 <= weather_id <= 622:
            return "❄️"  # Snow
        elif 701 <= weather_id <= 781:
            return "🌫️"  # Mist, Smoke, Haze, Dust, Fog, Sand, Ash, Squall, Tornado
        elif weather_id == 800:
            return "☀️"  # Clear Sky
        elif weather_id == 801:
            return "🌤️"  # Few Clouds
        elif weather_id == 802:
            return "⛅"   # Scattered Clouds
        elif weather_id == 803 or weather_id == 804:
            return "☁️"  # Broken Clouds or Overcast Clouds
        else:
            return "❓"  # Unknown Weather Condition

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
