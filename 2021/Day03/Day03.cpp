#include <iostream>
#include <string>
#include <vector>
#include <fstream>

std::vector<int> arange(int n){
    std::vector<int> array(n, 0);
    for (int i = 0; i < n; i++) {
        array[i] = i;
    }
    return array;
}


std::vector<std::vector<bool>> parse_file(std::string filename) {
    int N = size_of_input(filename);

    std::vector<std::vector<bool>> parsed_file;
    std::string val;
    std::ifstream MyReadFile(filename);


    while (getline(MyReadFile, val)) {
        std::vector<bool> parsed_line(N, 0);
        for (int i = 0; i < N; i++) {
            parsed_line[i] = val[i] == '1';
        }
        parsed_file.push_back(parsed_line);
    }
    return parsed_file;
}



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


std::vector<bool> get_gamma_rate(std::string filename) {
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
    
    for (int i = 0; i < N; i++){
        if (one_counter[i] > length - one_counter[i]) {
            gamma_rate[i] = 1;
        } else {
            gamma_rate[i] = 0;
        }
    }

    return gamma_rate;
}


std::vector<bool> get_epsilon_rate(std::string filename) {
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

    std::vector<bool> epsilon_rate(N, 0);
    
    for (int i = 0; i < N; i++){
        if (one_counter[i] > length - one_counter[i]) {
            epsilon_rate[i] = 0;
        } else {
            epsilon_rate[i] = 1;
        }
    }

    return epsilon_rate;
}


void part_one(std::string filename) {
    std::vector<bool> gamma_rate = get_gamma_rate(filename);
    std::vector<bool> epsilon_rate = get_epsilon_rate(filename);

    std::cout << binary_to_decimal(gamma_rate) * binary_to_decimal(epsilon_rate) << "\n";
}


void part_two(std::string filename) {
    std::vector<bool> gamma_rate = get_gamma_rate(filename);

    std::vector<int> working_index = arange(10);

}


int main(){
    std::string filename;
    
    // std::cout << "Input File: ";
    // std::cin >> filename;



    filename = "test_inputs.txt";

    part_one(filename);
    // part_two(filename);
}