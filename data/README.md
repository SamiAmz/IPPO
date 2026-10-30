# Data

## Files

| File | What it is |
|---|---|
| `raw/fights.csv` | One row per fight in the dataset |
| `raw/scorecards.csv` | Official round-by-round scores, one row per judge per round |
| `raw/annotations/<fight_id>_r<round>.csv` | Timestamped events logged with the annotation tool |
| `processed/rounds.csv` | One row per round: features + labels (built from the above) |

## `raw/fights.csv`

| Column | Example | Notes |
|---|---|---|
| `fight_id` | `usyk-fury-1` | lowercase, `fighterA-fighterB[-n]` |
| `date` | `2024-05-18` | ISO format |
| `fighter_a` / `fighter_b` | `Oleksandr Usyk` | A = first-named fighter |
| `weight_class` | `heavyweight` | |
| `scheduled_rounds` | `12` | |
| `result` | `a` / `b` / `draw` | |
| `decision_type` | `UD` / `SD` / `MD` / `D` | |
| `controversial` | `y` / `n` | widely disputed decision |
| `video_available` | `y` / `n` | legally watchable full rounds |
| `source` | URL | where the result was checked |

## `raw/scorecards.csv`

| Column | Example |
|---|---|
| `fight_id` | `usyk-fury-1` |
| `round` | `7` |
| `judge_name` | `Judge Name` |
| `score_a` / `score_b` | `10` / `9` |
| `source` | URL |

## Annotation event codes

| Key | Event |
|---|---|
| `j` / `J` | jab thrown / landed |
| `p` / `P` | power punch thrown / landed |
| `b` | body shot landed |
| `k` | knockdown |
| `f` | pressing forward |
| `c` | clinch |

## Sources & rules

- Scorecards are typed in by hand from public sources; every row records its source.
- No fight footage is stored in this repo.
