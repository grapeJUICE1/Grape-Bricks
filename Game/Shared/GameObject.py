class GameObject:
    def __init__(self , position , size,sprite):
        self.__position = position
        self.__size = size
        self.__sprite = sprite

    def setPosition(self , position):
        self.__position = position

    def getPosition(self):
        return self.__position

    def getSize(self):
        return self.__size

    def getSprite(self):
        return self.__sprite

    def setSprite(self , sprite):
        self.__sprite =  sprite

    def __intersectsY(self, other):
        otherPosition = other.getPosition()
        otherSize = other.getSize()

        if self.__position[1] >= otherPosition[1] and self.__position[1] <= otherPosition[1] + otherSize[1]:
            return 1
        if (self.__position[1] + self.__size[1]) > otherPosition[1] and (self.__position[1] + self.__size[1]) <= (otherPosition[1] + otherSize[1]):
            return 1
        return 0

    def __intersectsX(self, other):
        otherPosition = other.getPosition()
        otherSize = other.getSize()

        if self.__position[0] >= otherPosition[0] and self.__position[0] <= otherPosition[0] + otherSize[0]:
            return 1
        if (self.__position[0] + self.__size[0]) > otherPosition[0] and (self.__position[0] + self.__size[0]) <= (otherPosition[0] + otherSize[0]):
            return 1
        return 0

    def intersects(self, other):
        if self.__intersectsY(other) and self.__intersectsX(other):
            return 1
        return 0

