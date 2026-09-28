# Lecture 4 — Radiative Decay and Einstein Coefficients

## Central question
Energy differences tell us **where** a spectral line occurs. What determines whether a transition occurs rapidly, slowly, strongly or weakly?

For (E_2>E_1):
[
E_2-E_1=h\nu.
]

## Three radiative processes
Absorption:
[
R_{abs}=B_{12}\rho(\nu)N_1.
]

Stimulated emission:
[
R_{stim}=B_{21}\rho(\nu)N_2.
]

Spontaneous emission:
[
R_{sp}=A_{21}N_2.
]

For a single spontaneous decay channel:
[
\frac{dN_2}{dt}=-A_{21}N_2
]
so
[
N_2(t)=N_2(0)e^{-A_{21}t},qquad
\tau=\frac1{A_{21}}.
]

## Worked example
If
[
A_{21}=2.5\times10^7\,\mathrm{s^{-1}},
]
then
[
\tau=4.0\times10^{-8}\,\mathrm{s}=40\,\mathrm{ns}.
]

After one lifetime:
[
\frac{N(\tau)}{N_0}=e^{-1}\approx0.368.
]

## Numerical practice
1. (A_{21}=2.5\times10^7\,\mathrm{s^{-1}}): **(	au=40) ns**
2. After one lifetime: **36.8% remains**
3. (	au=50) ns, (t=100) ns: **13.5% remains**
4. (	au=25) ns: **(A=4.0\times10^7\,\mathrm{s^{-1}})**
5. If (N_2=2.0\times10^8) and (A=3.0\times10^7\,\mathrm{s^{-1}}): **(R_{sp}=6.0\times10^{15}\,\mathrm{s^{-1}})**
6. Two channels (A_1=2.0\times10^7), (A_2=3.0\times10^7\,\mathrm{s^{-1}}): **(	au=20) ns**

## Reading
Demtröder, Chapter 7, especially §7.1 and §7.1.1.

[Topic](../topics/radiative-transitions.md) · [Previous](03-moseleys-law.md) · [Next](05-atomic-units-hydrogen.md)
