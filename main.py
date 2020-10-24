import pygame
import threading, queue
import time
#imbunatariri 
#citire din fisier - preluare input de acolo
#optimizare

def OpenWindow(width_size,height_size):
    (width, height) = (width_size, height_size)
    screen = pygame.display.set_mode( (width, height) )
    pygame.display.flip()
    return screen

#-------------------------------Maze related essential functions---------------------------------
def Generate_Maze(rows,file):
    #maze = [[1,0,0,1,1] , [1,1,1,0,0] , [0,0,1,1,1] , [1,0,0,0,1] , [1,1,1,1,1] ]
    maze = []
    #procces the maze 
    for i in range(0,rows):
        line = file.readline().split()
        maze_line = list(map(int, line)) 
        maze.append(maze_line)
    return maze 

def Draw_Maze(maze , screen , rows, colums , position):
    for i in range(0,rows):
        for j in range(0,colums):
            if maze[i][j] >= 1:
                pygame.draw.rect(screen,(220,20,60),(j*50,i*50, 40,40))
            elif maze[i][j] == 0: 
                pygame.draw.rect(screen,(255,255,255),(j*50,i*50, 40,40))
            elif maze[i][j] == -1: 
                pygame.draw.rect(screen,(0,0,255),(j*50,i*50, 40,40))

#-------------------------------Lee's algorithm essential functions------------------------------
#return true if the player is able to walk on this position 
def IsOk(position , maze , rows, colums):
    if position[0] < 0 or position[0] >= rows or position[1] < 0 or position[1] >= colums:#it is out of bounds
        return False
    if maze[position[0]][position[1]] == -1:#it is a wall here
        return False
    if maze[position[0]][position[1]] > 1:#it has already been here
        return False
    return True

def Lee(maze , screen , start, end , rows , colums):
    di = [-1,0,+1,0] #array for line direction N,E,S,V
    dj = [0,+1,0,-1] #array for column direction N,E,S,V 
    positions = queue.Queue() #the queue which will store the next positions where the player will go 
    positions.put(start) # firstly we insert the start position in the queue
    while positions.empty()==False:
        current_position = positions.get()
        if current_position[0] == end[0] and current_position[1] == end[1]:
            break
        for i in range(0,4):
            next_line = current_position[0] + di[i]
            next_column = current_position[1] + dj[i]
            if IsOk( (next_line,next_column) ,maze, rows,colums ):
                positions.put( (next_line,next_column) )
                maze[next_line][next_column] = maze[current_position[0]][current_position[1]] + 1
        Draw_Maze(maze,screen,rows,colums,current_position)
        pygame.display.update()
        time.sleep(0.25)
    
    font = pygame.font.Font('freesansbold.ttf', 32) 
    text = font.render('GeeksForGeeks', True, (255,255,255)) 
    screen.blit(text,(300,200)) 

    print(maze[end[0]][end[1]])
    time.sleep(2)


def main(): 
    #Local variables
    pygame.init()
    window = OpenWindow(500,500)
    #get number of rows and number of colums and start position and end position from the first line 
    fin = open("input.txt","r")
    first_line = fin.readline().split(" ")
    rows = int(first_line[0])
    colums = int(first_line[1])
    start = ( int(first_line[2]) , int(first_line[3]) )
    end = ( int(first_line[4]) , int(first_line[5]) )
    maze = Generate_Maze(rows,fin)
    print(maze)
    Lee(maze,window,start,end,rows,colums)
 
main()
