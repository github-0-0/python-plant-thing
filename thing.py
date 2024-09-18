import random
grid=[]
width=100
height=100
plantlist=[]
population=500
def tile(type,id,water,energy,direction,rootx,rooty):
  return {
    "type":type,
    "id":id,
    "water":water,
    "energy":energy,
    "direction":direction,
    "rootx":rootx,
    "rooty":rooty
  }
grid = []
def creategrid(width,height):
  for i in range(height):
    grid.append([])
    for j in range(width):
      grid[i].append(tile(-1,-1,10,0,0))
def randomcelltype(lastdefindex):
  if random.randint(0,99)<50:
    return random.randint(0,7)
  else:
    return random.randint(8,lastdefindex)
def define():
  a = []
  b = random.randint(0,20)
  c = 8 + b
  for i in range(8):
    a.append(i)
  a.append([0,1,randomcelltype(c),randomcelltype(c)])
  random.shuffle(a)
  for i in range(b-1):
    a.append([randomcelltype(c) for i in range(4)])
  return a
def mutate(plant,mrate1,mrate2):
  plantdef=plant["def"]
  if(
def newplant(id):
  return {
    "def":define(),
    "id":id
  }
for i in range(population):
  plantlist.append(newplant(i))
def deathcondition(cell):
  if cell["water"]<=0 or cell["energy"]<=0 or grid[cell["rootx"]][cell["rooty"]]["id"]== -1:
    return True
  else:
    return False
def wrap(x,n):
  return (x+n)%n
def neighbors(x,y):
  return [[wrap(x-1,height),y],[x,wrap(y+1,width)],[wrap(x+1,height),y],[x,wrap(y-1,width)]]
def updategrid():
  vgrid = grid
  for i in range(height):
    for j in range(width):
      self=grid[i][j]
      if deathcondition(self):
        vgrid[i][j]["type"]=-1
        vgrid[i][j]["id"]=-1
        vgrid[i][j]["rootx"]=-1
        vgrid[i][j]["rooty"]=-1
      else:
        lneighbors=[]
        for pos in neighbor(i,j):
          lneighbors.append(grid[pos[0]][pos[1]])
        if self["cell"] == 0:
          
          a=0
          for k in range(4):
            neighbor=lneighbors[k]
            if(neighbor["id"]==self["id"]):
              a+=1
            else:
              lneighbors.pop(k)
          b=0
          c=0
          for neighbor in lneighbors:
            b+=neighbor["water"]
            c+=neighbor["energy"]
          b+=self["water"]
          b/=1+len(lneighbors)
          c+=neighbor["energy"]
          c/=1+len(lneighbors)
          for pos in neighbors(i,j):
            vgrid[pos[0]][pos[1]]["water"]=b
            vgrid[pos[0]][pos[1]]["energy"]=c
        elif self["cell"]==1:
          
        
        
        
        
          
        
        















      
  
