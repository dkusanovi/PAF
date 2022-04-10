import harmonic_oscillator as ho


ho1 = ho.HarmonicOscillator(5, 0, 15, 2, 0.1)
ho1.set_initial_conditions(5, 0, 10, 15, 2, 0.1)
ho1.period_n(2)
ho1.period_a()
ho1.reset()

ho2 = ho.HarmonicOscillator(5, 0, 15, 2, 0.01)
ho2.set_initial_conditions(5, 0, 10, 15, 2, 0.01)
ho2.period_n(2)
ho2.period_a()
ho2.reset()

ho3 = ho.HarmonicOscillator(5, 0, 15, 2, 0.001)
ho3.set_initial_conditions(5, 0, 10, 15, 2, 0.001)
ho3.period_n(2)
ho3.period_a()