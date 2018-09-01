def calorie_dictionary(file_path):
    calorie_list = open(file_path, "r")
    calories = {}
    for line in calorie_list:
        (key, val) = line.split(',')
        calories[key] = float(val)
    calorie_list.close()
    return calories

def guidline_dictionary(file_path):
    guidline_list = open (file_path, "r")
    guidlines = {}
    for line in guidline_list:
        (key, val) = line.split(', ')
        guidlines[key] = float(val)
    guidline_list.close()
    return guidlines


def consumption_dictionary(file_path):
    consumption_list = open (file_path, "r")
    persons = {}
    for line in consumption_list:
        (person, food, date, serving) = line.split(',')
        food_dictionary = {food: serving}
        date_dictionary = {date: food_dictionary}
        persons[person] = date_dictionary
    consumption_list.close()
    return persons

print(calorie_dictionary("data/calories_per_serving.txt"))
print(guidline_dictionary("data/guidline.txt"))
print(consumption_dictionary("data/consumption.txt"))