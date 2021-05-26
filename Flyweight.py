class Lamp:
    def __init__(self, color):
        self.color = color


class LampFactory:
    lamps = {}

    def get_lamp(color):
        return LampFactory.lamps.setdefault(color, Lamp(color))


class TreeBranch:
    def __init__(self, branch_number):
        self.branch_number = branch_number

    def hang(self, lamp):
        print("Поверешно {} [{}] светильник на ветку {} [{}]".format(lamp.color, id(lamp), self.branch_number, id(self)))


class ChristmasTree:
    def __init__(self):
        self.lamps_hung = 0
        self.branches = {}

    def get_branch(self, number):
        return self.branches.setdefault(number, TreeBranch(number))

    def dress_up_the_tree(self):
        self.hang_lamp('красный', 1)
        self.hang_lamp('голубой', 1)
        self.hang_lamp('желтый', 1)
        self.hang_lamp('красный', 2)
        self.hang_lamp('голубой', 2)
        self.hang_lamp('желтый', 2)
        self.hang_lamp('красный', 3)
        self.hang_lamp('голубой', 3)
        self.hang_lamp('желтый', 3)
        self.hang_lamp('красный', 4)
        self.hang_lamp('голубой', 4)
        self.hang_lamp('желтый', 4)
        self.hang_lamp('красный', 5)
        self.hang_lamp('голубой', 5)
        self.hang_lamp('желтый', 5)
        self.hang_lamp('красный', 6)
        self.hang_lamp('голубой', 6)
        self.hang_lamp('желтый', 6)
        self.hang_lamp('красный', 7)
        self.hang_lamp('голубой', 7)
        self.hang_lamp('желтый', 7)

    def hang_lamp(self, color, branch_number):
        self.get_branch(branch_number).hang(LampFactory.get_lamp(color))
        self.lamps_hung += 1


ChristmasTree().dress_up_the_tree()