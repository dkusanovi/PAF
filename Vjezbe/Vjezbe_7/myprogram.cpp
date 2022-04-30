#include <iostream>
#include "Particle.h"

int main()
{
    Particle p1(10, 40, 0, 10);
    Particle p2(30, 70, 0, 0);

    float domet1 = p1.range(0.01);
    std::cout << "Domet cestice 1 je " << domet1 << "." << std::endl;

    float domet2 = p2.range(0.01);
    std::cout << "Domet cestice 2 je " << domet2 << "." << std::endl;

    float vrijeme1 = p1.time(0.01);
    std::cout << "Vrijeme hitca cestice 2 je " << vrijeme1 << "." << std::endl;

    float vrijeme2 = p2.time(0.01);
    std::cout << "Vrijeme hitca cestice 2 je " << vrijeme2 << "." << std::endl;

    return 0;
};
