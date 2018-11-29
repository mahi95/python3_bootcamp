# Basic example

numbers = [1, 2, 3, 4, 5]
doubled_numbers = [x*10 for x in numbers]
print(doubled_numbers)

char = 'colt'
print([each_char.upper() for each_char in char])

friends = ['ashley', 'anand', 'maha']
print([friend.upper() for friend in friends])

string_list = [str(num) for num in numbers]
print(string_list)

string_char_list = [char + "HELLO" for char in string_list]
print(string_char_list)

evens = [num for num in numbers if num % 2 == 0]
print(evens)

odds = [num for num in numbers if num % 2 != 0]
print(odds)

even_odd = [num*2 if num % 2 == 0 else num/2 for num in numbers]
print(even_odd)

with_vowels = 'This is so much fun'
print(''.join(char for char in with_vowels if char not in "aeiou"))

names = ["Elie", "Tim", "Matt"]
reverse_names = [name[::-1].lower() for name in names]
print(reverse_names)

num_by_twelve = [num for num in range(1, 101) if num % 12 == 0]
print(num_by_twelve)

# Nested list
nested_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
[[print(i) for i in val] for val in nested_list]

board = [[num for num in range(1, 4)] for val in range(1, 4)]
print(board)

tic_toe = [["X" if num % 2 != 0 else "O" for num in range(1, 4)]
           for val in range(1, 4)]
print(tic_toe)

# Exercise
answer = [[num for num in range(0, 3)] for val in range(0, 3)]
answer_2 = [[num for num in range(0, 10)] for val in range(0, 10)]