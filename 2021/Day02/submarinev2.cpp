#include <iostream>
#include "submarinev2.hpp"
#include <vector>


const std::string FORWARD = "forward";
const std::string DOWN = "down";
const std::string UP = "up";


SubmarineV2::SubmarineV2(int initial_horizontal, int initial_depth, int initial_aim) : Submarine(initial_horizontal, initial_depth){
    aim = initial_aim;
}


void SubmarineV2::move(std::string command){
    int horizontal_change = horizontal_displacement(command);
    if (horizontal_change != 0) {
        horizontal += horizontal_change;
        depth += aim * horizontal_change;
    } else {
        int aim_change = -depth_displacement(command);
        aim += aim_change;
    }
}
