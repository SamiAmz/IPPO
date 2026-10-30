# IPPO

**Impartial Punch Performance Officials**

Three differently trained ML judges score boxing rounds from the same stats, and SHAP reveals what each one learned to value and why they split.


## The idea

Professional boxing is scored by three judges using the 10-point must system. They all apply the same criteria, yet they often disagree, because each weighs those criteria a little differently, and nobody can see how.

IPPO recreates that with three ML judges. None of them is told what to care about. All three see **every** round stat (power and volume, landed and thrown, accuracy, knockdowns, pressure, opponent's misses) and differ only in how they learn:

| Judge | Model | How it reads a round |
|---|---|---|
| **Judge 1** | Logistic regression | Steady and additive: every stat adds or subtracts a fixed amount |
| **Judge 2** | LightGBM (gradient-boosted trees) | Rule-like: picks up interactions such as "volume counts, unless the other guy landed the bigger shots" |
| **Judge 3** | Small neural network | Finds smoother, subtler patterns across all the stats |

Each round in the dataset has three official scores, and each judge trains on a different mix of those real judges' cards, so it picks up its own scoring tendencies the way human judges do.

Each judge scores every round, the cards are totalled into a decision (unanimous, split, majority or draw), and SHAP shows what each judge actually learned to value. The scoring styles are discovered, not designed.

**The core question:** do three independently trained ML judges disagree the way humans do, and on the same rounds?

## Related work

AI boxing judging already exists — The Ring's "AI 4th Judge" and Jabbr's DeepStrike both score fights from video. IPPO differs by:

- using **a panel of three independently trained judges** instead of one black box
- **explaining split decisions** round by round
- evaluating against the **human ceiling** (how often real judges agree with each other)
- being open and reproducible

## Roadmap

- [ ] **Phase 1 — Data:** fight list, official scorecards, hand-annotated round stats
- [ ] **Phase 2 — Baselines:** simple rules, logistic regression, LightGBM (split by fight)
- [ ] **Phase 3 — Three judges:** three model types on the same features, each trained on a different mix of real judges' cards
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
