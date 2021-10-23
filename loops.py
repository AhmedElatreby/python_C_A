# For Loops: Using Range
promise = "I will finish the python loops module!"
for i in range(5):
    print(promise)
print("=========================")

# using While loop
countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("We have liftoff!")

print("=========================")

python_topics = ["variables", "control flow", "loops", "modules", "classes"]
length = len(python_topics)
index = 0

while index < length:
    print("I am learning about " + python_topics[index])
    index += 1
print("=========================")
# Using if with for loop
dog_breeds_available_for_adoption = [
    "french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        break

print("They have the dog I want!")


print("=========================")
# Nested Loop
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0
for location in sales_data:
    print(location)
    for element in location:
        scoops_sold += element
print(scoops_sold)
