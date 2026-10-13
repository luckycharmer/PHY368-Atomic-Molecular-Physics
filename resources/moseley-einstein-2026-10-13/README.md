# Moseley’s law and Einstein coefficients

PHY368, COMSATS University Islamabad. Lecture of 13 October 2026.

This module connects characteristic X-ray energies with absorption, emission, lifetime and branching. The screened model is approximate. Reference line energies and synthetic examples are identified separately.

## Open the lab

Download this module and open `web/index.html` in a browser. It works offline.

## Run the notebook

From this module’s root directory:

```bash
python -m pip install -r requirements.txt
jupyter lab notebooks/PHY368_explorer.ipynb
python tests/test_numbers.py
```

The notebook also runs with `notebooks/` as its working directory. Zero total decay rate produces no decay and undefined branching. The thermal radiation calculation handles very small occupation factors without overflow.

## Files

- `src/phy368.py`: numerical functions and input checks.
- `src/make_animations.py`: regenerates four GIF/MP4 animations and stills. MP4 export requires ffmpeg.
- `data/kalpha_tabulated.csv` and `data/SOURCES.md`: reference data and provenance.
- `notebooks/PHY368_explorer.ipynb`: interactive calculations.
- `web/index.html`: self-contained offline lab.
- `docs/index.html`: matching copy for static hosting.
- `tests/test_numbers.py`: selected worked examples and boundary conditions.
- `animations/` and `static_fallbacks/`: demonstrations and stills.
- `student/`: lecture notes, practice and reading guide for students.

## Physics conventions

Radiation density is per unit ordinary frequency. The Planck occupation ratio assumes blackbody radiation. Population lifetime is `1/(sum(A) + k_nr)`; radiative lifetime is `1/sum(A)`. Inversion limits refer to steady incoherent radiative pumping of the stated two-level model. The model residual must not be interpreted as an independent measurement of screening.

## Reuse

The existing MIT licence applies to this module’s code. Reference data retain their source attribution. The repository is a course companion and does not replace the approved syllabus.
