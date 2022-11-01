# EXERCISE ONE
def sum_to(n):
  total = 0
  for i in range(n+1):
    total += i
  return total

# print(sum_to(6))
# print(sum_to(10))

# EXERCISE TWO
def largest(num_list):
  largest_num = 0
  for num in num_list:
    if num > largest_num:
      largest_num = num
  return largest_num

# print(largest([1, 2, 3, 4, 0]))
# print(largest([10, 4, 2, 231, 91, 54]))

# EXERCISE THREE
def occurrences(first_str, second_str):
  return first_str.count(second_str)  

# print(occurrences('fleep floop', 'e'))  # returns 2
# print(occurrences('fleep floop', 'p'))  # returns 2
# print(occurrences('fleep floop', 'ee'))  # returns 1
# print(occurrences('fleep floop', 'fe'))  # returns 0

# EXERCISE FOUR
def product(*args):
  total = 1
  for arg in args:
    total *= arg
  return total

# print(product(-1, 4) )# returns -4
# print(product(2, 5, 5)) # returns 50
# print(product(4, 0.5, 5)) # returns 10.0
