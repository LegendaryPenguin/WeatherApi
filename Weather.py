import requests

try: 
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=29.55&lon=73.53&units=imperial&appid=a142cfbb9a393f78ebef57345f7e2938")

except:
    print ("There is no internet access :(") 

response_json = response.json()

temp = response_json['main']['temp']
temp_min = response_json['main']['temp_min']
temp_max = response_json['main']['temp_max']

# print (temp)
# print (temp_min)
# print (temp_max)
print (f'In Sriganganagar, it is currently {temp} degrees')
print (f'In Sriganganagar, the low temperature for the day is {temp_min} degrees')
print (f'In Sriganganagar, the high temperature for the day is {temp_max} degrees')

class City:
    def __init__(self, name, lat, lon, units = 'metric'):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try: 
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&units={self.units}&appid=a142cfbb9a393f78ebef57345f7e2938")
        except:
            print ("There is no internet access :(") 
        self.response_json = response.json()
        self.temp = self.response_json['main']['temp']
        self.temp_min = self.response_json['main']['temp_min']
        self.temp_max = self.response_json['main']['temp_max']

    def temp_print(self):
        print (f'In {self.name}, it is currently {self.temp} degrees')
        print (f'In {self.name}, the low temperature for the day is {self.temp_min} degrees')
        print (f'In {self.name}, the high temperature for the day is {self.temp_max} degrees')

my_city = City("Tokyo", 35.6762, 139.6503, units = 'imperial')
my_city.temp_print()

vacation_city = City('Portland', 45.5152, -122.6768, units = 'imperial')
vacation_city.temp_print()
print ('Yay')