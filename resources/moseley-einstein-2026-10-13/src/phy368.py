"""Small, tested helper functions used by the PHY368 notebook and checks."""
import math

h = 6.62607015e-34; c = 2.99792458e8; kB = 1.380649e-23; eV = 1.602176634e-19
HC_EV_NM = 1239.84          # eV nm, as used in the lecture
COEFF = 10.2                # eV: (3/4) * 13.6 eV

def kalpha_energy_eV(Z, sigma=1.0):
    """Screened hydrogenic Kα estimate, E = 10.2 (Z - sigma)^2 eV."""
    return COEFF * (Z - sigma) ** 2

def wavelength_nm(E_eV):
    return HC_EV_NM / E_eV

def z_from_energy(E_eV, sigma=1.0):
    """Invert the Kα estimate: Z = sigma + sqrt(E / 10.2 eV)."""
    return sigma + math.sqrt(E_eV / COEFF)

def effective_sigma(Z, E_eV):
    """sigma = Z - sqrt(E/10.2 eV) from a measured Kα energy."""
    return Z - math.sqrt(E_eV / COEFF)

def moseley_slope_a():
    """a = sqrt(10.2 eV / h) in Hz^(1/2) per unit Z."""
    return math.sqrt(COEFF * eV / h)

def stim_over_spont(wavelength_m, T):
    """B21 u / A21 = 1/(exp(x) - 1), x = h c / (lambda kB T)."""
    x = h * c / (wavelength_m * kB * T)
    return 0.0 if x > 700 else 1.0 / math.expm1(x)

def A_over_B21(nu):
    """A21/B21 = 8 pi h nu^3 / c^3 (u per unit ordinary frequency)."""
    return 8 * math.pi * h * nu ** 3 / c ** 3

def B12_over_B21(g1, g2):
    return g2 / g1

def lifetime_and_branching(rates):
    """Population lifetime and fractions for all supplied loss rates (s^-1).
    All-zero input returns (inf, zero placeholders); branching is undefined.
    """
    if not rates or any(r < 0 for r in rates):
        raise ValueError("Supply a nonempty sequence of nonnegative decay rates")
    total = sum(rates)
    if total == 0:
        return math.inf, [0.0 for r in rates]
    return 1.0 / total, [r / total for r in rates]

def surviving_fraction(t, tau):
    return math.exp(-t / tau)

def net_absorption_factor(N1, N2, g1, g2):
    """N1 - (g1/g2) N2 : positive means net absorption, negative means gain."""
    return N1 - (g1 / g2) * N2
