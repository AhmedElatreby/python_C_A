# accessing list
shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]

print(last_element)

index5_element = shopping_list[5]

print(index5_element)

# replace item in the list
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
print(garden_waitlist)
garden_waitlist[1] = "Calla"
print(garden_waitlist)
garden_waitlist[-1] = "Alex "
print(garden_waitlist)


# remove from list
order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)
new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")
print(new_store_order_list)

# Two-Dimensional list
heights = [["Jenny", 61], ["Alexus", 70], [
    "Sam", 67], ["Grace", 64], ["Vik", 68]]
print(heights)
ages = [["Aaron", 15], ["Dhruti", 16]]
print(ages)

# Accessing 2D list
class_name_test = [["Jenny", 90], [
    "Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)
sams_score = class_name_test[2][1]
print(sams_score)
ellies_score = class_name_test[-1][-1]
print(ellies_score)

# Modifying 2D Lists
incoming_class = [["Kenny", "American", 9], [
    "Tanya", "Russian", 9], ["Madison", "Indian", 7]]
print(incoming_class)
incoming_class[2][2] = 8
print(incoming_class)
incoming_class[-3][-3] = "Ken"
print(incoming_class)

# INTRODUCTION TO LISTS
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], [
    "Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)
customer_data[2][2] = False
print(customer_data)
customer_data[1].remove(False)
print(customer_data)
customer_data_final = customer_data + \
    [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

# Usiung .(insert) to added into list
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)
front_display_list.insert(0, "Pineapple")
print(front_display_list)

# using .pop() to remove in the list
data_science_topics = ["Machine Learning", "SQL",
                       "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

data_science_topics.pop()
print(data_science_topics)
data_science_topics.pop(3)
print(data_science_topics)

# using range() function
number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

# using range function to skip numbers
range_five_three = range(5, 15, 3)
range_diff_five = range(0, 40, 5)
print(range_diff_five)

# using len() function
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that",
             "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
range_list = range(2, 3000, 100)
long_list_len = len(long_list)
print(long_list_len)
range_list_length = len(range_list)
print(range_list_length)


# Slicing List 1
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:2]
print(beginning)
middle = suitcase[2:4]
print(middle)

# Slicing List 2
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
last_two_elements = suitcase[-2:]
print(last_two_elements)
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

# using .count() cunftion
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie",
         "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]
jake_votes = votes.count("Jake")
print(jake_votes)
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place",
             "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()
print(names)
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
cities.sort(reverse=True)
print(cities)

# using sorted(..) function
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]
games_sorted = sorted(games)
print(games)
print(games_sorted)

# WORKING WITH LISTS IN PYTHON
# Review
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table",
             "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
print(inventory_len)

first = inventory[0]
print(first)

last = inventory[-1]
print(last)

inventory_2_6 = inventory[2:6]
print(inventory_2_6)

first_3 = inventory[0:3]
print(first_3)

twin_beds = inventory.count("twin bed")
print(twin_beds)

removed_item = inventory.pop(4)
print(removed_item)

inventory.insert(10, "19th Century Bed Frame")
print(inventory)

inventory = sorted(inventory)
print(inventory)
