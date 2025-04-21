class Pet:
    def __init__(self, name, hunger, energy, happiness):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.tricks = []

    def describe_level(self, level):
        if level <= 2:
            return "very low"
        elif level <= 4:
            return "low"
        elif level <= 6:
            return "moderate"
        elif level <= 8:
            return "high"
        else:
            return "very high"

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating. Hunger: {self.describe_level(self.hunger)}, Happiness: {self.describe_level(self.happiness)}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping. Energy: {self.describe_level(self.energy)}")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played. Energy: {self.describe_level(self.energy)}, Happiness: {self.describe_level(self.happiness)}, Hunger: {self.describe_level(self.hunger)}")
        else:
            print(f"{self.name} is too tired to play. Try letting them sleep first.")

    def get_status(self):
        print(f"\n📋 {self.name}'s Status:")
        print(f"   Hunger: {self.describe_level(self.hunger)}")
        print(f"   Energy: {self.describe_level(self.energy)}")
        print(f"   Happiness: {self.describe_level(self.happiness)}")

    def train(self):
        trick = input("What trick do you want to teach your pet? ")
        if trick:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned a new trick: {trick}! 🎉")
        else:
            print("You didn't enter a trick!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")


def create_pet():
    name = input("Enter your pet's name: ")
    try:
        hunger = int(input("Enter hunger level (0–10): "))
        energy = int(input("Enter energy level (0–10): "))
        happiness = int(input("Enter happiness level (0–10): "))
    except ValueError:
        print("❌ Please enter valid numbers between 0 and 10.")
        return None
    return Pet(name, hunger, energy, happiness)


def run_pet_game():
    while True:
        pet = create_pet()
        if not pet:
            continue

        while True:
            print(f"\nWhat would you like to do with {pet.name}?")
            print("1. Eat 🍖")
            print("2. Sleep 😴")
            print("3. Play 🎾")
            print("4. Train a new trick 🧠")
            print("5. Show learned tricks 🎓")
            print("6. Show pet status 📋")
            print("7. Exit to create new pet or quit ❌")

            choice = input("Choose an option (1-7): ")

            if choice == "1":
                pet.eat()
            elif choice == "2":
                pet.sleep()
            elif choice == "3":
                pet.play()
            elif choice == "4":
                pet.train()
            elif choice == "5":
                pet.show_tricks()
            elif choice == "6":
                pet.get_status()
            elif choice == "7":
                break
            else:
                print("❌ Invalid choice. Try again.")

        again = input("\nDo you want to create a new pet? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing! 🐾")
            break


# Start the game
if __name__ == "__main__":
    run_pet_game()
