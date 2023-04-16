import os


class TXT:
    def __init__(self, inputFile):
        self.inputFile = inputFile

    def getSeq(self):
        with open(self.inputFile, "r") as file:
            if os.stat(self.inputFile).st_size == 0:
                return None
            lines = file.read().split("\n")
            return [line for line in lines if line != '']

