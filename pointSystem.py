class PointSystem:
    def __init__(self):
        self.points = 0
        self.otherPoints = 0

    def addPointSelf (self):
        self.points += 1

    def addPointsOther (self):
        self.otherPoints += 1

    def isWin(self):
        if (self.points == 7 or self.otherPoints == 7):
            return True
        
