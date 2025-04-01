import random
import time

class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, other):
        damage = random.randint(1, self.strength)
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage!")
        print(f"{other.name} has {other.health} health remaining.\n")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        self.okonkwo = Character("Okonkwo", 100, 20)
        self.enemies = [
            Character("Ikemefuna", 50, 10),
            Character("Nwoye", 40, 8),
            Character("Colonial Soldier", 200, 15)
        ]
        self.symbols = {
            "Yams": "Yams symbolize wealth, masculinity, and the importance of agriculture in Igbo culture. They represent Okonkwo's success and his fear of failure.",
            "Fire": "Fire represents Okonkwo's fierce nature and his passionate drive. It also symbolizes destruction, reflecting the chaos brought by colonialism.",
            "The Locusts": "The locusts symbolize the arrival of colonial forces and the inevitable change they bring to the Igbo society, consuming everything in their path."
        }
        self.plot_moments = [
            "Okonkwo's exile after accidentally killing a clansman.",
            "The arrival of the missionaries and the beginning of colonial influence.",
            "Okonkwo's tragic end as he takes his own life."
        ]
        self.social_issue = "Colonialism and its impact on traditional societies."
        self.universal_idea = "The struggle between tradition and change."

    def display_intro(self):
        print("Welcome to the world of 'Things Fall Apart'!")
        print("You will play as Okonkwo, a proud warrior of the Igbo tribe.")
        print("Your journey will involve battles, choices, and the struggle against colonialism.")
        print("\nImportant symbols in this story include:")
        for symbol, explanation in self.symbols.items():
            print(f"- {symbol}: {explanation}")
        print("\nThe story addresses the social issue of:", self.social_issue)
        print("Universal idea:", self.universal_idea)
        print("\nLet the journey begin!\n")
        time.sleep(2)

    def battle(self, enemy):
        print(f"A wild {enemy.name} appears!")
        while self.okonkwo.is_alive() and enemy.is_alive():
            self.okonkwo.attack(enemy)
            if enemy.is_alive():
                enemy.attack(self.okonkwo)
            time.sleep(1)

        if self.okonkwo.is_alive():
            print(f"{self.okonkwo.name} has defeated {enemy.name}!\n")
        else:
            print(f"{self.okonkwo.name} has been defeated by {enemy.name}...\n")

    def plot_arc(self):
        print("Plot Moments:")
        for moment in self.plot_moments:
            print(f"- {moment}")
        print("\n")

    def conclusion(self):
        print("As you reflect on your journey as Okonkwo, consider the following themes:")
        print("1. **Tradition vs. Change**: Okonkwo's struggle against the changes brought by colonialism highlights the tension between maintaining cultural identity and adapting to new realities.")
        print("2. **Masculinity and Pride**: Okonkwo's fear of being perceived as weak drives many of his actions, ultimately leading to his downfall. This reflects the societal pressures surrounding masculinity.")
        print("3. **The Impact of Colonialism**: The arrival of the missionaries and colonial forces disrupts the Igbo way of life, symbolized by the locusts that consume everything in their path.")
        print("4. **Tragedy and Fate**: Okonkwo's tragic end serves as a reminder of the consequences of pride and the inability to adapt to change.")
        print("\nThank you for playing! Remember, the struggle of the Igbo people continues, and their story is one of resilience and strength.")

    def start_game(self):
        self.display_intro()
        self.plot_arc()

        for enemy in self.enemies:
            self.battle(enemy)
            if not self.okonkwo.is_alive():
                print("Game Over! You have failed to uphold your legacy.")
                return

        print("Congratulations! You have fought bravely against the challenges.")
        print("However, the struggle against colonialism continues...\n")
        self.conclusion()

if __name__ == "__main__":
    game = Game()
    game.start_game()
