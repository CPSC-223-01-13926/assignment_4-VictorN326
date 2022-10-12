import json
import calendar
filename = "w.dat"
def read_data(filename = 'w.dat'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data  
    except FileNotFoundError:
     return {}
def write_data(data, filename = 'w.dat'):
    with open(filename, 'w') as f:
        json.dump(data, f)
    
def max_temperature(data = {}, date = ''):
    temperature = []
    for key in data:
        if date == key[:8]:
            temperature.append(data[key]["t"])
    if(len(temperature)):
        return max(temperature)
    else:
        #doesn't do anything if the temp doesn't have the date as key
      return  None 
        
    
def min_temperature(data = {}, date = ''):
    temperature = []
    for key in data:
        if date == key[:8]:
            temperature.append(data[key]["t"])
    if(len(temperature)):
        return min(temperature)
    else:
       return None

def max_humidity(data = {}, date = ''):
    humid = []
    for key in data:
        if date == key[:8]:
            humid.append(data[key]["h"]) 
    if len(humid):
        return max(humid)
    else:
        return None   
   
def min_humidity(data= {}, date = ''):
    humid = []
    for key in data:
        if date == key[:8]:
            humid.append(data[key]["h"])
    if len(humid):
        return min(humid)
    else:
        return None
            
        
def tot_rain(data = {},date = ''):
    rain = []
    for key in data:
        if date == key[:8]:
            rain.append(data[key]["r"])
    if(len(rain)):
        return sum(rain)
    else:
        return None
def report_daily(data = {},date = ''):
       print("="*24, "{:^14}".format("DAILY REPORT"), "="*24)
       print("{:<20}  {:^8}  {:>12}  {:>8}  {:>8}".format(
            "Date", "Time", "Temperature", "Humidity", "Rainfall"))
       print("{:<20}  {:^8}  {:>12}  {:>8}  {:>8}".format(
            "="*20, "="*8, "="*12, "="*8, "="*8))
       for key in data.keys():
            if key[:8] == date:
                weather_date = "{} {}, {}".format(calendar.month_name[int(key[4:6])], int(key[6:8]), int(key[:4]))

                weather_time = "{}:{}:{}".format(key[8:10], key[10:12], key[12:14])
                temperature = data[key]['t']
                humidity = data[key]['h']
                rainfall = data[key]['r']
                rainfall_second = "{:.2f}".format(float(rainfall))
                print("{:<20}  {:^8}  {:>11}  {:>8}  {:>8}".format(
                        weather_date, weather_time, temperature, humidity, rainfall_second))
                
def report_historical(data ={}):
    print("="*30, "{:^20}".format("HISTORICAL REPORT"), "="*30)
    print("{:<20}  {:>12}  {:>12}  {:>8}  {:>8}  {:>8}".format(
            "", "Maximum", "Minimum", "Maximum", "Minimum", "Total") +
            "\n{:<20}  {:>12}  {:>12}  {:>8}  {:>8}  {:>8}".format(
            "Date", "Temperature", "Temperature", "Humidity", "Humidity", "Rainfall"))
    print("{:<20}  {:>12}  {:>12}  {:>8}  {:>8}  {:>8}".format(
            "="*20, "="*12, "="*12, "="*8, "="*8, "="*8))
    
    # print('============================== HISTORICAL REPORT ===========================\n')
    # print("                          Minimum      Maximum   Minumum   Maximum     Total\n")
    # print("Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n")
    # print("====================  ===========  ===========  ========  ========  ========\n")
    historical_Data = []
    for keys in data.keys():
        new_date = "{} {}, {}".format(calendar.month_name[int(keys[4:6])], int(keys[6:8]), int(keys[:4]))
        if new_date not in historical_Data:
            max_temp = max_temperature(data, keys[:8])
            min_temp = min_temperature(data, keys[:8])
            max_humid = max_humidity(data, keys[:8])
            min_humid = min_humidity(data, keys[:8])
            total_rain = tot_rain(data, keys[:8])
            total_rain2 = "{:.2f}".format(float(total_rain))
            print("{:<20} {:>11} {:>8} {:>8} {:>8}".format(new_date,min_temp,max_temp,min_humid,max_humid,total_rain2))  
            historical_Data.append(new_date)
    