#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    srand(time(0));

    int secret = rand() % 10 + 1;
    int guess;

    cout << "Guess a number between 1 and 10: ";
    cin >> guess;

    if (guess == secret) {
        cout << "Correct! You guessed it.\n";
    } else if (guess < secret) {
        cout << "Too low! The number was " << secret << ".\n";
    } else {
        cout << "Too high! The number was " << secret << ".\n";
    }

    return 0;
}