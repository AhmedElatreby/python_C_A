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
