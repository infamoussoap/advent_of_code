#include "submarine.hpp"


class SubmarineV2 : public Submarine {
    public:
        int aim;
        SubmarineV2(int initial_horizontal, int initial_depth, int aim);
        void move(std::string command);
};
