import matplotlib.pyplot as plt


class Force:
    def __init__(self, k, m, dt, force):
        self.t = []
        self.ax = []
        self.vx = []
        self.x = []
        self.dt = dt
        self.m = m
        self.k = k


    def set_initial_conditions(self, x0, v0, t0, k, m, dt, force):
        self.m = m
        self.k = k
        self.dt = dt
        self.vx.append(v0)
        self.x.append(x0)
        self.t.append(t0)
        self.force = force(self.vx[-1], self.x[-1], self.t[-1])
        self.ax.append(self.force / m)
        self.name = force 


    def reset(self):
        self.__init__()


    def move(self, t, force):
        for i in range(int(t/self.dt)):
            self.force = force(self.vx[-1], self.x[-1], self.t[-1])
            self.t.append(self.t[-1] + self.dt)
            self.ax.append(self.force / self.m)
            self.vx.append(self.vx[-1] + self.ax[-1]*self.dt)
            self.x.append(self.x[-1] + self.vx[-1]*self.dt)

        return self.t, self.ax, self.vx, self.x

    
    def graf(self):
        self.move(10, self.name)

        fig, axes = plt.subplots(1, 3, figsize=(14, 4))

        axes[0].plot(self.t, self.x)
        axes[0].set_xlabel('vrijeme [s]')
        axes[0].set_ylabel('položaj [m]')

        axes[1].plot(self.t, self.vx)
        axes[1].set_xlabel('vrijeme [s]')
        axes[1].set_ylabel('brzina [m/s]')

        axes[2].plot(self.t, self.ax)
        axes[2].set_xlabel('vrijeme [s]')
        axes[2].set_ylabel('akceleracija [m/s^2]')

        plt.show()


