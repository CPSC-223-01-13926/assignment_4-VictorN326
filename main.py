import weather
# from calender import calender
filename = "w.dat"
info = weather.read_data(filename)
import calendar

while True:
    print("\n\t***TUFFY TITAN WEATHER LOGGER MAIN MENU\n")
    print("1. Set data filename \n2. Add weather dataW")
    print("3.Print Daily Report")
    print("4. Print Historical report \n5. Exit the program\n")

    options = int(input("Enter menu choice: "))

    if options == 1:
        file = input("Enter data filename: ")
        filename = file
    
    elif options == 2:
        date = (input("Enter date as (YYYYMMDD): "))
        time = input("Enter time as (hhmmss): ")
        temperature = int(input("Enter temperature: "))
        humidity = int(input("Enter humidity: "))
        rainfall = float(input("Enter rainfall: "))
    
        info[date + time] = {'t': temperature, 'h': humidity, 'r': rainfall}
        weather.write_data(info, filename)
    
    elif options == 3:
        print()
        date = input("Enter Date (YYYYMMDD): ")
        weather.report_daily(info, date)
    

    elif options == 4:
        print()
        weather.report_historical(info)
        # data = weather_function.read_data(filename)
        # report_historical()
        # historical_Data = []
        # for keys in data.keys():
        #     new_date = "{} {}, {}".format(calender.month_name[int(keys[4:6])], int(keys[6:8]), keys[:4])
        #     if new_date not in historical_Data:
        #         max_temp = weather.max_temperature(data, keys[:8])
        #         min_temp = weather.min_temperature(data, keys[:8])
        #         max_humid = weather.max_humidity(data, keys[:8])
        #         min_humid = weather.min_humidity(data, keys[:8])
        #         total_rain = weather.tot_rain(data, keys[:8])
        #         print("{:<20} {:>12} {:>8} {:>8} {:>8}".format(new_date,max_temp,min_temp,max_humid,min_humid,total_rain))  
        #         historical_Data.append(new_date)
        print()
    
    elif options == 5:
        break
    else:
        print('You have entered an invalid choice')

