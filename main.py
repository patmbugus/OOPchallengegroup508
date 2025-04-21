from pet import Pet

if __name__ == "__main__":
    # Create a pet object
    my_pet = Pet("Buddy")

    # Test the methods
    print("Creating pet: Buddy")
    my_pet.get_status()

    print("\nBuddy is eating...")
    my_pet.eat()
    my_pet.get_status()

    print("\nBuddy is playing...")
    my_pet.play()
    my_pet.get_status()

    print("\nBuddy is sleeping...")
    my_pet.sleep()
    my_pet.get_status()

    print("\nTeaching Buddy some tricks...")
    my_pet.train("roll over")
    my_pet.train("play dead")
    my_pet.show_tricks()