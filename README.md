# Strathmore Lost and Found AI prototype

The course-named public assessment repository is [SemProject_MLEngine](https://github.com/nimrod-kobia/SemProject_MLEngine). This `AI-project` repository also contains the Android starter and prototype API. Both repositories carry the current Delhi notebook workflow; use the course-named repository for the lecturer's required submission.

## Project objective

Compare one lost-item report with one found-item report and suggest pairs worth human review. A score never establishes ownership; authorised Lost and Found staff must verify a claim before an item is released.

## CAT 2 definition

**AI Application: Classification**

**Algorithm/Approach: Logistic Regression**

The supervised model classifies a report pair as `1 = match` or `0 = non-match`. Start with [LogisticRegression_Base.ipynb](LogisticRegression_Base.ipynb), which now shows **real Delhi found-item data -> cleaning and EDA -> synthetic lost claims -> constructed pair labels -> Logistic Regression -> grouped validation**. Its model metrics are for constructed labels, not real campus performance.

The Delhi source contains **13,713 real found-item records**, but no linked lost claims or confirmed handovers. `scripts/create_delhi_experiment.py` reproducibly creates 120 **fictional** lost claims and 360 pairs: 120 positives by construction and 240 assumed negatives. These claims are not Delhi Metro or Strathmore reports. Different source rows are not verified different physical items, so the model score cannot establish real matching accuracy. The raw CSV and all Delhi-derived row-level outputs stay local and Git-ignored. See [dataset provenance](docs/DATASET.md).

## Existing baseline and datasets

The manually weighted matcher in `matching_system/matcher.py` is retained as the **Rule-Based Baseline**. It is not trained ML and still powers the small prototype API. The Logistic Regression experiment is offline; the API and Android starter do not use it yet.

`matching_system_testing.ipynb` is a separate engineering notebook. `trial.ipynb` contains earlier exploration and historical outputs; use the CAT 2 notebook for current assessed results.

* `data/raw/campus/synthetic_campus_reports.csv`: 46 synthetic reports, including six malformed source rows repaired in a generated copy.
* `data/raw/campus/labelled_campus_pairs.csv`: 32 designed pairs (14 `match`, 8 `plausible`, 10 `non_match`). The CAT classifier maps `plausible` to class 0 as a coursework assumption and reports an exclusion sensitivity check. Unlabelled pairs remain unknown.
* Delhi Metro: 13,713 real-world *found-item* records for cleaning and EDA, plus the clearly labelled constructed-pair exercise in the main notebook. The raw CSV is excluded from new commits because descriptions may contain personal details. Obtain your own copy from the source and place it at `data/raw/delhi/delhimetrorail.csv`; see `docs/DATASET.md`.
* Future images: no downloaded Roboflow images, own same-item photographs, image encoder, or measured CLIP result. See `docs/IMAGE_DATASET_GUIDE.md`.

Raw campus inputs are kept unchanged. Keep the Delhi CSV and row-level derivatives local. Delhi generated data goes under `data/processed/`; its model outputs go under `results/delhi_experiment/`. The older campus results remain under `results/ml/`. Dataset provenance and limits are in `docs/DATASET.md`.

## Run CAT 2

From the repository root, with Python 3.11+:

```powershell
python -m pip install -r requirements.txt
python -m scripts.create_delhi_experiment
python -m notebook LogisticRegression_Base.ipynb

# Optional: regenerate the older synthetic campus baseline
python -m scripts.run_cat2
```

Before running the current notebook, download the Delhi Metro CSV as described in `docs/DATASET.md`, save it at `data/raw/delhi/delhimetrorail.csv`, and verify its SHA-256 hash. Run the notebook from first cell to last. The Delhi script generates cleaned rows, fictional claims, constructed labels and grouped splits. The notebook saves four aggregate Delhi charts under `results/figures/`; row-level outputs remain local. `python -m scripts.run_cat2` still regenerates the older campus baseline. A fresh clone needs the separately obtained Delhi CSV for a full notebook rerun.

To check the original rule-based baseline and available tests:

```powershell
python run_evaluation.py
python -m unittest discover -s tests -p "test_*.py"
python -m pytest -q
uvicorn matching_system.api:app --reload
```

`pytest` is needed for the three function-style tests in `tests/test_matching.py`. The FastAPI endpoints use a static synthetic inventory; `POST /reports` does not save reports. Never expose this prototype publicly with sensitive reports. The `android/` folder is an app scaffold with no sign-in, reporting flow or API integration.

## Current status and limitations

**Implemented:** raw-data preparation, pair features, offline Logistic Regression training and grouped validation, synthetic test evaluation, rule-based matcher and prototype API.

**Partially implemented:** Delhi pair labels are constructed, not independently verified; the four Delhi EDA figures depend on the separately obtained CSV for reproduction.

**Planned:** real-campus evaluation, image pairs and CLIP features, model comparison, durable backend and Android integration.

The current Delhi-derived held-out check has 108 constructed pairs. Precision is 0.971, recall 0.944 and F1 0.958 in that academic exercise; these are **not** real-world lost-and-found accuracy estimates. The older campus baseline has eight held-out synthetic pairs. See `docs/CAT2_WORKFLOW.md`, `docs/MODEL_EXPLANATION.md`, and `docs/NEXT_STEPS.md` for the presentation guide and next work.
