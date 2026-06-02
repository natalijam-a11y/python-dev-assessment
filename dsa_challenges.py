

def filter_and_sort_evens(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    even_numbers.sort()
    return even_numbers



def count_character_frequency(text):
    frequency = {}
    for char in text:
        char_lower = char.lower()

        if char_lower in frequency:
            frequency[char_lower] += 1
        else:
            frequency[char_lower] = 1

    return frequency



# --- TEST CASES---
if __name__ == "__main__":
    
    even_numbers = [3, 1, 4, 7, 1, 5, 9, 2, 6, 8]
    print(filter_and_sort_evens(even_numbers))

    text = "This my task for Basic Data Structures & Algorithms"
    print(count_character_frequency(text))