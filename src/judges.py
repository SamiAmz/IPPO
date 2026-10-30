"""The three IPPO judges.

All three see the same round stats; none is told what to value. They differ in how they learn:
  - judge 1: logistic regression
  - judge 2: LightGBM (gradient-boosted trees)
  - judge 3: small neural network
Each trains on a different mix of the real judges' cards, so each picks up its own scoring tendencies.

Implemented in Phase 3.
"""
