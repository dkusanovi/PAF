#include <iostream>
#include <cmath>
#include <list>
#include <algorithm>



int funkcija(int list[], int a, int b) {
    for (int i = a; i < b; i++)
    {
        std::cout << list[i]  <<" ";
    }
    return 0;
}


int okretanje(int list[]) {
    for (int i = 9; i > -1; i--)
    {
        std::cout << list[i]  <<" ";
    }
    return 0;
}


int zamjena(int list[], int a, int b){
    for (int i = 0; i < 10; i++)
    {
        int x = list[a];
        list[a] = list[b];
        list[b] = x;
        std::cout << list[i]  <<" ";
    }
    return 0;
}



int main() {
    int cijeli_br[] = {2, 1, 3, 4, 9, 6, 7, 8, 5, 10};
    // funkcija(cijeli_br, 3, 7);
    // okretanje(cijeli_br);
    // zamjena(cijeli_br, 5, 8);
    std::sort(std::begin(cijeli_br), std::end(cijeli_br));

}
