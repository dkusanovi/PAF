#include <iostream>
#include <cmath>

void sustav(float a1, float b1, float c1, float a2, float b2, float c2) {
    if ((a1*b2-a2*b1)==0)
    {
        std::cout << "Dijeljenje s 0, nema rjesenja" << std::endl;
    }
    else if ((a2*b1-a1*b2)==0)
    {
        std::cout << "Dijeljenje s 0, nema rjesenja" << std::endl;
    }
    else
    {
    float x = (b1*c2-b2*c1)/(a2*b1-a1*b2);
    float y = (a1*c2-a2*c1)/(a1*b2-a2*b1);
    std::cout << "x = " << x << " i y = " << y << std::endl;
    }
}

int main() {
    sustav(1, 2, 3, 4, 5, 6);
}