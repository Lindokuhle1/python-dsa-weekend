#Task 1: Simple Telemetry Processing

voltage = [3.3, 3.2, 3.1, 3.0, 2.9]
def cal_minum(voltage):
    min_voltage = min(voltage)
    print("Minimum voltage:", min_voltage)

print("Task 1: Minimum Voltage")
cal_minum(voltage)

#max voltage
def cal_max(voltage):
    max_voltage = max(voltage)
    print("Maximum Voltage:", max_voltage)
print("Task 1: Maximum Voltage")
cal_max(voltage)

def cal_avg(voltage):
    voltage.sort()
    avg = sum(voltage) / len(voltage)
    print("Average Voltage:", avg)
print("Task 1: Average Voltage")
cal_avg(voltage)

def print_above_average(voltage):
    avg = sum(voltage) / len(voltage)
    above_avg = 0
    for v in voltage:
        if v > avg:
            above_avg += 1
    print("Number of voltage readings above average:", above_avg)

print("Task 1: Voltage Readings Above Average")
print_above_average(voltage)

#Task 2 Reverse and Palindrom checker

battery_serail = input("entery battery serail: ")
battery_serail = battery_serail.lower()
def reverse_string(battery_serail):
    reversed_string = battery_serail[::-1]
    if battery_serail == reversed_string:
        print("The battery serial is a palindrome.")
    else:
        print("Reversed Battery Serial:", reversed_string)
print("Task 2: Reverse Battery Serial")
reverse_string(battery_serail)

#Task 3 - mini Stack List

class Stack:
    items = [50, 31, 21, 28, 72, 41, 73, 93, 68, 43, 45, 78, 5, 17, 97, 71, 69, 61, 88, 75, 99, 44, 55, 9]
def push(item):
    Stack.items.append(item)
    print("Pushed item:", item)
push(10)
print("Current Stack:", Stack.items)

def pop_item():
    if Stack.items:
        popped_item = Stack.items.pop()
        print("Popped item:", popped_item)
        return popped_item
    else:
        print("Stack is empty. Cannot pop item.")
print(pop_item())
print("Current Stack:", Stack.items)

def peek():
    if Stack.items:
        top_item = Stack.items[-1]
        print("Top item:", top_item)
        return top_item
    else:
        print("Stack is empty. No items to peek.")

print(peek())

def is_empty():
    if len(Stack.items) == 0:
        print("Stack is empty.")
    else:
        print(f"Stack is not empty. it has {len(Stack.items)} items.")
        for i in Stack.items:
            print (i)

is_empty()
