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
