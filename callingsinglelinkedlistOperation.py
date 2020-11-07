from singlelinkedlistOperation import *


a = node(5)
b = node(7)
c = node(9)

a.nextNode = b
b.nextNode = c


print(a.value)
print(a.nextNode.value)
print(b.value)
print(b.nextNode.value)
print(c.value)