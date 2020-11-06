from dequeOperation import *

d = dequeOperation()

d.addFront(5)
d.addRear(6)

# Printing front element
print(d.items[len(d.items)-1])

# Printing rear element
print(d.items[0])

# Size of deque
print(d.sizeof())

# Checking whether the deque is empty or not
print(d.isEmpty())