from graphics import*
from Dice import Dice

class Horse:
   def __init__(self, speed, y_pos, image, window):
       self.speed = speed
       self.dice = Dice(speed)
       self.x_pos = 0
       self.y_pos = y_pos
       self.image = image
       self.window = window
       #self.image.draw(self.window)

   def move(self):
       roll = self.dice.roll()
       self.x_pos += roll
       #self.image.move(roll, 0)


   def draw(self):
       self.image.draw_at_pos(self.window, self.x_pos, self.y_pos)


   def crossed_finish_line(self, finish_line_x):
       return self.x_pos >= finish_line_x


def main():
   #Creating window
   win = GraphWin("Race field", 700, 350, autoflush= False)
   win.setBackground(color_rgb(0, 255, 0))

   #Set horse image
   horse1_image = "Knight.gif"
   horse2_image = "Wizard.gif"

   horse1_image = Image(Point(0,100), "Knight.gif")
   horse2_image = Image(Point(0, 150), "Wizard.gif")

   #Set horse1, horse2
   horse1 = Horse(6, 50, horse1_image, win)
   horse2 = Horse(6, 150, horse2_image, win)

   #Draw finish line
   finish_line = Line(Point(650,0), Point(650, 350))
   finish_line.draw(win)
   win.getMouse()

   race_over = False
   while not race_over:
       win.clear_win()

       #Move horse
       horse1.move()
       horse2.move()
       horse1.draw()
       horse2.draw()
       finish_line.draw(win)
       update(10)

       if horse1.crossed_finish_line(650) and horse2.crossed_finish_line(650):
           race_over = True
           print("Tie")
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




