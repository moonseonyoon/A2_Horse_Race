from graphics import *
from Dice import Dice

class Horse:
    def __init__(self, speed, y_pos, image, window):
        self.speed = speed
        self.dice = Dice(speed)
        self.x_pos = 0
        self.y_pos = y_pos
        self.image = image
        self.window = window

    def move(self):
        roll = self.dice.roll()
        self.x_pos += roll
        self.image.move(roll, 0)  # Moves the image on the screen

    def draw(self):
        self.image.draw(self.window)

    def crossed_finish_line(self, finish_line_x):
        return self.x_pos >= finish_line_x


def main():
    # Creating window
    win = GraphWin("Race field", 700, 350, autoflush=False)
    win.setBackground(color_rgb(0, 255, 0))

    # Set horse images
    horse1_image = Image(Point(0, 100), "Knight.gif")
    horse2_image = Image(Point(0, 150), "Wizard.gif")

    # Create horse objects
    horse1 = Horse(6, 100, horse1_image, win)
    horse2 = Horse(6, 150, horse2_image, win)

    # Draw finish line
    finish_line = Line(Point(650, 0), Point(650, 350))
    finish_line.setWidth(3)
    finish_line.draw(win)

    # Draw horses
    horse1.draw()
    horse2.draw()

    # Display start message
    start_text = Text(Point(350, 20), "Click to start the race!")
    start_text.setSize(14)
    start_text.setStyle("bold")
    start_text.draw(win)

    win.getMouse()
    start_text.undraw()

    # Race loop
    race_over = False
    while not race_over:
        horse1.move()
        horse2.move()
        update(10)

        if horse1.crossed_finish_line(650) and horse2.crossed_finish_line(650):
            race_over = True
            print("It's a tie!")
        elif horse1.crossed_finish_line(650):
            race_over = True
            print("The Crab is the winner")
        elif horse2.crossed_finish_line(650):
            race_over = True
            print("The Snake is the winner")

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()

