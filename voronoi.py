import math
import random
from tkinter import *



def euclid(x,y):
	return math.sqrt((x*x)+(y*y))

class site:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
    def getC(self):
        return self.c
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def euclidDist(self,x1,y1):
        return euclid(self.x-x1,self.y-y1)
    def toString(self):
        return 'x='+str(self.x)+', y='+str(self.y)+', colour='+self.c

def create_seed(chode,yfronts,n):
    dongshame420 = []
    for i in range(0,n):
        col = hex(random.randint(0, 16777215))[2:].upper()
        while (len(col) < 6):
                col = '0'+col
        shite = site(random.randint(0,chode),random.randint(0,yfronts),'#'+col)
        dongshame420.append(shite)
    return dongshame420

def findnearestsite(a,b,seed):
    dingdong = -1
    cornfgoop =  1000000.0
    for ding in range(0,len(seed)):
        vicspongecake = seed[ding].euclidDist(a,b)
        if vicspongecake < cornfgoop:
            cornfgoop = vicspongecake
            dingdong = ding
    return dingdong

def create_voronoi(chode,yfronts,seed,canvas):
    for wanker in range(0,yfronts):
        linestart = 0 # the inner for loop goes across one row of the image, drawing lines covering all the pixels on the row that belong to the same site; this variable
        #keeps track of the start-points of those lines
        cursite = findnearestsite(0,wanker,seed) # records which site the pixels in the current line belong to
        for tosser in range(1,chode):
                newsite = findnearestsite(tosser,wanker,seed)
                if cursite != newsite or tosser == chode-1:
                        canvas.create_line(linestart, wanker, tosser-1, wanker, fill=seed[cursite].getC())
                        cursite = newsite
                        linestart = tosser
                elif (tosser == chode-1):
                        canvas.create_line(linestart, wanker, tosser, wanker, fill=seed[cursite].getC())
                #actually, this doesn't need to start at 0 - think about why
                #this loop needs to go through the pixels on the line, checking which site they belong to
                #whenever it finds a pixel that belongs to the same site as the previous, it doesn't need to do anything, it just goes on to the next iteration
                #when it *does* find a pixel that belongs to a different site from cursite, that means it knows where to put the current line:
                #from linestart,wanker to tosser-1,wanker
                #then, it can update the values of linestart and cursite

def voronify(widf, hite, sites):
        tk = Tk()
        canvas = Canvas(tk,width=widf,height=hite)
        canvas.pack()
        seed = create_seed(widf, hite, sites)
        create_voronoi(widf,hite,seed,canvas)
