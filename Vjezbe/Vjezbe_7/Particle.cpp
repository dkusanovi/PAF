#include "Particle.h"
#include <math.h>
#include <iostream>
// #include <cmath>


void Particle::evolve(float dt)
{
        t = t + dt;

        vx = vx + 0.0;
        vy = vy - _g*dt;

        x = x + vx*dt;
        y = y + vy*dt;
    
};

void Particle::restart()
{
    vx = _v0*cos(_theta);
    vy = _v0*sin(_theta);
    x = _x0;
    y = _y0;
};

float Particle::range(float dt)
{
    while (y >= 0){
        evolve(dt);
    }
    return x;
};

float Particle::time(float dt)
{
    while (y >= 0){
        evolve(dt);
    }
    return t;
};


Particle::Particle(float v0, float theta, float x0, float y0, float deltat, float g)
{
    _v0 = v0;
    _theta = (theta/180)*3.14159;
    x = x0;
    y = y0;
    _deltat = deltat;
    _g = g;
    vx = v0*cos(_theta);
    std::cout << vx << std::endl;
    vy = v0*sin(_theta);
};
