PHY368 Student Handout

Moseley’s law and Einstein coefficients | 13 October 2026

Keep this beside you during the lecture and use it to revise before the midterm. Use the worked examples to practise selecting the correct equation and stating its assumptions.

Before class

Review E = hν = hc/λ, K and L shell labels, and exponential functions. The Planck and Boltzmann expressions are supplied below; you are not asked to derive them in this session.

Part 1. Moseley's law

1.1 Why it matters

In 1913–14 Moseley measured the K and L X-ray lines of many elements and found that √ν rises linearly with an integer, the atomic number Z. Z became a measurable quantity: the nuclear charge. Ordering elements by Z, not atomic weight, places Co before Ni, Ar before K and Te before I, and the gaps at Z = 43, 61, 72 and 75 pointed to elements found later (Tc, Pm, Hf, Re).

1.2 Derivation of the Kα energy

A K-shell vacancy is filled by an L-shell electron (Kα, n = 2 → 1). Other electrons screen the nucleus, so use an effective charge Z − σ in a hydrogen-like model:

Eₙ ≈ −13.6 (Z−σ)² / n²  eV

Eγ = E₂ − E₁ ≈ 13.6 (Z−σ)² (1 − ¼) eV = 10.2 (Z−σ)² eV

After the vacancy forms, one K electron remains and screens about one unit of charge, so σ ≈ 1:

E(Kα) ≈ 10.2 (Z−1)² eV

Since E = hν, √ν = a (Z − σ) with a = √(10.2 eV / h) ≈ 4.97 × 10⁷ Hz^½.

1.3 Reading the plot

Axes: Z (dimensionless) horizontal, √ν (Hz^½) vertical; use one line series (Kα) for all elements.

Slope = a. Horizontal intercept = σ. Vertical intercept = −aσ (it is not the screening constant).

Mixing Kα and Kβ points breaks the straight line.

1.4 How good is it?

| Element | Z | Tabulated Kα₁ (keV) | Model (keV) | Error |

| --- | --- | --- | --- | --- |

| Ti | 22 | 4.511 | 4.498 | −0.3% |

| Fe | 26 | 6.404 | 6.375 | −0.5% |

| Cu | 29 | 8.048 | 7.997 | −0.6% |

| Mo | 42 | 17.479 | 17.146 | −1.9% |

| Ag | 47 | 22.163 | 21.583 | −2.6% |

| W | 74 | 59.318 | 54.356 | −8.4% |



For the sampled elements Ti to Zn, the model error is below 1%. It underestimates every value in this table. The fitted σ values absorb neglected screening and relativistic effects; they are not direct measurements of screening. Data: LBNL X-Ray Data Booklet, Table 1-2.

1.5 Not every vacancy gives an X-ray

A vacancy can also relax by Auger emission, where the energy goes to another electron that leaves the atom. The formula gives the photon energy for the case where the radiative transition happens, not how often.

1.6 Worked example: copper (Z = 29)

Z − σ = 28.

E ≈ 10.2 × 784 = 7996.8 eV ≈ 8.00 keV.

λ = hc/E = 1239.84 eV·nm / 7996.8 eV ≈ 0.155 nm.

ν = E/h ≈ 1.93 × 10¹⁸ Hz, so √ν ≈ 1.39 × 10⁹ Hz^½ (check: a × 28).

Tabulated Cu Kα₁ ≈ 8.048 keV: the model is 0.6% low.

Part 2. Absorption, spontaneous and stimulated emission

| Process | Atom | Photons | Notes |

| --- | --- | --- | --- |

| Absorption | 1 → 2 | −1 | needs radiation |

| Spontaneous emission | 2 → 1 | +1 | random direction; no trigger |

| Stimulated emission | 2 → 1 | +1 | same mode as triggering photon |



2.1 Symbols

| Symbol | Meaning | Unit |

| --- | --- | --- |

| N₁, N₂ | populations of lower and upper level | number or per volume |

| g₁, g₂ | degeneracies: states in each level | – |

| A₂₁ | spontaneous-emission rate per atom | s⁻¹ |

| B₁₂, B₂₁ | absorption and stimulated-emission coefficients | m³·J⁻¹·s⁻² |

| u(ν₀) | radiation energy density per unit ordinary frequency at ν₀ | J·s·m⁻³ |

| B·u | rate per atom | s⁻¹ |



Assumptions: isotropic radiation; narrow line so u is nearly constant across it; closed two-level system, no collisions or extra pumping.

2.2 Rate equation

dN₂/dt = N₁B₁₂u − N₂B₂₁u − N₂A₂₁

One gain term, two loss terms. If the radiation is removed, both terms containing u vanish; spontaneous emission remains.

Part 3. The Einstein relations

Step 1. At equilibrium dN₂/dt = 0:

N₁B₁₂u = N₂(A₂₁ + B₂₁u)  ⇒  u = A₂₁ / [(N₁/N₂)B₁₂ − B₂₁]

Step 2. Boltzmann ratio (supplied):

N₂/N₁ = (g₂/g₁) e^(−x),   x = hν₀/kBT

u = A₂₁ / [(g₁/g₂)B₁₂ eˣ − B₂₁] = (A₂₁/B₂₁) / [(g₁B₁₂/g₂B₂₁) eˣ − 1]

Step 3. Planck (supplied, per unit ordinary frequency): u = (8πhν₀³/c³)/(eˣ − 1). Matching for all T gives:

g₁B₁₂ = g₂B₂₁          A₂₁/B₂₁ = 8πhν₀³/c³

B₁₂ = B₂₁ only when g₁ = g₂.

Derived at equilibrium; A and B are atomic properties, so the rate equation applies in any radiation field in this model.

Without the stimulated term the algebra gives Wien's form, which is wrong at low frequency.

If u is per angular frequency, the prefactor changes (ħω³/π²c³); do not mix conventions.

3.1 Stimulated against spontaneous, and gain

B₂₁u / A₂₁ = 1/(eˣ − 1)  in thermal radiation

500 nm at 300 K: x ≈ 96, ratio ≈ 2×10⁻⁴². Spontaneous emission dominates.

500 nm at 6000 K: x ≈ 4.8, ratio ≈ 0.008.

3 cm (10 GHz) at 300 K: x ≈ 0.0016, ratio ≈ 625. Stimulated emission exceeds spontaneous emission for an excited atom in this thermal field. Net amplification still requires population inversion.

Net absorption − stimulated emission = B₁₂u (N₁ − (g₁/g₂)N₂). Gain needs N₂/g₂ > N₁/g₁: a population inversion, impossible in thermal equilibrium.

Part 4. Radiative decay

For one radiative channel, with no incident radiation, collisions or feeding from above: dN₂/dt = −A₂₁N₂, so

N₂(t) = N₂(0) e^(−A₂₁t),   τ = 1/A₂₁

At t = τ, 36.8% remain; 2τ, 13.5%; 3τ, 5.0%.

Half-life t½ = τ ln 2 = 0.693 τ.

Several channels: τ = 1/ΣA, branching b_i = A_i/ΣA.

With nonradiative loss, Γ = ΣA + kₙᵣ and τₚₒₚ = 1/Γ. The radiative lifetime is τᵣₐd = 1/ΣA. The photon yield is ΣA/Γ.

For constant decay rates, τ is both the population e-folding time and the mean waiting time. Individual atoms decay at random times.

4.1 Typical radiative lifetimes

| Transition | A₂₁ (s⁻¹) | τ |

| --- | --- | --- |

| H Lyman-α (2p → 1s) | ≈ 6.265×10⁸ | ≈ 1.6 ns |

| Na D lines | ≈ 6.15×10⁷ | ≈ 16 ns |

| Metastable levels | very small | µs to seconds or longer |



4.2 Worked example: two channels

A(a) = 4.0×10⁷ s⁻¹, A(b) = 1.0×10⁷ s⁻¹.

A(total) = 5.0×10⁷ s⁻¹; τ = 20 ns.

b(a) = 0.80, b(b) = 0.20.

After 40 ns: e⁻² = 0.135, so 13.5% remain.

Common error: 1/A(a) = 25 ns ignores channel b.

Seven errors to avoid

Calling the vertical intercept the screening constant (it is −aσ).

Treating 10.2(Z−1)² as exact.

Mixing Kα and Kβ points on one plot.

Treating B as a rate (the rate is B·u).

Using 1/A of one channel when there are several.

Confusing τ with half-life.

Mixing u per ν and per ω; forgetting g₁B₁₂ = g₂B₂₁.

Constants

h = 6.626×10⁻³⁴ J·s;  hc = 1239.84 eV·nm;  1 eV = 1.602×10⁻¹⁹ J;  kB = 1.381×10⁻²³ J/K = 8.617×10⁻⁵ eV/K;  c = 2.998×10⁸ m/s;  Hartree energy ≈ 27.2114 eV (Eₕ/2 = 13.6 eV).

Further reading

C. J. Foot, Atomic Physics (course edition 2005): introductory atomic structure and radiation topics.

W. Demtröder, Atoms, Molecules and Photons, 2nd edition (2010); A. P. Thorne, Spectrophysics, 2nd edition (1988): radiation and spectroscopy topics.

NIST X-ray Transition Energies Database and NIST Atomic Spectra Database for measured energies and transition rates.

B. H. Bransden and C. J. Joachain, Physics of Atoms and Molecules, 2nd edition: Chapters 1 and 4. Prescribed course printing: 2008.

Tabulated Kα₁ energies: https://xdb.lbl.gov/Section1/Table_1-2.pdfH 2p and Na 3p rates: NIST persistent-line tables. https://physics.nist.gov/PhysRefData/Handbook/Tables/hydrogentable3.htmhttps://physics.nist.gov/PhysRefData/Handbook/Tables/sodiumtable3.htm

After class

Estimate iron's Kα energy (Z = 26). Then find τ and the branching fractions for an upper level with rates 6×10⁷ and 2×10⁷ s⁻¹. Next class: which hydrogen transitions have nonzero electric-dipole amplitude? (parity, selection rules, π/σ components).

Atomic units

Atomic units set ℏ = mₑ = e = 4πε₀ = 1 numerically. The unit of length is a₀ ≈ 0.0529177 nm and the unit of energy is Eₕ ≈ 27.2114 eV. For a hydrogen-like atom with a fixed nucleus, Eₙ/Eₕ = −Z²/(2n²). In the screened Kα teaching model, replace Z by Z−σ. The n = 2 to n = 1 energy difference is (3/8)Eₕ(Z−σ)² ≈ 10.2(Z−σ)² eV.

Optional extension on natural linewidth

For a stable lower level, exponential upper-level population decay and no additional dephasing, the natural line has frequency FWHM Δν = 1/(2πτ). A population lifetime of 20 ns gives Δν ≈ 7.96 MHz. If both levels have finite population lifetimes, Δν = (1/τᵤ + 1/τₗ)/(2π), before adding other broadening mechanisms.
