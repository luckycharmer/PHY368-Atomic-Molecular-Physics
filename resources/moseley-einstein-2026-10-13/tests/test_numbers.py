"""Run:  python tests/test_numbers.py   (or pytest). Checks selected numerical examples and boundary cases."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
from phy368 import *

def close(a, b, rel=1e-3): assert abs(a - b) <= rel * abs(b), (a, b)

def test_copper():
    E = kalpha_energy_eV(29); close(E, 7996.8); close(wavelength_nm(E), 0.15504, 2e-3)
def test_zinc_iron_molybdenum_line():
    close(kalpha_energy_eV(30), 8578.2); close(kalpha_energy_eV(26), 6375.0)
    close(z_from_energy(17150), 42.005, 1e-3); close(z_from_energy(6400), 26.049, 1e-3)
def test_slope_and_sigma():
    close(moseley_slope_a(), 4.966e7, 1e-3)
    close(effective_sigma(42, 17479.34), 0.604, 2e-2); close(effective_sigma(29, 8047.78), 0.911, 5e-3)
def test_ratio_numbers():
    close(stim_over_spont(500e-9, 300), 2.2e-42, 0.05); close(stim_over_spont(0.03, 300), 625.0, 0.01)
    close(A_over_B21(5.0e14), 7.7258e-14, 1e-3)
def test_degeneracy():
    assert B12_over_B21(2, 6) == 3.0 and B12_over_B21(3, 5) == 5 / 3
    assert net_absorption_factor(1e12, 2e12, 1, 3) > 0 and net_absorption_factor(1e12, 4e12, 1, 3) < 0
def test_decay():
    tau, b = lifetime_and_branching([4e7, 1e7]); close(tau, 20e-9); close(b[0], 0.8); close(b[1], 0.2)
    close(surviving_fraction(40e-9, tau), 0.1353, 1e-3)
    tau3, b3 = lifetime_and_branching([6e7, 3e7, 1e7]); close(tau3, 10e-9); close(surviving_fraction(25e-9, tau3), 0.0821, 2e-3)
    tau_f, bf = lifetime_and_branching([6e7, 2e7]); close(tau_f, 12.5e-9); assert bf == [0.75, 0.25]
    close(40 * math.log(10), 92.1, 1e-3)     # time for 90 % to decay, tau = 40 ns
    tau_nr, bnr = lifetime_and_branching([2e7, 1e7, 2e7]); close(tau_nr, 20e-9); close(1 / 3e7, 33.3e-9, 2e-3)

def test_zero_rates_and_low_temperature():
    tau, b = lifetime_and_branching([0, 0, 0])
    assert math.isinf(tau) and b == [0, 0, 0]
    assert stim_over_spont(100e-9, 100) == 0.0
    try:
        lifetime_and_branching([-1, 2])
    except ValueError:
        pass
    else:
        raise AssertionError("Negative rates must be rejected")

if __name__ == "__main__":
    n = 0
    for k, v in list(globals().items()):
        if k.startswith("test_"): v(); n += 1; print("ok", k)
    print(n, "checks passed")
