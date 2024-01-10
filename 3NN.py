from math import sqrt
import tkinter as tk

class Pos():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def dist(self,other):
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)
    __repr__=lambda self:f'({self.x}, {self.y})'

    
def nearestat(event):
    pos = Pos(event.x,event.y)
    dists_black = [bpos.dist(pos) for bpos in black]
    dists_blue = [bpos.dist(pos) for bpos in blue]
    dists_blue.sort()
    dists_black.sort()
    orders = []
    for _ in range(3):
        if dists_blue[0]<dists_black[0]:
            dists_blue.pop(0)
            orders.append("blue")
        else:
            dists_black.pop(0)
            orders.append("black")
    result = "black" if orders.count("black") > orders.count("blue") else "blue"
    can.create_rectangle(pos.x-5,pos.y-5,pos.x+5,pos.y+5,fill=result,tags=('jui',),outline="white")
    return result


def grid(event):
    step = 10
    for y in range(0,500+step,step):
        for x in range(0,500+step,step):
            nearestat(Pos(x,y))
            
def circle(posa,ray,coul):
    return can.create_oval(posa.x*10+ray,posa.y*10+ray,
                    posa.x*10-ray,posa.y*10-ray,
                    fill=coul,tags=("mouvable",))
class self():
    _drag_data = {"x": 0, "y": 0, "item": None}

def drag_start(event):
    self._drag_data["item"] = can.find_closest(event.x, event.y)[0]
    self._drag_data["x"] = event.x
    self._drag_data["y"] = event.y

def drag_stop(event):
    for pos in blue+black:
        if pos.tag==self._drag_data["item"]:
            pos.x,pos.y=self._drag_data["x"],self._drag_data["y"]
    self._drag_data["item"] = None
    self._drag_data["x"] = 0
    self._drag_data["y"] = 0

def drag(event):
    delta_x = event.x - self._drag_data["x"]
    delta_y = event.y - self._drag_data["y"]
    can.move(self._drag_data["item"], delta_x, delta_y)
    self._drag_data["x"] = event.x
    self._drag_data["y"] = event.y

def erase(event):
    can.delete("jui")

    
black = [Pos(15,49),Pos(11,18),Pos(9,25)]
blue = [Pos(17,22),Pos(28,20),Pos(19,17)]

f = tk.Tk()
f.title('The 3 Nearest Neighbord')
can = tk.Canvas(f,width=500,height=500)
can.pack()
for posa,posb in zip(black,blue):
    posa.tag = circle(posa,10,"black")
    posb.tag = circle(posb,10,"blue")
can.bind('<Button-2>',lambda event:print(nearestat(event)))
can.tag_bind("mouvable", "<ButtonPress-1>", drag_start)
can.tag_bind("mouvable", "<ButtonRelease-1>", drag_stop)
can.tag_bind("mouvable", "<B1-Motion>", drag)
f.bind('a',grid)
f.bind('e',erase)
input()
    
