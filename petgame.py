import random
import time

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = random.randint(0, 10)
        self.happiness = random.randint(0, 10)
        self.health = random.randint(0, 10)
        self.age = 0

    def eat(self):
        if self.hunger > 0:
            self.hunger -= random.randint(1, 3)
        else:
            print(f"{self.name} is not hungry right now.")

    def play(self):
        self.happiness += random.randint(1, 3)

    def sleep(self):
        print(f"{self.name} is sleeping...")
        time.sleep(2)
        print(f"{self.name} wakes up refreshed!")
        self.health += random.randint(1, 2)

    def check_health(self):
        if self.hunger <= 3:
            print(f"{self.name} is hungry.")
        if self.happiness <= 3:
            print(f"{self.name} is feeling sad.")
        if self.health <= 3:
            print(f"{self.name} is not feeling well.")

    def age_up(self):
        self.age += 1

    def __str__(self):
        return f"{self.name} the {self.species}: Hunger - {self.hunger}, Happiness - {self.happiness}, Health - {self.health}, Age - {self.age}"

class Shelter:
    def __init__(self):
        self.pets = []

    def adopt_pet(self, pet):
        self.pets.append(pet)

    def feed_all_pets(self):
        for pet in self.pets:
            pet.eat()

    def play_with_all_pets(self):
        for pet in self.pets:
            pet.play()

    def check_all_pets_health(self):
        for pet in self.pets:
            pet.check_health()

    def show_all_pets(self):
        for pet in self.pets:
            print(pet)

def main():
    shelter = Shelter()

    while True:
        print("\n1. Adopt a pet")
        print("2. Feed all pets")
        print("3. Play with all pets")
        print("4. Check pets' health")
        print("5. Show all pets")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter the pet's name: ")
            species = input("Enter the pet's species: ")
            pet = Pet(name, species)
            shelter.adopt_pet(pet)
            print(f"{name} the {species} has been adopted!")
        elif choice == "2":
            shelter.feed_all_pets()
            print("All pets have been fed.")
        elif choice == "3":
            shelter.play_with_all_pets()
            print("All pets have been played with.")
        elif choice == "4":
            shelter.check_all_pets_health()
        elif choice == "5":
            print("\nAll Pets:")
            shelter.show_all_pets()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

        # Aging the pets
        for pet in shelter.pets:
            pet.age_up()

if __name__ == "__main__":
    main()
