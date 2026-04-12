# include <iostream>
# include <string>
using namespace std;


double addFunc(double a, double b){
    return a + b;
}
double subtractFunc(double a, double b){
    return a - b;
}
double multiplyFunc(double a, double b){
    return a * b;
}
double divideFunc(double a, double b){
    if(b != 0){
        return a / b;
    } else {
        std::cerr << "Error: Division by zero!" << std::endl;
        return 0; // or handle error as appropriate
    }
};

int main() {
    bool calculate_again = true;

    while (calculate_again) {
        double number1, number2, result = 0.0;
        string operatorIs;

        cout << "Enter 1st number: ";
        if (!(cin >> number1)) {
            cerr << "Invalid number input. Exiting." << endl;
            return 1;
        }

        cout << "Enter 2nd number: ";
        if (!(cin >> number2)) {
            cerr << "Invalid number input. Exiting." << endl;
            return 1;
        }

        cout << "Enter operator (+, -, * or /): ";
        cin >> operatorIs;

        if (operatorIs == "+") {
            result = addFunc(number1, number2);
        } else if (operatorIs == "-") {
            result = subtractFunc(number1, number2);
        } else if (operatorIs == "*") {
            result = multiplyFunc(number1, number2);
        } else if (operatorIs == "/") {
            // divideFunc already reports divide-by-zero
            result = divideFunc(number1, number2);
        } else {
            cerr << "Error: Invalid operator!" << endl;
            // ask user whether to continue
            cout << "Do you want another calculation? (y/n): ";
            char choice;
            cin >> choice;
            if (choice == 'y' || choice == 'Y') {
                continue;
            } else {
                break;
            }
        }

        cout << number1 << " " << operatorIs << " " << number2 << " = " << result << endl;

        cout << "Do you want another calculation? (y/n): ";
        char choice;
        cin >> choice;
        if (choice == 'y' || choice == 'Y') {
            calculate_again = true;
        } else {
            calculate_again = false;
        }
    }

    cout << "\nThanks for using the calculator! 👋" << endl;
    return 0;
}