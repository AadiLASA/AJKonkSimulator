#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
using namespace std;

struct Character {
    string name;
    int health;
    int attack;
};

void intro() {
    cout << "You are a Vietnam War soldier, mysteriously transported to Umuofia, the world of Okonkwo.\n";
    cout << "In this land, you must navigate choices that test your morality and survival instincts.\n";
    cout << "Your decisions will shape your fate.\n\n";
}

void battle(Character &player, Character &okonkwo) {
    srand(time(0));
    cout << "A battle begins between " << player.name << " and " << okonkwo.name << "!\n";
    while (player.health > 0 && okonkwo.health > 0) {
        cout << player.name << "'s turn! Choose an action:\n";
        cout << "1. Attack\n2. Defend\n3. Run\n";
        int choice;
        cin >> choice;

        if (choice == 1) {
            int damage = rand() % player.attack + 1;
            okonkwo.health -= damage;
            cout << "You strike Okonkwo for " << damage << " damage!\n";
        } else if (choice == 2) {
            cout << "You brace yourself for the next attack.\n";
        } else if (choice == 3) {
            cout << "You attempt to flee... but Okonkwo does not let cowards escape!\n";
        }

        if (okonkwo.health > 0) {
            int damage = rand() % okonkwo.attack + 1;
            player.health -= damage;
            cout << "Okonkwo strikes back for " << damage << " damage!\n";
        }
    }

    if (player.health <= 0) {
        cout << "You have been defeated by Okonkwo...\n";
    } else {
        cout << "You have defeated Okonkwo!\n";
    }
}

void choice_morality(Character &player, Character &okonkwo) {
    int choice;
    cout << "Okonkwo challenges your views. How do you respond?\n";
    cout << "1. Engage in a fight to prove your strength.\n";
    cout << "2. Try to reason with him about tradition and change.\n";
    cout << "3. Reject his worldview and walk away.\n";
    cin >> choice;

    switch(choice) {
        case 1:
            battle(player, okonkwo);
            break;
        case 2:
            cout << "You discuss history, culture, and war. Okonkwo listens but remains skeptical.\n";
            break;
        case 3:
            cout << "You turn away, choosing a different path. Okonkwo watches in silence.\n";
            break;
        default:
            cout << "Invalid choice. Try again.\n";
            choice_morality(player, okonkwo);
    }
}

void main_menu() {
    Character player = {"Soldier", 100, 20};
    Character okonkwo = {"Okonkwo", 120, 25};

    int choice;
    cout << "1. Start Game\n";
    cout << "2. Exit\n";
    cin >> choice;

    if (choice == 1) {
        intro();
        choice_morality(player, okonkwo);
    } else {
        cout << "Exiting game.\n";
    }
}

int main() {
    main_menu();
    return 0;
}
