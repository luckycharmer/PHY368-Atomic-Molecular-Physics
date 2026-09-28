# Lecture 4 — Radiative Decay and Einstein Coefficients

## Central question
Energy differences tell us **where** a spectral line occurs. What determines how rapidly or strongly a transition occurs?

## Learning outcomes
Students should be able to:

1. distinguish absorption, spontaneous emission and stimulated emission;
2. interpret the Einstein (A) and (B) coefficients;
3. calculate radiative lifetimes from decay probabilities;
4. use exponential population decay;
5. connect stimulated emission conceptually to laser action.

## Two-level system

Let

[
E_2>E_1,
]

with

[
E_2-E_1=h
u.
]

Let (ho(
u)) be the spectral energy density of the radiation field per unit frequency.

## Three radiative processes

### Absorption

[
R_{m abs}
=
B_{12}ho(
u)N_1.
]

### Stimulated emission

[
R_{m stim}
=
B_{21}ho(
u)N_2.
]

### Spontaneous emission

[
R_{m sp}
=
A_{21}N_2.
]

The (B)-processes depend on the external radiation field. Spontaneous emission does not require an applied field.

## Spontaneous decay

For one radiative decay channel,

[
rac{dN_2}{dt}
=
-A_{21}N_2.
]

Hence,

[
N_2(t)
=
N_2(0)e^{-A_{21}t}.
]

The radiative lifetime is

[
	au=rac{1}{A_{21}}.
]

If several independent radiative channels are available,

[
A_{m total}=sum_k A_{2k},
]

and

[
	au=rac{1}{A_{m total}}.
]

## Worked example

If

[
A_{21}=2.5	imes10^7,mathrm{s^{-1}},
]

then

[
	au
=
rac{1}{2.5	imes10^7}
=
4.0	imes10^{-8},mathrm s
=
40,mathrm{ns}.
]

After one lifetime,

[
rac{N(	au)}{N_0}
=
e^{-1}
approx0.368.
]

Thus about 36.8% of the original excited population remains.

## Einstein relations

Thermal equilibrium with Planck radiation leads to relations between the Einstein coefficients.

For levels with degeneracies (g_1) and (g_2),

[
g_1B_{12}=g_2B_{21}.
]

With (ho(
u)) defined per unit frequency,

[
rac{A_{21}}{B_{21}}
=
rac{8pi h
u^3}{c^3}.
]

For non-degenerate levels with (g_1=g_2),

[
B_{12}=B_{21}.
]

## Numerical checks

1. (A=2.5	imes10^7,mathrm{s^{-1}}) gives (	au=40,mathrm{ns}).
2. After one lifetime, 36.8% remains.
3. If (	au=50,mathrm{ns}), after (100,mathrm{ns}) the remaining fraction is (e^{-2}approx0.135).
4. If (	au=25,mathrm{ns}), (A=4.0	imes10^7,mathrm{s^{-1}}).
5. If (N_2=2.0	imes10^8) and (A=3.0	imes10^7,mathrm{s^{-1}}),

[
R_{m sp}=6.0	imes10^{15},mathrm{s^{-1}}.
]

6. If (A_1=2.0	imes10^7) and (A_2=3.0	imes10^7,mathrm{s^{-1}}),

[
	au=20,mathrm{ns}.
]

## Conceptual bridge to lasers
Stimulated emission reproduces the frequency, propagation direction, phase relationship and polarization mode associated with the stimulating radiation. Laser action additionally requires appropriate gain and population inversion conditions.

## Reading
**Best match:** W. Demtröder, *Atoms, Molecules and Photons*, Chapter 7, especially §7.1 and §7.1.1.

[Previous](03-moseleys-law.md) · [Topic](../topics/radiative-transitions.md) · [Module 1 overview](../modules/module-1.md)
