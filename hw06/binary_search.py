class BinarySearch:
    def __init__(self, array, number):
        self.array = array
        self.number = number
        self.left = 0
        self.right = len(array)
        self.middle = (self.left + self.right) // 2

    def search(self):
        while self.left <= self.right:
            self.middle = (self.left + self.right) // 2

            if self.array[self.middle] == self.number:
                return self.middle
            elif self.array[self.middle] < self.number:
                self.left = self.middle + 1
            else:
                self.right = self.middle - 1

        return -1


array = [1, 2, 3, 5, 7, 9, 11, 13]
number = 13

print(BinarySearch(array, number).search())
