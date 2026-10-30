# IPPO

**Impartial Punch Performance Officials**

Three ML judges, three scoring philosophies (clean punching, pressure, defense), one scorecard. When they split, you see why.

> 🚧 Work in progress — currently building the dataset (Phase 1).

## The idea

Professional boxing is scored by three judges using the 10-point must system, and they often disagree. IPPO builds three ML judges, each trained to weight the official criteria differently:

| Judge | Philosophy |
|---|---|
| **The Puncher's Judge** | Clean, effective punching |
| **The Pressure Judge** | Effective aggression and ring generalship |
| **The Defense Judge** | Defense and making the opponent miss |

Each judge scores every round, the cards are totalled into a decision (unanimous, split, majority or draw), and SHAP explanations show *why* the judges disagreed.

## Related work

AI boxing judging already exists — The Ring's "AI 4th Judge" and Jabbr's DeepStrike both score fights from video. IPPO differs by:

- using **multiple judges with explicit, different philosophies** instead of one black box
- **explaining split decisions** round by round
- evaluating against the **human ceiling** (how often real judges agree with each other)
- being open and reproducible

## Roadmap

- [ ] **Phase 1 — Data:** fight list, official scorecards, hand-annotated round stats
- [ ] **Phase 2 — Baselines:** simple rules, logistic regression, LightGBM (split by fight)
- [ ] **Phase 3 — Three judges:** distinct feature sets and weightings
- [ ] **Phase 4 — Evaluation:** agreement vs real judges, Cohen's kappa, SHAP, controversial decisions revisited
- [ ] **Phase 5 — Vision:** pose estimation → punch detection → automatic round stats
- [ ] **Phase 6 — Demo:** Streamlit app ("be the 4th judge")

## Repo layout

```
data/        raw + processed data (see data/README.md)
annotate/    round-logging tool
src/         features, judges, training, evaluation, explanations
vision/      pose + punch detection (phase 5)
app/         Streamlit demo
notebooks/   exploration only
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
