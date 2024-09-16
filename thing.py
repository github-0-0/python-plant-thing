import random
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
  c = 8 + len(b)
  for i in range(8):
    a.append(i)
  for i in range():
    a.append([randomcelltype(c) for i in range(4)])
  return a
def plant(id):
  return {
    "def":define(),
    "id":id
  }
plantlist=[]
population = 500
for i in range(population):
  plantlist.append(plant(i))
def deathcondition(cell):
  if cell["water"]<=0 or cell["energy"]<=0 or grid[rootx][rooty]["id"]== -1:
    return True
  else:
    return False
def updategrid():
  vgrid = grid
  for i in range(height):
    for j in range(width):
















      
  
