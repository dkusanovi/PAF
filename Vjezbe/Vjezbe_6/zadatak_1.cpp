// Napišite C++ program u koji sadrži funkciju koja kao ulazne parametre prima (x, y) koordinate za dvije
// točke. Neka ta funkcija na ekran ispisuje jednadžbu pravca koji prolazi kroz te dvije točke. Pozovite tu
// funkciju u svom programu.

#include <iostream>
#include <iomanip>



void koordinate(float x1, float y1, float x2, float y2)
{
    float k = (y2-y1)/(x2-x1);
    float l = -k*x1 + y1;
    if (l > 0)
    {
    std::cout << "Jednadzba pravca je y = " << k << "x +" << l <<"." <<std::endl;
    }
    else if (l < 0)
    {
    std::cout << "Jednadzba pravca je y = " << k << "x " << l <<"." <<std::endl;
    }
}


int main() {
    koordinate(15, 4, 20, 3);
    return 0;

}

