#include <iostream>
#include <vector>
#include <math.h>
#include <fstream>
#include <string>

using std::vector;


class HarmonicOscillator {

    private:

    float t, x, v;
    float dt;
    float v0, a, theta, x0, k, m, t_uk;

    void oscillate(float dt)
    {
        t = t + dt;
        x = x + v*dt;
        a = -(k/m)*x;
        v = v + a*dt;

        t_lista.push_back(t);
        x_lista.push_back(x);
        a_lista.push_back(a);
        v_lista.push_back(v);
    };
    

    public:

    vector<float> t_lista;
    vector<float> x_lista;
    vector<float> a_lista;
    vector<float> v_lista;

    HarmonicOscillator(float v0, float a, float x0, float k, float m, float t_uk, float dt=0.01)
    {
        while (t < t_uk){
            x = x0;
            v = v0;
            k = k;
            m = m;
            dt = dt;
            a = -(k/m)*x;
            t = 0;
            x_lista.push_back(x);
            v_lista.push_back(v);
            a_lista.push_back(a);
            t_lista.push_back(t);
        }
    };
};

int main()
{
    HarmonicOscillator ho(10.0, 0, 10, 10, 2, 20, 0.01);

    std::string x_br;
    std::string v_br;
    std::string a_br;
    std::string t_br;

    float x = ho.x_lista[0];
    float v = ho.v_lista[0];
    float a = ho.a_lista[0];
    float t = ho.t_lista[0];

    x_br = std::to_string(x);
    v_br = std::to_string(v);
    a_br = std::to_string(a);
    t_br = std::to_string(t);


    std::ofstream file;

    file.open ("x.txt");
    file << x_br;
    file.close();

    file.open ("v.txt");
    file << v_br;
    file.close();

    file.open ("a.txt");
    file << a_br;
    file.close();

    file.open ("t.txt");
    file << t_br;
    file.close();

    return 0;

}
