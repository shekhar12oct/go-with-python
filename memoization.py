# Concept of memoization in the python
nums = {}

def fib(n):
    if type(n) != int:
        raise TypeError(" Number is not an integer !")

    if n < 0:
        raise TypeError("Number is a negative number !")
    if n <= 2:
        return 1

    if n in nums:
        return nums[n]
    else:
        num = fib(n-1) + fib(n-2)
        nums[n] = num
        return num


print(fib(599))
