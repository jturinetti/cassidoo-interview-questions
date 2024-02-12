# Write a function that produces a generator that produces values in a range.

# Example:

# let range = fromTo(0,3)

# > range()
# 0
# > range()
# 1
# > range()
# 2
# > range()
# null

def from_to(f, t):
    r = range(f, t)
    i = iter(r)
    def inner_function():
        try:
            return next(i)
        except StopIteration:
            return        
    return inner_function

begin_value = 0
end_value = 10

from_to_generator = from_to(begin_value, end_value)

for i in range(begin_value, end_value + 5):
    print(from_to_generator())


