#include "Particle.h"
#include <math.h>
// #include <cmath>


void Particle::evolve(float dt)
{
        t = t + dt;

        vx = vx + 0.0;
        vy = vy - g*dt;

        x = x + vx*dt;
        y = y + vy*dt;
    
};

void Particle::restart()
{
    vx = v0*cos(theta);
    vy = v0*sin(theta);
    x = x0;
    y = y0;
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
    v0 = v0;
    theta = (theta/180)*3.14;
    x = x0;
    y = y0;
    deltat = deltat;
    g = g;
    vx = v0*cos(theta);
    vy = v0*sin(theta);
};
