# 1476. Subrectangle Queries

# [
#     "SubrectangleQueries",
#     "getValue",
#     "updateSubrectangle",
#     "getValue",
#     "getValue",
#     "updateSubrectangle",
#     "getValue",
#     "getValue",
# ]

# [[[[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]],
#  [0, 2],
#  [0, 0, 3, 2, 5],
#  [0, 2],
#  [3, 1],
#  [3, 0, 3, 2, 10],
#  [3, 1],
#  [0, 2]]


class SubrectangleQueries:
    def __init__(self, rectangle: list[list[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)


if __name__ == "__main__":
    rectangle = [[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]]
    coords1 = [0, 0, 3, 2, 5]
    obj = SubrectangleQueries(rectangle)
    print(obj.getValue(0, 2))
    obj.updateSubrectangle(*coords1)
    print(obj.getValue(0, 2), obj.getValue(3, 1))
    coords2 = [3, 0, 3, 2, 10]
    obj.updateSubrectangle(*coords2)
    print(obj.getValue(0, 2), obj.getValue(3, 1))
