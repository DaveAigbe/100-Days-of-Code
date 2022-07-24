import pandas

filename = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'

data = pandas.read_csv(filename)

# print(type(data))
# print(type(data['temp']))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].tolist()
# print(temp_list)
#
# print(data['temp'].mean())
# print(data['temp'].max())
#
#
# # Get Data in Columns
# print(data['condition'])
# print(data.condition)

# Get Data in rows
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print((monday.temp)*(9/5)+32)

# Create Dataframe
# data_dict = {
#     'students': ['amy','jon','berto'],
#     'scores': [55,93,83]
# }
# data_1 = pandas.DataFrame(data_dict)
# data_1.to_csv("new_data.csv")
# all_colors = data.Primary_Fur_Color.to_list()
#


gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
