import hashlib
import fileinput
import operator

class Highscore:

    def __init__(self):
        self.__highscore = self.load()

    def getScores(self):
        return self.__highscore

    def load(self):
        highscore = []
        for line in fileinput.input("highscore.dat"):
            name, score, md5 = line.split('[::]')
            md5 = md5.replace('\n', '')

            if str(hashlib.md5(str.encode(str(name+score+"pygame"))).hexdigest()) == str(md5):
                highscore.append([str(name), int(score), str(md5)])

        highscore.sort(key=operator.itemgetter(1), reverse=True)
        highscore = highscore[0:11]

        return highscore

    def add(self, name, score):
        hash = hashlib.md5((str(name+str(score)+"pygame")).encode('utf-8'))
        self.__highscore.append([name, str(score), hash.hexdigest()])

        f = open("highscore.dat", 'w')
        for name, score, md5 in self.__highscore:
            f.write(str(name)+"[::]"+str(score)+"[::]"+str(md5)+"\n")

        f.close()
