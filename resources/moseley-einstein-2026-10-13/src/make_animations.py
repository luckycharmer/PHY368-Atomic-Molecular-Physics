"""PHY368 animations: K-alpha vacancy filling, three radiation processes,
ensemble radiative decay with branching, and Moseley plot build-up.

Run:  python src/make_animations.py
Writes GIF + MP4 to animations/ and a key-frame PNG to static_fallbacks/.
The diagrams are schematic. The Moseley plot uses LBNL Table 1-2 data.
"""
import csv, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANIM = os.path.join(ROOT, "animations"); STAT = os.path.join(ROOT, "static_fallbacks")
os.makedirs(ANIM, exist_ok=True); os.makedirs(STAT, exist_ok=True)
NAVY, TEAL, ORANGE, GREY, PURPLE = "#14213D", "#0F8B8D", "#E07A1F", "#5B6573", "#7B4FA0"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})
FPS = 15

def ease(t):
    t = np.clip(t, 0, 1); return t * t * (3 - 2 * t)
def seg(f, a, b):
    return ease((f - a) / max(b - a, 1e-9))
def wave(ax, x0, y0, ang, length, phase, color=ORANGE, amp=0.18, lw=2.5, k=9.0):
    s = np.linspace(0, length, 80)
    env = np.sin(np.pi * s / length) ** 0.5
    px = x0 + s * np.cos(ang) - amp * env * np.sin(k * s - phase) * np.sin(ang)
    py = y0 + s * np.sin(ang) + amp * env * np.sin(k * s - phase) * np.cos(ang)
    ax.plot(px, py, color=color, lw=lw, solid_capstyle="round")
def save(fig, update, frames, name, key_frame):
    anim = FuncAnimation(fig, update, frames=frames, interval=1000 / FPS)
    anim.save(os.path.join(ANIM, name + ".gif"), writer=PillowWriter(fps=FPS))
    try:
        anim.save(os.path.join(ANIM, name + ".mp4"), writer=FFMpegWriter(fps=FPS, bitrate=1800))
    except Exception as e:
        print("MP4 skipped:", e)
    update(key_frame)
    fig.savefig(os.path.join(STAT, name + ".png"), dpi=110)
    plt.close(fig); print("done", name)

# ---------------------------------------------------------------- 1. vacancy
def vacancy():
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=100)
    yK, yL = 1.3, 4.0
    K2, L1, L2, KV = 5.8, 3.4, 6.6, 4.2          # electron x-positions; K vacancy x
    def base(title):
        ax.clear(); ax.set_xlim(0, 10); ax.set_ylim(0, 6.2); ax.axis("off")
        ax.hlines(yK, 2, 8, color=NAVY, lw=3); ax.hlines(yL, 2, 8, color=NAVY, lw=3)
        ax.text(1.85, yK, "K  (n = 1)", ha="right", va="center", color=NAVY)
        ax.text(1.85, yL, "L  (n = 2)", ha="right", va="center", color=NAVY)
        ax.text(5, 5.85, title, ha="center", color=NAVY, fontsize=14, fontweight="bold")
        ax.text(5, 0.2, "One vacancy, two routes.   Photon energy: E ≈ 10.2 (Z−1)² eV", ha="center", color=GREY, fontsize=11)
    def e(x, y, **k):
        ax.plot(x, y, "o", color=k.pop("color", TEAL), ms=13, **k)
    def update(f):
        route = "photon" if f < 120 else "auger"
        g = f if f < 120 else f - 120
        base("Kα X-ray emission" if route == "photon" else "Auger emission (no photon)")
        e(K2, yK)
        if g < 22:
            p = seg(g, 0, 18)
            ax.plot(0.3 + p * (KV - 0.3), 0.3 + p * (yK - 0.3), "o", color=GREY, ms=9)
            ax.text(0.2, 2.3, "energetic electron\nor X-ray photon", color=GREY, fontsize=10)
            e(KV, yK); e(L1, yL); e(L2, yL); return
        q = seg(g, 22, 44)
        if q < 1:
            e(KV + q * 4.8, yK + q * 3.6, alpha=1 - 0.8 * q)
            ax.text(8.0, 4.9, "K electron ejected", color=TEAL, fontsize=10, ha="center")
        p = seg(g, 50, 80)
        ex, ey = L2 + p * (KV - L2), yL + p * (yK - yL)
        e(ex, ey)                                      # L electron falling into K
        if p < 1:
            ax.plot(KV, yK, "o", mfc="white", mec=ORANGE, mew=3, ms=15)
            ax.text(KV, 0.7, "K vacancy", color=ORANGE, ha="center", fontsize=11)
        if route == "photon":
            e(L1, yL)
            if p >= 1:
                ph = seg(g, 80, 118)
                wave(ax, 5.0 + 3.3 * ph, 2.6 + 1.2 * ph, np.deg2rad(20), 1.9, 14 * ph)
                ax.text(7.7, 5.2, "Kα photon:  E = E_L − E_K", color=ORANGE, ha="center", fontsize=11)
        else:
            if p < 1:
                e(L1, yL)
            else:
                a = seg(g, 80, 118)
                e(L1 - a * 3.2, yL + a * 1.9, color=ORANGE)
                ax.text(1.6, 5.3, "Auger electron", color=ORANGE, ha="center", fontsize=11)
    save(fig, update, 240, "01_kalpha_vacancy", 100)

# ---------------------------------------------------------------- 2. three processes
def processes():
    fig, axs = plt.subplots(1, 3, figsize=(10.5, 4.4), dpi=100)
    names = ["Absorption", "Spontaneous emission", "Stimulated emission"]
    y1, y2, xa, xb = 1.5, 6.0, 2.6, 7.4
    def base(ax, t, line):
        ax.clear(); ax.set_xlim(0, 10); ax.set_ylim(0, 8.6); ax.axis("off")
        ax.hlines(y1, xa, xb, color=NAVY, lw=3); ax.hlines(y2, xa, xb, color=NAVY, lw=3)
        ax.text(xa - 0.15, y1, "E₁", ha="right", va="center", color=NAVY); ax.text(xa - 0.15, y2, "E₂", ha="right", va="center", color=NAVY)
        ax.set_title(t, color=NAVY, fontweight="bold", fontsize=13); ax.text(5, 0.2, line, ha="center", color=GREY, fontsize=9.5)
    def update(f):
        t = f % 150
        ax = axs[0]; base(ax, names[0], "photons:  1 → 0")
        yy = y1 + (y2 - y1) * seg(t, 55, 78)
        if t < 55:
            wave(ax, -1.5 + 6.5 * seg(t, 0, 55), 3.75, 0, 1.8, 18 * t / 15)
        ax.plot(5, yy if t >= 55 else y1, "o", color=TEAL, ms=14)
        ax = axs[1]; base(ax, names[1], "photons:  0 → 1  (random time, random direction)")
        yy = y2 - (y2 - y1) * seg(t, 62, 84)
        ax.plot(5, y2 if t < 62 else yy, "o", color=TEAL, ms=14)
        if t >= 84:
            p = seg(t, 84, 148); wave(ax, 5.3 + 3.0 * p, 2.0 + 2.6 * p, np.deg2rad(40), 1.8, 18 * t / 15)
        ax = axs[2]; base(ax, names[2], "photons:  1 → 2  (same mode, in phase)")
        yy = y2 - (y2 - y1) * seg(t, 55, 77)
        ax.plot(5, y2 if t < 55 else yy, "o", color=TEAL, ms=14)
        if t < 55:
            wave(ax, -1.5 + 6.5 * seg(t, 0, 55), 3.75, 0, 1.8, 18 * t / 15)
        else:
            x = 5.0 + 4.5 * seg(t, 55, 148)
            wave(ax, x, 3.95, 0, 1.8, 18 * t / 15); wave(ax, x, 3.55, 0, 1.8, 18 * t / 15)
    fig.tight_layout()
    save(fig, update, 300, "02_three_processes", 135)

# ---------------------------------------------------------------- 3. ensemble decay
def decay():
    rng = np.random.default_rng(368)
    N, tau, pa = 400, 20.0, 0.80
    td = rng.exponential(tau, N); br = rng.random(N) < pa
    fig, (axa, axp) = plt.subplots(1, 2, figsize=(10.5, 4.6), dpi=100, gridspec_kw={"width_ratios": [1, 1.25]})
    gx, gy = np.meshgrid(np.arange(20), np.arange(20)); gx, gy = gx.ravel(), gy.ravel()
    tt = np.linspace(0, 100, 300)
    def update(f):
        t = f * 100 / 120.0
        dec = td <= t; exc = ~dec
        axa.clear(); axa.set_xlim(-1, 20); axa.set_ylim(-5, 20); axa.axis("off")
        axa.scatter(gx[exc], gy[exc], s=70, color=ORANGE)
        axa.scatter(gx[dec & br], gy[dec & br], s=70, color=TEAL)
        axa.scatter(gx[dec & ~br], gy[dec & ~br], s=70, color=PURPLE)
        axa.set_title(f"400 atoms,  t = {t:5.1f} ns", color=NAVY, fontweight="bold")
        axa.text(-0.5, -2.0, "● excited", color=ORANGE, fontsize=10); axa.text(5.5, -2.0, "● decayed by a (4×10⁷ s⁻¹)", color=TEAL, fontsize=10)
        axa.text(5.5, -3.6, "● decayed by b (1×10⁷ s⁻¹)", color=PURPLE, fontsize=10)
        axp.clear(); axp.plot(tt, np.exp(-tt / tau), "--", color=NAVY, lw=2, label=r"theory  $e^{-t/\tau}$,  τ = 20 ns")
        ts = np.linspace(0, t, 200); fr = [(td > s_).mean() for s_ in ts]
        axp.plot(ts, fr, color=ORANGE, lw=3, label="this ensemble (random decays)")
        axp.axvline(tau, color=GREY, ls=":"); axp.axhline(np.exp(-1), color=GREY, ls=":")
        axp.text(tau + 1.5, 0.9, "t = τ: 36.8 %", color=GREY, fontsize=10)
        axp.set_xlim(0, 100); axp.set_ylim(0, 1.05); axp.set_xlabel("time (ns)"); axp.set_ylabel("fraction still excited")
        axp.legend(frameon=False, loc="upper right", fontsize=10); axp.spines[["top", "right"]].set_visible(False)
        axp.set_title(f"decayed so far:  a = {int((dec & br).sum())},  b = {int((dec & ~br).sum())}   (expect 0.80 : 0.20)", fontsize=10.5, color=NAVY)
    fig.tight_layout()
    save(fig, update, 121, "03_ensemble_decay", 60)

# ---------------------------------------------------------------- 4. Moseley build-up
def moseley():
    rows = list(csv.DictReader(open(os.path.join(ROOT, "data", "kalpha_tabulated.csv"))))
    el = [r["element"] for r in rows]; Z = np.array([int(r["Z"]) for r in rows]); E = np.array([float(r["K_alpha1_eV"]) for r in rows])
    fig, ax = plt.subplots(figsize=(8, 4.8), dpi=100)
    zz = np.linspace(15, 78, 100)
    def update(f):
        ax.clear(); n = min(len(Z), f // 6 + 1) if f < 60 else len(Z)
        ax.set_xlim(15, 78); ax.set_ylim(40, 270)
        ax.set_xlabel("Atomic number Z"); ax.set_ylabel(r"$\sqrt{E}$  (eV$^{1/2}$)")
        ax.spines[["top", "right"]].set_visible(False)
        ax.plot(Z[:n], np.sqrt(E[:n]), "o", color=ORANGE, ms=10, label="tabulated Kα₁")
        for i in range(n): ax.annotate(el[i], (Z[i], np.sqrt(E[i])), xytext=(-6, 9), textcoords="offset points", color=NAVY, fontweight="bold")
        if f >= 60:
            p = seg(f, 60, 85); zl = zz[: max(2, int(p * len(zz)))]
            ax.plot(zl, np.sqrt(10.2) * (zl - 1), color=TEAL, lw=3, label=r"model  $\sqrt{E}=\sqrt{10.2}\,(Z-1)$")
        if f >= 95:
            ax.text(46, 62, "sampled Ti–Zn: error < 1 %;\nW: 8 % low; screening + relativity", color=GREY, fontsize=11)
        ax.legend(frameon=False, loc="upper left"); ax.set_title("Moseley's plot: a straight line in Z", color=NAVY, fontweight="bold")
    fig.subplots_adjust(left=0.14, right=0.97, bottom=0.15, top=0.90)
    save(fig, update, 120, "04_moseley_buildup", 119)

if __name__ == "__main__":
    vacancy(); processes(); decay(); moseley()
