import random
import curses
# make object of class initscr()
screen = curses.initscr()
# hide the curse
curses.curs_set(0)
# get the height and width
height,width = screen.getmaxyx()
# set the window
window = curses.newwin(height,width,0,0)
# make the keyboard is ready to recevice staff
window.keypad(1)
# method for delay
window.timeout(100)
# determine the snake
y = height //2
x = width // 4
snake = [
              [y,x] # that for head
              [y,x -1 ] # that for body
              [y,x -2 ] # that for tail
]
food = [height // 2, width // 2]
window.addch(food[0],food[1],curses.ACS_PI)
move_snake = curses.KEY_RIGHT
while True :
              next_move = window.getch()
              key = key if next_move == -1 else next_move
              new_head = [snake[0][0],snake[0][1]]
              if key == curses.KEY_UP:
                      new_head[0]-1
              elif key == curses.KEY_DOWN:
                      new_head[0]+1
              elif key == curses.KEY_RIGHT:
                      new_head[1]+1
              elif key == curses.KEY_LEFT:
                      new_head[1]-1
              snake.insert(0,new_head)
              if snake[0][0] in [0,height] or snake[0][1] in [0,width] or snake[0] == snake[1:]:
                      curses.endwin()
                      quit()
              if snake[0] == food :
                      food = None
              while food is None :
                      food =[random.randint(3,height-3),random.randint(3,width-3)]
                      window.addch(food[0],food[1],curses.ACS_PI)
              else:
                      tail = snake.pop()
                      window.addch(tail[1],tail[0],)
