import copy
from os import urandom

class Game():
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.history = ""
    def play (self, position):
        if (position<0) or (position>8):
            return False
        player = 0
        if self.history=="":
            player=1
        else:
             lastPlayer = self.board[int(self.history [len(self.history)-1])]
             if lastPlayer==1:
                 player=2
             else:
                 player=1
        if self.board[position]!=0:
            return False
        self.board[position]=player
        self.history=self.history+str(position)
        return True
    def copy (self):
        other = Game()
        other.board=copy.copy(self.board)
        other.history=copy.copy(self.history)
        return other
    def winner (self):
        if self.board[0]!=0:
            if (self.board[0]==self.board[1]) and (self.board[0]==self.board[2]):
                return self.board[0]
            if (self.board[0]==self.board[3]) and (self.board[0]==self.board[6]):
                return self.board[0]
            if (self.board[0]==self.board[4]) and (self.board[0]==self.board[8]):
                return self.board[0]
        if self.board[1]!=0:
            if (self.board[1]==self.board[4]) and (self.board[1]==self.board[7]):
                return self.board[1]
        if self.board[2]!=0:
            if (self.board[2]==self.board[5]) and (self.board[2]==self.board[8]):
                return self.board[2]
        if self.board[3]!=0:
            if (self.board[3]==self.board[4]) and (self.board[3]==self.board[5]):
                return self.board[3]
        if self.board[6]!=0:
            if (self.board[6]==self.board[7]) and (self.board[6]==self.board[8]):
                return self.board[6]
            if (self.board[6]==self.board[4]) and (self.board[6]==self.board[2]):
                return self.board[6]
        return 0
    def ended(self):
        if (self.winner()!=0) or (len(self.history)>8):
            return True
        return False
    def __str__ (self):
        return str(self.board[0])+"|"+str(self.board[1])+"|"+str(self.board[2])+"\n"+str(self.board[3])+"|"+str(self.board[4])+"|"+str(self.board[5])+"\n"+str(self.board[6])+"|"+str(self.board[7])+"|"+str(self.board[8])
    def randomPlay (self):
        while self.ended()==False:
            self.play (int(urandom(1)[0])%9)
    def almost3 (self, a, b, c):
        if self.board[a]!=0:
            if self.board[a]==self.board[b]:
                if self.board[c]==0:
                    return c
            if self.board[a]==self.board[c]:
                if self.board[b]==0:
                    return b
        if self.board[b]!=0:
            if self.board[b]==self.board[c]:
                if self.board[a]==0:
                    return a
        return -1
    def almost(self):
        i = self.almost3(0,1,2)
        if i!=-1:
            return i
        i = self.almost3(0,4,8)
        if i!=-1:
            return i
        i = self.almost3(3,4,5)
        if i!=-1:
            return i
        i = self.almost3(6,7,8)
        if i!=-1:
            return i
        i = self.almost3(0,3,6)
        if i!=-1:
            return i
        i = self.almost3(6,4,2)
        if i!=-1:
            return i
        i = self.almost3(1,4,7)
        if i!=-1:
            return i
        return self.almost3(2,5,8)

game = Game()
print (game)
c = input ("Type f to be the first or s to be the second: ")
if c=='f':
    position = int (input ("Type the index of the position you want to play: "))
    if (position<0) or (position>8):
        print ("Invalid position.")
        exit()
    game.play(position)
    print (game)
elif c!='s':
    print ("Invalid option.")
    exit()
while (False==game.ended()):
    alm = game.almost()
    if alm!=-1:
        game.play(alm)
    else:
        statistics = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ti = 0
        ntries = 10000
        while ti<ntries:
            g = game.copy()
            computerPlayed = False
            while computerPlayed==False:
                position = int(urandom(1)[0])%9
                computerPlayed = g.play(position)
            g.randomPlay()
            gw = g.winner()
            ginc = 0
            if gw==1:
                if c=='f':
                    ginc = -1
                else:
                    ginc = 1
            elif gw==2:
                if c=='f':
                    ginc = 1
                else:
                    ginc = -1
            statistics[position] = statistics[position]+ginc
            ti = ti+1
        bestIndex = 9
        bestValue = -ntries
        si = 0
        while si<9:
            print (str(si)+": "+str(statistics[si]))
            if (game.board[si]==0) and (statistics[si]>=bestValue):
                bestValue = statistics[si]
                bestIndex = si
            si = si+1
        if game.play(bestIndex)==False:
            print ("I desist.")
            exit()
    print (game)
    if game.ended():
        break
    userPlayed = False
    while (userPlayed==False):
        position = int (input("Type the index of the position you want to play: "))
        userPlayed = game.play(position)
        print (game)
w = game.winner()
if 0==w:
    print ("The game ended in a draw.")
elif ((w==1) and (c=='f')) or ((w==2) and (c=='s')):
    print ("You won.")
else:
    print ("You lost.")
