class Parser:
    def __init__(self, infile):
        self.inputFileName = infile
        self.data = open(self.inputFileName, 'r')

    def parseNumColumn(self):
        arr = []
        for line in self.data:
            numStr = line.split()
            if len(numStr) > 1:
                print("Not a 1D num column")
                exit()
            if len(numStr) != 0:
                arr.append(int(numStr[0]))

        return arr