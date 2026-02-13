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
    print("Reversed Battery Serial:", reversed_string)
print("Task 2: Reverse Battery Serial")
reverse_string(battery_serail)
