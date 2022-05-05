class Particle {

    private:

    float t, x, y, vx, vy;
    float _dt;
    float _g;
    float _v0, _theta, _x0, _y0, _deltat;

    void evolve(float dt);
    void restart();

    public:
    Particle(float v0, float theta, float x0, float y0, float deltat=0.01, float g=9.81);
    // ~Particle();

    float range(float dt);
    float time(float dt);
};
