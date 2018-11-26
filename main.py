import random
import pyglet


chunkWidth = 640//32
chunkHeight = 480//32

birthLimit = 5
deathLimit = 5

numberOfSteps = 6



def init_grid(chance, chunk):
    for i in range(0, chunkHeight):
        for j in range(0, chunkWidth):
            bet = random.uniform(0,1)
            if(bet < chance):
               chunk[i][j] = 1   
        
def count(chunk, x, y):
    c = 0
    for i in range(-1, 2):
        for  j in range(-1, 2):
            nx = x+j
            ny = y+i

            if(nx < 0 or ny < 0 or nx >= chunkWidth or ny >= chunkHeight):
                c+=1
            elif(chunk[ny][nx]):
                c+=1
    return c
def tick(chunk):
    newChunk = []
    for i in range(0, chunkHeight):
        lst = list()
        for j in range(0, chunkWidth):
            lst.append(0)
        newChunk.append(lst)

    for i in range(0, chunkHeight):
        for j in range(0, chunkWidth):
            alive = count(chunk, j, i)
            if(chunk[i][j]):
                if alive < deathLimit:
                    newChunk[i][j] = 0
                else:
                    newChunk[i][j] = 1
            else:
                if alive > birthLimit:
                    newChunk[i][j] = 1
                else:
                    newChunk[i][j] = 0
    return newChunk
 
window = pyglet.window.Window(caption = 'Dungeon Generator')

pyglet.resource.path = ['res']
pyglet.resource.reindex()

block_image = pyglet.resource.image('block.png')



chunk = []
for i in range(0, chunkHeight):
    lst = list()
    for j in range(0, chunkWidth):
        lst.append(0)
    chunk.append(lst)

    
sprites = list()


init_grid(0.5, chunk)
for i in range(0, numberOfSteps):
    chunk = tick(chunk)

for i in range(0, chunkHeight):
    for j in range(0, chunkWidth):
          if(chunk[i][j] == 1):
              sprites.append(pyglet.sprite.Sprite(img=block_image, x=j*32, y=i*32))


@window.event
def on_draw():
     for s in sprites:
         s.draw()
pyglet.app.run()
