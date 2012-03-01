def showmap(self):
    guess = self.locate()

    # set cell colours
    mycell = colorama.Style.BRIGHT + colorama.Fore.WHITE + colorama.Back.RED
    normalcell = colorama.Style.DIM + colorama.Fore.WHITE
    normalcell += colorama.Back.BLACK

    # build location list
    if len(guess['guess']) == guess['cells']:
        guess = []
    else:
        guess = [(i, j) for p, j, i in guess['guess']]

    # make pretty map
    mapstr = normalcell
    for j in range(len(self.world)):
        for i in range(len(self.world[j])):
            if (i, j) in guess:
                mapstr += mycell
                mapstr += str(self.world[j][i]).center(10)
                mapstr += normalcell
            else:
                mapstr += str(self.world[j][i]).center(10)
        mapstr += '\n'
    print mapstr
