from graphics import *
from Dice import Dice

class Horse:
    def __init__(self, speed, y_pos, image_file, window):
        self.speed = speed
        self.dice = Dice(speed)
        self.x_pos = 0
        self.y_pos = y_pos
        self.window = window

        # Create Image inside the class instead of passing it
        self.image = Image(Point(self.x_pos, self.y_pos), image_file)

    def move(self):
        roll = self.dice.roll()
        self.x_pos += roll
        self.image.move(roll, 0)  # Move image along the x-axis

    def draw(self):
        self.image.draw(self.window)

    def crossed_finish_line(self, finish_line_x):
        return self.x_pos >= finish_line_x

def main():
    # Create window
    win = GraphWin("Race Field", 700, 350, autoflush=False)
    win.setBackground(color_rgb(0, 255, 0))

    # Add start message text
    start_text = Text(Point(350, 20), "Click to start the race!")
    start_text.setSize(14)
    start_text.setStyle("bold")
    start_text.draw(win)

    # Create horses (pass filenames instead of Image objects)
    horse1 = Horse(6, 100, "Knight.gif", win)
    horse2 = Horse(6, 150, "Wizard.gif", win)

    # Draw horses initially
    horse1.draw()
    horse2.draw()

    # Draw finish line
    finish_line = Line(Point(650, 0), Point(650, 350))
    finish_line.setWidth(2)
    finish_line.draw(win)

    # Wait for mouse click to start race
    win.getMouse()
    start_text.undraw()  # Remove start message before the race begins

    race_over = False
    while not race_over:
        # Move horses
        horse1.move()
        horse2.move()

        # Check for winner
        if horse1.crossed_finish_line(650) and horse2.crossed_finish_line(650):
            race_over = True
            print("Tie")
        elif horse1.crossed_finish_line(650):
            race_over = True
            print("Horse 1 is the winner")
        elif horse2.crossed_finish_line(650):
            race_over = True
            print("Horse 2 is the winner")

        update(10)

    # Wait for final mouse click before closing
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()


