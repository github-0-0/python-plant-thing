import random
def tile(type,id,water,energy,direction):
  return {
    "type":type,
    "id":id,
    "water":water,
    "energy":energy,
    "direction":direction
  }
grid = []
def creategrid(width,height):
  for i in range(height):
    grid.append([])
    for j in range(width):
      grid[i].append(tile(-1,-1,10,0,0))
def plant():
  
  
