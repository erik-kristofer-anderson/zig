### stable version as of 2019-11-24 for easier sharing

class Switch:
    def __init__(self, x=0, y=0, state="A"):
        self.x = x
        self.y = y
        self.state = state

    def __str__(self):
        s = "switch at location {}, {} with state {}.".format(self.x, self.y, self.state)
        return s

    def change_state(self):
        if self.state == "A":
            self.state = "B"
        elif self.state == "B":
            self.state = "A"
        else:
            print("oops, this code should not have executed")


class Explorer:
    """
    class with attributes position (list) and direction (string)
    """

    def __init__(self, x, y, direction="E"):
        self.x = x
        self.y = y
        self.direction = direction

    def __str__(self):
        s = "explorer at position {}, {} facing in direction {}.".format(self.x, self.y, self.direction)
        return s

    def step_explorer(self, switches):
        # self is an explorer

        # turn explorer
        for switch in switches:
            if (self.x, self.y) == (switch.x, switch.y):
                self.turn_explorer(switch)

        # move explorer forward
        if self.direction == "N":
            self.y -= 1
        if self.direction == "E":
            self.x += 1
        if self.direction == "S":
            self.y += 1
        if self.direction == "W":
            self.x -= 1

    def turn_explorer(self, switch):
        if switch.state == "A":
            if self.direction == "W":
                self.direction = "N"
            elif self.direction == "E":
                self.direction = "S"
            elif self.direction == "S":
                self.direction = "E"
            elif self.direction == "N":
                self.direction = "W"
            switch.state = "B"
        elif switch.state == "B":
            if self.direction == "W":
                self.direction = "S"
            elif self.direction == "E":
                self.direction = "N"
            elif self.direction == "S":
                self.direction = "W"
            elif self.direction == "N":
                self.direction = "E"
            switch.state = "A"
        else:
            print("oops, this code shouldn't have executed")

    def test_explorer_in_room(self, height, width):
        if self.x < 0 or self.x > width or self.y < 0 or self.y > height:
            return False
        else:
            return True


def parse_artifact(artifact):
    switches = []
    i, j = 0, 0
    for i, row in enumerate(artifact):
        row = row.replace(" ", "=")
        for j, character in enumerate(row):
            if character in "AB":
                switch = Switch(x=j, y=i, state=character)
                switches.append(switch)
    height, width = i, j
    return switches, height, width


def move_explorer(explorer_row, switches, artifact):
    explorer = Explorer(x=0, y=explorer_row, direction="E")
    in_room = True
    _, height, width = parse_artifact(artifact)
    while in_room:
        # print(explorer)
        for switch in switches:
            # print(switch)
            pass
        explorer.step_explorer(switches)
        in_room = explorer.test_explorer_in_room(height, width)
    # upon exiting while loop, in_room is False
    return explorer.x, explorer.y


def ride_of_fortune(artifact, explorers):

    switches, room_height, room_width = parse_artifact(artifact)

    exit_locations = []
    for explorer_row in explorers:
        x, y = move_explorer(explorer_row, switches, artifact)

        if x < 0:
            exit_location = None
        elif x > room_width or y > room_height or y < room_height:
            if x > room_width:
                x -= 1
            elif y > room_height:
                y -= 1
            elif y < room_height:
                y += 1
            exit_location = [y, x]
             # exit_location = [x, y]
        exit_locations.append(exit_location)
        # print([x, y])
    return exit_locations


# switch = Switch()
# print(switch)
# switch.change_state()
# print(switch)
#
# explorer = Explorer()
# print(explorer)



