from player import *
from wall import *
from graphics import *
from settings import *
from random import *

def main():
    """This is the main function."""

    win = GraphWin(WIN_TITLE, WIN_X, WIN_Y, autoflush=False)

    #Setting up player object
    bird = Player(WIN_X // 4, WIN_Y // 4, PLAYER_COLOR, win)
    bird.body.draw(win)

    #Setting up wall objects
    y = randrange(WIN_Y * 2 // 10, WIN_Y * 5 // 10)
    space = randrange(WIN_Y * 2 // 10, WIN_Y * 4 // 10)

    wallA = Wall(WIN_X, y, space, WALL_COLOR, win)
    wallB = Wall(-WALL_WIDTH, y, space, WALL_COLOR, win)

    wallA.upRect.draw(win)
    wallA.downRect.draw(win)
    wallB.upRect.draw(win)
    wallB.downRect.draw(win)

    score = 0
    collision = 0   

    scoreText = Text(Point(WIN_X // 2, WIN_Y // 8), str(score))
    scoreText.setSize(30)
    scoreText.draw(win)

    #Main game loop
    while not win.isClosed() and collision == 0:
        if win.checkMouse() != None:
            bird.velocity += -GRAVITY * FPS
        bird.update()

        #Checking if the first wall has reached the beginning. If so, it spawns again.
        if wallA.x + WALL_WIDTH <= 0:

            y = randrange(WIN_Y * 2 // 10, WIN_Y * 5 // 10)
            space = randrange(WIN_Y * 2 // 10, WIN_Y * 4 // 10)

            wallA.upRect.undraw()
            wallA.downRect.undraw()
            wallA = Wall(WIN_X, y, space, WALL_COLOR, win)

            wallA.upRect.draw(win)
            wallA.downRect.draw(win)

        #Checking if the first wall is at the half. If it is, second wall is spawned
        if wallA.x + WALL_WIDTH <= (WIN_X // 2) and wallB.x + WALL_WIDTH <= 0:
            y = randrange(WIN_Y * 2 // 10, WIN_Y * 5 // 10)
            space = randrange(WIN_Y * 2 // 10, WIN_Y * 4 // 10)

            wallB.upRect.undraw()
            wallB.downRect.undraw()
            wallB = Wall(WIN_X, y, space, WALL_COLOR, win)

            wallB.upRect.draw(win)
            wallB.downRect.draw(win)

        #Checking if any collision has taken place
        #Collision with wallA
        if bird.x + PLAYER_SIZE >= wallA.x and bird.x + PLAYER_SIZE <= wallA.x + WALL_WIDTH:
            if bird.y - PLAYER_SIZE >= wallA.y and bird.y + PLAYER_SIZE <= wallA.y + wallA.space:
                 score += 1
            else:
                collision = 1

        #Collision with wallB
        if bird.x + PLAYER_SIZE >= wallB.x and bird.x + PLAYER_SIZE <= wallB.x + WALL_WIDTH:
            if bird.y - PLAYER_SIZE >= wallB.y and bird.y + PLAYER_SIZE <= wallB.y + wallB.space:
                score += 1
            else:
                collision = 1

        wallA.update()
        wallB.update()
        scoreText.setText(str(score // (WALL_WIDTH // -GAME_SPEED)))
        update(FPS)

    #Game over screen
    gameOver = Text(Point(WIN_X // 2, WIN_Y //2), "GAME OVER")
    gameOver.setSize(30)
    gameOver.draw(win)

    win.getMouse() # Pause
    win.close()    # Close window

if __name__ == "__main__":
    main()