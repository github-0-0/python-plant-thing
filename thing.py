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
  if random.random()<0.5:
    return random.randint(0,8)
  else:
    return random.randint(8,lastdefindex+8)
def define():
  a = []
  b = random.randint(0,20)
  a.append([0,1,randomcelltype(b),randomcelltype(b)])
  random.shuffle(a)
  for i in range(b-1):
    a.append([randomcelltype(b) for i in range(4)])
  return a
def mutate(plant,mrate1,mrate2,mrate3):
  plantdef=plant["def"]
  if random.random()<mrate1:
    for i in range(len(plant["def"])):
      if random.random()<mrate2:
        b=len(plant["def"])
        plantdef[i]=[randomcelltype(b) for i in range(4)]
  if random.random()<mrate3:
    plantdef.append([randomcelltype(b) for i in range(4)])
  return plantdef
def newplant(id):
  return {
    "def":define(),
    "id":id,
    "throwlength":random.randint(0,100)
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
          vgrid[i][j]
          if lneighbors[self["direction"]]["id"]==-1:
            vgrid[neighbors(i,j)[self("direction")][0]][neighbors(i,j)[self("direction")][1]]=self
            vgrid[i][j]["type"]=-1
            vgrid[i][j]["id"]=-1
            vgrid[i][j]["rootx"]=-1
            vgrid[i][j]["rooty"]=-1
          
        
        
        
        
          
        
        















      
  
