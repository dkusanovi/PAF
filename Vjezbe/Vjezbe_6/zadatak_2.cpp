#include <iostream>
#include <cmath>

void kruznica(float a, float b, float x0, float y0, float r) {
    float udaljenost = sqrt(pow((b-y0), 2)+pow((a-x0), 2));
    float udaljenost2 = sqrt(pow((b-y0), 2)+pow((a-x0), 2))-r;

    if (udaljenost < r)
    {
        std::cout << "Tocka se nalazi unutar kruznice." << std::endl;
    }
    else if (udaljenost == r)
    {
        std::cout << "Tocka se nalazi na kruznici." << std::endl;
    }
    else 
    {
        std::cout << "Tocka se nalazi izvan kruznice." << std::endl;
    }

}

int main() {
    kruznica(2, -6, 2, 4, 7);
    return 0;
}