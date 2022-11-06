#include "submarine.hpp"


class SubmarineV1 : public Submarine {
    public:
        SubmarineV1(int initial_horizontal, int initial_depth);
        void move(std::string command);
};
