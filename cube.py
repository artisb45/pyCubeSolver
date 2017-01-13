from termcolor import colored

class Cube(object):
    def __init__(self):
        self.white_side = [['#','#','#'],['#','#','#'],['#','#','#']]
        self.yellow_side = [[colored('#','yellow'),colored('#','yellow'),colored('#','yellow')],
                            [colored('#','yellow'),colored('#','yellow'),colored('#','yellow')],
                            [colored('#','yellow'),colored('#','yellow'),colored('#','yellow')]]
        self.green_side = [[colored('#','green'),colored('#','green'),colored('#','green')],
                           [colored('#','green'),colored('#','green'),colored('#','green')],
                           [colored('#','green'),colored('#','green'),colored('#','green')]]
        self.blue_side = [[colored('#','blue'),colored('#','blue'),colored('#','blue')],
                          [colored('#','blue'),colored('#','blue'),colored('#','blue')],
                          [colored('#','blue'),colored('#','blue'),colored('#','blue')]]
        self.red_side = [[colored('#','red'),colored('#','red'),colored('#','red')],
                         [colored('#','red'),colored('#','red'),colored('#','red')],
                         [colored('#','red'),colored('#','red'),colored('#','red')]]
        self.orange_side = [[colored('#','magenta'),colored('#','magenta'),colored('#','magenta')],
                            [colored('#','magenta'),colored('#','magenta'),colored('#','magenta')],
                            [colored('#','magenta'),colored('#','magenta'),colored('#','magenta')]]

    def __str__(self):
        return """
       - - -
      |"""+self.yellow_side[0][0]+"""|"""+self.yellow_side[0][1]+"""|"""+self.yellow_side[0][2]+"""|
       - - -
      |"""+self.yellow_side[1][0]+"""|"""+self.yellow_side[1][1]+"""|"""+self.yellow_side[1][2]+"""|
       - - -
      |"""+self.yellow_side[2][0]+"""|"""+self.yellow_side[2][1]+"""|"""+self.yellow_side[2][2]+"""|
 - - - - - - - - - - - -
|"""+self.red_side[0][0]+"""|"""+self.red_side[0][1]+"""|"""+self.red_side[0][2]+"""|"""+self.green_side[0][0]+"""|"""+self.green_side[0][1]+"""|"""+self.green_side[0][2]+"""|"""+self.orange_side[0][0]+"""|"""+self.orange_side[0][1]+"""|"""+self.orange_side[0][2]+"""|"""+self.blue_side[0][0]+"""|"""+self.blue_side[0][1]+"""|"""+self.blue_side[0][2]+"""|
 - - - - - - - - - - - -
|"""+self.red_side[1][0]+"""|"""+self.red_side[1][1]+"""|"""+self.red_side[1][2]+"""|"""+self.green_side[1][0]+"""|"""+self.green_side[1][1]+"""|"""+self.green_side[1][2]+"""|"""+self.orange_side[1][0]+"""|"""+self.orange_side[1][1]+"""|"""+self.orange_side[1][2]+"""|"""+self.blue_side[1][0]+"""|"""+self.blue_side[1][1]+"""|"""+self.blue_side[1][2]+"""|
 - - - - - - - - - - - -
|"""+self.red_side[2][0]+"""|"""+self.red_side[2][1]+"""|"""+self.red_side[2][2]+"""|"""+self.green_side[2][0]+"""|"""+self.green_side[2][1]+"""|"""+self.green_side[2][2]+"""|"""+self.orange_side[2][0]+"""|"""+self.orange_side[2][1]+"""|"""+self.orange_side[2][2]+"""|"""+self.blue_side[2][0]+"""|"""+self.blue_side[2][1]+"""|"""+self.blue_side[2][2]+"""|
 - - - - - - - - - - - -
      |"""+self.white_side[0][0]+"""|"""+self.white_side[0][1]+"""|"""+self.white_side[0][2]+"""|
       - - -
      |"""+self.white_side[1][0]+"""|"""+self.white_side[1][1]+"""|"""+self.white_side[1][2]+"""|
       - - -
      |"""+self.white_side[2][0]+"""|"""+self.white_side[2][1]+"""|"""+self.white_side[2][2]+"""|
       - - -"""
    
    def solve(self, formula):
        commands = formula.split()
        for c in commands:
            return
            

c = Cube()
print(c);            