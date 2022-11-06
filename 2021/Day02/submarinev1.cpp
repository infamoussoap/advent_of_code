#include "submarinev1.hpp"

SubmarineV1::SubmarineV1(int initial_horizontal, int initial_depth) : Submarine(initial_horizontal, initial_depth){
    
}


void SubmarineV1::move(std::string command){
    horizontal += horizontal_displacement(command);
    depth += depth_displacement(command);
}