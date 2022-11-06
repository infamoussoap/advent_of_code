#ifndef SUBMARINE_CPP
#define SUBMARINE_CPP

#include <string>
#include <iostream>
#include <vector>


class Submarine {
    public:
        int horizontal;
        int depth;

        Submarine(int initial_horizontal, int initial_depth);
        
        void display();
        std::vector<int> get_position();
        
        int horizontal_displacement(std::string command);
        int depth_displacement(std::string command);

};

#endif