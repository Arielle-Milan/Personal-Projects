#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void casinoNumberGuessingGame() {
    srand(time(0));  //initialize random seed based on current time

    double balance = 1000.0;  //starting balance
    int secretNumber, guess, bet;

    cout << "Welcome to the Casino Number Guessing Game!" << endl;
    cout << "Your starting balance is R" << balance << endl;

    while (true) {
        cout << "---------------------------------------------------" << endl;

        //Bet Input
        cout << "How much would you like to bet? Your current balance is R" << balance << ": ";
        cin >> bet;

        if (bet > balance) {
            cout << "You cannot bet more than your current balance. Please enter a valid amount." << endl;
            continue;
        }

        //Generate secret number
        secretNumber = rand() % 100 + 1;  // Random number between 1 and 100

        //player Guess
        cout << "Guess the number (between 1 and 100): ";
        cin >> guess;

        //check guess
        if (guess == secretNumber) {
            cout << "Congratulations! You guessed the correct number: " << secretNumber << endl;
            balance += bet;  //win the bet amount
        } 
        else {
            cout << "Sorry, the correct number was " << secretNumber << "." << endl;
            balance -= bet;  //lose the bet amount
        }

        //display current balance
        cout << "Your current balance is: R" << balance << endl;

        //check if the player still has money
        if (balance <= 0) {
            cout << "You have no more money left. Game over!" << endl;
            break;
        }

        //ask the player if they want to play again
        string playAgain;
        cout << "Do you want to play again? (yes/no): ";
        cin >> playAgain;

        if (playAgain != "yes") {
            cout << "Thank you for playing! Your final balance is R" << balance << endl;
            break;
        }
    }
}

int main() {
    casinoNumberGuessingGame();  //start the game
    return 0;
}