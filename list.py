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

# using rang() function
number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))
