#include <iostream>
#include "submarine.hpp"
#include <vector>


const std::string FORWARD = "forward";
const std::string DOWN = "down";
const std::string UP = "up";


Submarine::Submarine(int initial_horizontal, int initial_depth){
    horizontal = initial_horizontal;
    depth = initial_depth;
}


void Submarine::display(){
    std::cout << "Horizontal " << horizontal << ", Depth " << depth << "\n";
}

std::vector<int> Submarine::get_position(){
    std::vector<int> pos(2, 0);
    
    pos[0] = horizontal;
    pos[1] = depth;
    
    return pos;
}


int Submarine::horizontal_displacement(std::string command){

    if (command.substr(0, FORWARD.size()) == FORWARD){
        int displacement = stoi(command.substr(FORWARD.size() + 1, command.size()));
        return displacement;
    }
    return 0;
}


int Submarine::depth_displacement(std::string command){

    if (command.substr(0, DOWN.size()) == DOWN){
        int displacement = stoi(command.substr(DOWN.size() + 1, command.size()));
        return -displacement;
    } else if (command.substr(0, UP.size()) == UP){
        int displacement = stoi(command.substr(UP.size() + 1, command.size()));
        return displacement;
    }
    return 0;
}