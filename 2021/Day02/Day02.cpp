#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <stdlib.h>
#include "submarinev1.hpp"
#include "submarinev2.hpp"


void part_one(std::string filename) {
    SubmarineV1 submarine(0, 0);

    std::string command;
    std::ifstream MyReadFile(filename);

    while (getline(MyReadFile, command)) {
        submarine.move(command);
    }

    submarine.display();

    std::vector<int> position = submarine.get_position();
    std::cout << "Part One: " << abs(position[0]) * abs(position[1]) << "\n";
}


void part_two(std::string filename) {
    SubmarineV2 submarine(0, 0, 0);
    
    std::string command;
    std::ifstream MyReadFile(filename);

    while (getline(MyReadFile, command)) {
        submarine.move(command);
    }

    submarine.display();

    std::vector<int> position = submarine.get_position();
    std::cout << "Part Two: " << abs(position[0]) * abs(position[1]) << "\n";
}


int main(){
    std::string filename;
    
    std::cout << "Input File: ";
    std::cin >> filename;

    // filename = "test_inputs.txt";

    part_one(filename);
    part_two(filename);
}