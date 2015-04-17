#from dungeon import Dungeon

class Dungeon:

    def __init__(self):
        self.place = [["S",".","#","#",".",".",".",".",".","T"],
                        ["#", "T", "#","#", ".", ".", "#", "#", "#","."],
                        ["#",".","#","#","#","E","#","#","#","E"],
                        ["#",".","E", ".", ".", ".", "#","#","#", "."],
                        ["#","#","#","T", "#","#","#","#","G"]
                        ]

    def __str__(self):
        return "S.##.....T\n#T##..###.\n#.###E###E\n#.E...###.\n###T####G"

    def print_map(self):
        return self.__str__()

m = Dungeon()
print(m.print_map())
