## 🧠 Objective

# Create a class called Pet with the following:

# ### Attributes:
# - name: the name of your pet
# - hunger: an integer representing hunger level (0 = full, 10 = very hungry)
# - energy: an integer representing energy level (0 = tired, 10 = fully rested)
# - happiness: an integer (0–10)
# ### Methods:
# - eat(): reduces hunger by 3 points (but not below 0), and increases happiness by 1.
# - sleep(): increases energy by 5 points (but not above 10).
# - play(): decreases energy by 2, increases happiness by 2, and increases hunger by 1.
# - get_status(): prints the current state of the pet.

# ### Bonus 🎯
# - Add a method train(trick) that teaches your pet a new trick and stores it in a list.
# - Add a method show_tricks() that prints all learned tricks.
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.energy = 10
        self.happiness = 5
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Ensure hunger does not go below 0
        self.happiness = min(10, self.happiness + 1)  # Ensure happiness does not exceed 10

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Ensure energy does not exceed 10

    def play(self):
        self.energy = max(0, self.energy - 2)  # Ensure energy does not go below 0
        self.happiness = min(10, self.happiness + 2)  # Ensure happiness does not exceed 10
        self.hunger = min(10, self.hunger + 1)  # Ensure hunger does not exceed 10

    def get_status(self):
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        """Teaches the pet a new trick."""
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}!")

    def show_tricks(self):
        """Displays all learned tricks."""
        if self.tricks:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")