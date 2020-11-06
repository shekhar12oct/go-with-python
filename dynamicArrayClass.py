# Creating a Dynamic Array

import ctypes

class dynamicArray(object):
# Initialising the property of the Array
    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    # Returning length of the array
    def __len___(self):
        return self.n


    # Returning the element at the specific position
    def __getitem__(self,k):
        if not 0 <= k < self.n:
            print("Index out of bound")

        return self.A[k]

    def append(self,ele):
        if self.n == self.capacity:
            # Double capacity if not enough room
            self._resize(2*self.capacity)


        self.A[self.n] = ele
        self.n += 1

    def insertAt(self,item,index):
        if index<0 or index>self.n:
            print("Please enter appropriate index number")
            return

        if self.n == self.capacity:
            self._resize(2*self.capacity)

            for i in range(self.n-1,index-1,-1):
                self.A[i+1] = self.A[i]

        self.A[index] = item
        self.n += 1


    def delete(self):
        if self.n == 0:
            print("Array is empty and  deletion  is not Possible")
            return

        self.A[self.n - 1] = 0
        self.n -= 1


    def removeAt(self, index):

        if self.n == 0:
            print("Array is empty and  deletion is  not Possible")
            return

        if index < 0 or index >= self.n:
            return IndexError("Index out of bound so deletion is not possible")

        if index == self.n - 1:
            self.A[index] = 0
            self.n -= 1
            return

        for i in range(index, self.n - 1):
            self.A[i] = self.A[i + 1]

        self.A[self.n - 1] = 0
        self.n -= 1


    def _resize(self, new_cap):
        B = self.make_array(new_cap)

        # Reference all existing values from array A  into dynamic Array B
        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap


    def make_array(self,new_cap):
        #  Returns a new array with new_cap capacity
        return (new_cap * ctypes.py_object)()