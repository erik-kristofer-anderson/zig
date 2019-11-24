class Switch:
    def __init__(self, x=0, y=0, state="A"):
        self.x = x
        self.y = y
        self.state = state

    def __str__(self):
        s = "Switch at location {}, {} with state {}.".format(self.x, self.y, self.state)
        return s

class Explorer:
    def __init__(self, x=0, y=0, direction=):
