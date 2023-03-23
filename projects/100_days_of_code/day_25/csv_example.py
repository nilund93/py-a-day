import csv
import pandas

if __name__ == "__main__":
    # with open("weather_data.csv", mode="r", encoding="utf-8") as f:
    #     data = f.readlines()
    
    
    # with open("weather_data.csv", mode="r", encoding="utf-8") as f:
    #     data = csv.reader(f)
    #     temperatures = []
    #     for row in data:
    #         if row[1] != "temp":
    #             temperatures.append(int(row[1]))
    #     print(temperatures)
    
    

    data = pandas.read_csv("weather_data.csv")
    # print(data["temp"])
    data_dict = data.to_dict()
    print(data_dict)
    
    temp_list = data["temp"].to_list()
    print(temp_list)
    
    # my avg solution
    average_temp = sum(temp_list)/len(temp_list)
    print(average_temp)
    
    # pandas solution for avg val
    avg_temp = data["temp"].mean()
    print(avg_temp)
    
    # pandas solution for max val
    max_temp = data["temp"].max()
    print(max_temp)
    
    # Get data in columns
    print(data["condition"])
    print(data.condition)
    
    # Get data in rows
    print(data[data.day == "Monday"])
    
    # Pull the row of data where temp is max
    print(data[data.temp == max_temp])
    
    monday_c = data[data.day == "Monday"]
    print(monday_c.condition)
    
    monday_f = int(monday_c.temp) * 9/5 + 32
    print(f"\n{monday_c}C is {monday_f}F, the temperature of Monday")
    
    # Create dataframe from scratch
    data_dict = {
        "student": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    data = pandas.DataFrame(data_dict)
    data.to_csv("new_data.csv")
    