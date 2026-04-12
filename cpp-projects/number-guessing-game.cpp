#include <iostream>
#include <cstdlib>
#include <ctime>
#include <limits> // for numeric_limits

using namespace std;

int main() {
    srand(time(0)); // seed RNG once at the start
    bool play_again = true;

    while (play_again) {
        int max_attempts;
        bool game_over = false;
        int upper_limit;

        string difficulty;

        cout << "\n🎯 Welcome to the Number Guessing Game!" << endl << "Enter your difficulty level(E-easy, M-medium, H-hard):" << endl;
        cin >> difficulty;

        

if (difficulty == "E" || difficulty == "e") {
    upper_limit = 10;
    max_attempts = 3;
} else if (difficulty == "M" || difficulty == "m") {
    upper_limit = 50;
    max_attempts = 5;
} else if (difficulty == "H" || difficulty == "h") {
    upper_limit = 100;
    max_attempts = 7;
} else {
    cerr << "Invalid difficulty level. Setting to Easy." << endl;
    upper_limit = 10;
    max_attempts = 3;
}
        int secret_number = rand() % upper_limit + 1;
        int attempts = 0;



        cout << "I have selected a number between 1 and " << upper_limit << ". You have " << max_attempts << " chances!" << endl;

        while (!game_over) {
            int guess;
            cout << "\nEnter your guess: ";
            cin >> guess;
            attempts++;

            if (guess == secret_number) {
                cout << "🎉 Congratulations! You guessed the number in " 
                     << attempts << " attempt(s)!" << endl;
                game_over = true;
            } else if (guess < secret_number) {
                cout << "Too low! Try again." << endl;
            } else {
                cout << "Too high! Try again." << endl;
            }

            if (attempts >= max_attempts && !game_over) {
                cout << "\n❌ You've used all attempts! The number was " 
                     << secret_number << "." << endl;
                game_over = true;
            }
        }

        cout << "\nDo you want to play again? (y/n): ";
        char choice;
        cin >> choice;
        if (choice == 'y' || choice == 'Y') {
            play_again = true;
        } else {
            play_again = false;
            cout << "\nThanks for playing! 👋\n";
        }
    }

    return 0;
}
