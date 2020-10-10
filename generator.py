#! python
# Generators
def square_numbers(nums):
    for i in nums:
        yield i * i # yield is used to return generators


my_nums = square_numbers([1, 2, 3, 4, 5])

# my_nums as a list comprehension
# my_nums = [x * x for x in [1, 2, 3, 4, 5]]

# my_nums as a generator
# my_nums = (x * x for x in [1, 2, 3, 4, 5])

print(my_nums)

for num in my_nums:
    print(num)