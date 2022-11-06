#include <iostream>
#include <string>
#include <vector>
#include <fstream>


int size_of_input(std::string filename) {
    std::ifstream MyReadFile(filename);
    std::string val;

    getline(MyReadFile, val);
    MyReadFile.close();

    return val.size();
}


int binary_to_decimal(std::vector<bool> binary_array){
    int val = 0;
    int running_power = 1;

    for (int i = binary_array.size() - 1; i >= 0; i--) {
        if (binary_array[i]){
            val += running_power;
        }
        running_power *= 2;
    }
    return val;
}

void part_one(std::string filename) {
    std::string val;
    std::ifstream MyReadFile(filename);

    int N = size_of_input(filename);

    std::vector<int> one_counter(N, 0);
    int length = 0;

    while (getline(MyReadFile, val)) {
        for (int i = 0; i < N; i++) {
            one_counter[i] += val[i] == '1';
        }
        length += 1;
    }

    std::vector<bool> gamma_rate(N, 0);
    std::vector<bool> epsilon_rate(N, 0);
    
    for (int i = 0; i < N; i++){
        if (one_counter[i] > length - one_counter[i]) {
            gamma_rate[i] = 1;
            epsilon_rate[i] = 0;
        } else {
            gamma_rate[i] = 0;
            epsilon_rate[i] = 1;
        }
    }

    std::cout << binary_to_decimal(gamma_rate) * binary_to_decimal(epsilon_rate) << "\n";
}


void part_two(std::string filename) {

}


int main(){
    std::string filename;
    
    // std::cout << "Input File: ";
    // std::cin >> filename;



    filename = "test_inputs.txt";

    part_one(filename);
    // part_two(filename);
}