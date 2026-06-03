def calculate_average(numbers):
    try:
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]
        # Logical Error: Incorrect average calculation for empty list
        return total / len(numbers)
    except ZeroDivisionError:
        print("Erorr: Cannot calculate average of an empty list.")
        return None


def get_list_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print(f"Error: Index {index} is out of range for list of length {len(my_list)} ")
        return None
    except TypeError:
        print("Error: First argument must be a list.")
        return None
    



data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = [] # This will cause an error
print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")

my_list = [100, 200, 300]
print(get_list_element(my_list, 1))
print(get_list_element(my_list, 5))
print(get_list_element(100, 1))