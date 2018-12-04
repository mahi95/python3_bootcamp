import sys
import math

# Normal function
def square(num):
    return num * num

print(square(7))

# lambda function
square2 = lambda num: num*num
print(square2(8))

print(square.__name__)
print(square2.__name__)

# Basic Exercise
cube = lambda num: num**3  # never assign a lambda function to a variable
print(cube(3))

# Map function
nums = [2, 4, 6, 8, 10]
doubles = list(map(lambda x: x*2, nums))
doubles_1 = [x*2 for x in nums]
print(doubles)
print(doubles_1)

people = ['Ajmal', 'Maha', 'Pathma', 'Ismail']
peeps = list(map(lambda x: x.upper(), people))
print(peeps)

# Map Exercise
decrement_list = [[1, 2, 3], [20, 14, 11]]
out_dec_list = [map(lambda x: x-1, l) for l in decrement_list]
print(out_dec_list)

# Filter Exercise
l = [1, 2, 3, 4]
evens = filter(lambda x: x % 2 == 0, l)
print(evens)

twit_dict = [
    {'user_name': 'Maha', 'tweets': ['Not good', 'bad']},
    {'user_name': 'Pathma', 'tweets': ['Bad']},
    {'user_name': 'Ismail', 'tweets': []},
    {'user_name': 'Ajmal', 'tweets': []}
]
inactive_users = filter(lambda u: not u['tweets'], twit_dict)
print([l['user_name'] for l in inactive_users])

# combining map and filter
inactive_users_1 = list(map(lambda x: x['user_name'],
                            filter(lambda u: not u['tweets'], twit_dict)))
print(inactive_users_1)

# Filter exercise
num = [-1, 3, -45, 9]
non_negative = filter(lambda x: x > 0, num)
print(non_negative)

# Built in functions(any and all) any is like AND & all is like OR
char = all([char for char in "eio" if char in "aeiou"])
print(char)
num = [4, 2, 6, 8]
num_1 = all(filter(lambda x: x % 2 == 0, num))
print(num_1)
num.append(21)

num_2 = any([even_num % 2 == 0 for even_num in num])
print(num_2)

# any using lambda expression
num_3 = [21, 3, 5]
print(any(filter(lambda x: x % 2 == 0, num_3)))

# Generator expression and getsizeof()
len_list = sys.getsizeof([num for num in [1, 4, 6, 8] if num % 2 == 0])
gen_list = sys.getsizeof(num for num in [1, 4, 6, 8] if num % 2 == 0)

print("length of list comp {} bytes".format(len_list))
print("length of gen expression {} bytes".format(gen_list))

print(all([num % 2 == 0 for num in [1, 4, 6, 8]]))
print(any(num % 2 == 0 for num in [1, 4, 6, 8]))

# Sorted function
num_s = [1, 2, 3, 4, 5]
print(sorted(num_s, reverse=True))
user_s = [
    {'user_name': 'Maha', 'tweets': ['Not good', 'bad']},
    {'user_name': 'Pathma', 'tweets': ['Bad']},
    {'user_name': 'Ismail', 'tweets': []},
    {'user_name': 'Ajmal', 'tweets': []}
]
print(sorted(user_s, key=lambda x: x['user_name'], reverse=True))

# Min and Max functions
print('Min value is : {}'.format(min(4, 5, 6)))
print('Max value is : {}'.format(max(4, 5, 6)))

names = ['Anand', 'Maha', 'Pathma', 'Ajmal']
print('Biggest name is : {}'.format(max(names, key=lambda x: len(x))))
print('Shortest name is : {}'.format(min(names, key=lambda x: len(x))))

spottify_dict = [
    {'name': 'Happy Birthday', 'playcount': 20},
    {'name': 'Survive', 'playcount': 120},
    {'name': 'Toxic', 'playcount': 280},
    {'name': 'Halo', 'playcount': 210},
]
print('Most time played album: {}'.format(max(spottify_dict,
                                              key=lambda x: x['playcount'])['name']))
print('Most time played album: {}'.format(min(spottify_dict,
                                              key=lambda x: x['playcount'])['name']))

# Reversed function:
nums = [1, 2, 3, 4]
print(nums.reverse())
print(list(reversed(nums)))

print("hello"[::-1])
print(list(reversed("Hello")))
print("".join(list(reversed("Hello"))))

for x in reversed(range(0, 10)):
    print(x)

# Len function

print("Length of the list is : {}".format(len([1, 2, 3, 4])))
print("Length of the character is: {}".format(len('asdasa')))
print('Length of the dictionary is : {}'.format(len({'a': 10, 'b': 100})))

# Length will call the __len__ function in each object
# when the function len(object) is called
print("Call using __len__ function : {}".format("hello".__len__()))
print("List length using __len__func: {}".format([1, 2, 3].__len__()))

# abs, sum and round
print('Absolute value of -43 : {}'.format(abs(-43)))
print('Absolute value of 3.444: {}'.format(abs(3.444)))
print('Abolute value of -3.444: {}'.format(abs(-3.444)))
print('Abolute value of float abs 4: {}'.format(math.fabs(4)))
print('Abolute value of float abs -5.6: {}'.format(math.fabs(-5.6)))
print('\n_________SUM___________\n')
print('Sum of the numbers in the list: {}'.format(sum([1, 2, 3])))
print('Sum of the numbers in the list([1, 2, 3],6): {}'.
      format(sum([1, 2, 3], 6)))
print('Sum of the numbers in the list([1, 2, 3], -6): {}'.
      format(sum([1, 2, 3], -6)))

print('\n_________ROUND___________\n')
print('Rounded number of 3.51234: {}'.format(round(3.51235, 2)))

print('\n_________BUILT-IN FUNCTIONS Exercise___________\n')
print('Maximum magnitude is : {}'.
      format(max(map(lambda x: abs(x), [300, 20, -900]))))

# Zip function
nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7, 8]
print('\n_________ZIP___________\n')
print('Zipped list is: {}'.format(list(zip(nums1, nums2))))
print('Zipped dict is: {}'.format(dict(zip(nums1, nums2))))
words = ['Hi', 'Hello', 'Welcome', 'Greetings']
print('Zipping three lists: {}'.format(list(zip(words, nums1, nums2))))
five_by_two = [(1, 5), (2, 6), (3, 7), (4, 8)]
print('Unpacking the list: {}'.format(list(zip(*five_by_two))))

# Complex zip functions
print('\n_________Complex ZIP functions___________\n')
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['Anand', 'Pathma', 'Ismail']
print('Maximum pair: {}'.format([max(pair) for pair in zip(midterms, finals)]))
final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
print('Final grades using dict comprehension: {}'.format(final_grades))
print('Final grades using map, lambda, zip: {}'.format(
    dict(zip(students, map(lambda x: max(x), zip(midterms, finals))))))

# Zip Exercise
print('\n_________ZIP exercises___________\n')
def interleave(n1, n2):
    print(''.join(''.join(x) for x in zip(n1, n2)))
interleave('hi', 'no')
