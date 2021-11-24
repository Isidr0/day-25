# this creates a list formatted as a string with new lines includes. better to use CSV library.
# with open("weather_data.csv") as data:
#     weather_data = data.readlines()
#     print(weather_data)

# the csv library method is better, but still not as good as pandas. the block of code below is required whenever
# doing something like this with a CSV
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import and install the pandas library. pandas does everything that the csv library does and more in fewer steps.
# it reads data in one step and formats it automatically.

import pandas

data = pandas.read_csv("weather_data.csv")
# data type of a whole table/sheet is a DataFrame
# print(type(data))
# data type of a column is a series
# print(type(data["temp"]))

# convert DataFrame to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# # convert Series to a Python List
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# print(data["temp"].max())
#
# # panda automatically converts column headers to attributes so you can call them as an attribute or by the name
# # it's case sensitive either way
# print(data["temp"])
# print(data.condition)

# get data in rows
# print(data[data.day == "Monday"])

# print the row of data which had the highest temperature
# it's ordered like dataframe/table[column == row]
# print(data[data.temp == data.temp.max()])

# print a particular cell/data value from a row of data.
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print((monday.temp * 9/5) + 32)

# create a dataframe (AKA Table) from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("squirrel_count.csv")
squirrel_color = data["Primary Fur Color"]
red = data[squirrel_color == "Cinnamon"]["Primary Fur Color"].count()
grey = data[squirrel_color == "Gray"]["Primary Fur Color"].count()
black = data[squirrel_color == "Black"]["Primary Fur Color"].count()
color_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey, red, black]
}

red_test = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_test)

# print(red)
# print(red["Primary Fur Color"].count(), grey["Primary Fur Color"].count(), black["Primary Fur Color"].count())

data = pandas.DataFrame(color_dict)

data.to_csv("squirrel_color_count.csv")
