class Table:

    length = 25
    width = 30
    height = 15

    def __init__(self):
        self.width = 5

    def chcange_length(self, length):
        self.length = length
        return length

    def chcange_width(self, width):
        self.width = width
        return width

    def chcange_height(self, height):
        self.height = height
        return height

    def times(self, length, width, height):
        self.times = length*width*height
        return self.times
