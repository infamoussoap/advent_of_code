#include <iostream>
#include <fstream>
#include <iterator>
#include <vector>
using namespace std;


vector<int> getInputs(string filename){
    vector<int> outputs;
    string text;

    ifstream MyReadFile(filename);

    while (getline(MyReadFile, text)) {
        outputs.push_back(stoi(text));
    }

    return outputs;
}


void part_one(string filename){
    vector<int> array = getInputs(filename);

    int count = 0;

    for (int i = 0; i < array.size() - 1; i++){
        count += array[i + 1] > array[i];
    }

    cout << "Part One: " << count << "\n";
}


void part_two(string filename){
    vector<int> array = getInputs(filename);

    int count = 0;
    int current_summand = 0;
    int next_summand = 0;

    current_summand = array[0] + array[0 + 1] + array[0 + 2];

    for (int i = 0; i < array.size() - 3; i++){
        next_summand = array[i + 1] + array[i + 2] + array[i + 3];

        count += next_summand > current_summand;

        current_summand = next_summand;
    }

    cout << "Part Two: " << count;
}


int main(){
    string filename = "01_inputs.txt";
    
    part_one(filename);
    part_two(filename);
}
