#Implement a class calles Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket." Derive two classes, Batman and Bowler, from the Player class. Override the play() method in each dervied class to.print "The batman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object. #


# Define thevbase class player
class Player:
    def play(self):
        print(" The player is playing cricket.")

# Define the dervied class Batsman
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

# Define the dervied class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()