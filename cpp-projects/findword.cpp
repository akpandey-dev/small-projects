#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char* argv[]) {
    if (argc != 3) {
        cout << "Usage: findword <filename> <word>" << endl;
        return 1;
    }

    string filename = argv[1];
    string word = argv[2];

    ifstream file(filename);

    if (!file.is_open()) {
        cout << "Error: Could not open file." << endl;
        return 1;
    }

    string line;
    int lineNumber = 0;
    int totalCount = 0;
    vector<pair<int, string>> lines;

    while (getline(file, line)) {
        lineNumber++;
        size_t pos = 0;
        int countInLine = 0;
        bool foundInLine = false;

    while ((pos = line.find(word, pos)) != string::npos) {
        countInLine++;
        totalCount++;
        pos += word.length();
        foundInLine = true;
    }

    if (foundInLine) {
        lines.push_back({lineNumber, line});
    }

        if (countInLine > 0) {
            cout << "Line " << lineNumber << ": " << countInLine << " match(es)" << endl;
        }
    }

    if (totalCount == 0) {
        cout << "Word not found." << endl;
    } else {
        char wantLineView;
        cout << "Total occurrences: " << totalCount << endl;
        cout << "Do you want to view the lines where match(es) have been found?(y/n)" << endl;
        cin >> wantLineView;
        if(wantLineView == 'y' || wantLineView == 'Y'){
        int n = lines.size();
        for (int i = 0; i < n; i++) {
        cout << "Line " << lines[i].first << ": " << lines[i].second << endl;}
        }
    }

    file.close();
    return 0;
}