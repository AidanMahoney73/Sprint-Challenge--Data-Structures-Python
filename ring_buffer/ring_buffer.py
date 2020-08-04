class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        #* iterate through list to decrease the history value by one
        #* append data to list
            #* append to the end of the list if list not full
            #* if list full replace item with history 0

        for element in self.data:
            element[1] -= 1

        if len(self.data) < self.capacity:
            self.data.append([item, self.capacity])
        else:
            for element in range(len(self.data)):
                if self.data[element][1] == 0:
                    self.data[element] = [item, self.capacity]

    def get(self):
        return [element[0] for element in self.data]

    def test(self):
        return self.data


# buffer = RingBuffer(3)

# buffer.get()   #* should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   #* should return ['a', 'b', 'c']

# #* 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   #* should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   #* should return ['d', 'e', 'f']
if __name__ == "__main__":
    #* Test One
    capacity = 5
    buffer = RingBuffer(capacity)
    assert buffer.capacity == capacity

    #* Test Two
    buffer.append('a')
    assert buffer.get() == ['a']

    #! Test Three
    buffer.append('a')
    buffer.append('b')
    buffer.append('c')
    buffer.append('d')
    print("===========start==========")
    print(buffer.test())
    print(buffer.get())
    buffer.append('e')
    print(buffer.test())
    print(buffer.get())
    print("===========end============")