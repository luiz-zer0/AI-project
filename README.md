# AI-assisted campus lost and found matching prototype

The current system ranks possible found-item reports from a lost-item report, explains shared and conflicting details, and requires human ownership verification. It is a prototype; optional cosine similarity can contribute a small image score when precomputed embeddings for both reports are supplied, but no image encoder or image evaluation has been run. Persistent reporting, notifications and an Android application are not implemented.

## Data and reproducibility

See [dataset provenance](docs/DATASET.md) and [labelling rules](docs/LABELLING_GUIDE.md). Root CSVs are the unchanged sources. Generated outputs go to `data/processed/`, `data/metadata/` or `results/`.

Install Python 3.11+ and then:

```powershell
python -m pip install -r requirements.txt
python scripts/prepare_campus_data.py
python scripts/prepare_delhi_data.py
python scripts/split_campus_data.py
python run_evaluation.py
python -m pytest -q
uvicorn matching_system.api:app --reload
```

`run_evaluation.py` also prepares the corrected campus copy and split manifest. It writes `results/baseline_results.json`. The FastAPI prototype serves `/health`, `/reports`, `/matches`, and a non-persisting `/reports` POST. It does not authenticate users or prove ownership; do not expose it publicly with sensitive reports.

Roboflow version 2 must be downloaded separately with attribution. After obtaining its YOLO export, install Pillow and run:

```powershell
python scripts/prepare_image_data.py data/raw/roboflow --output data/metadata/image_metadata.csv
```

The image script inventories and validates files while preserving Roboflow's split. `matching_system/image_matching.py` can compare supplied vectors, and the ranker caps their supporting bonus at 10 points and suppresses it when structured fields conflict. A pretrained CLIP encoder, generated embeddings and hybrid image evaluation remain pending because no images or confirmed same-item image pairs are in this repository. The Delhi Metro file contains no images or verified lost-found pairs and is not used to calculate matching accuracy.

The labelled campus set is small and partly incomplete: unlabelled combinations are unknown, not confirmed false positives. Baseline numbers are synthetic-prototype checks, not production accuracy. See `STAGES_B_TO_G.md` for earlier implementation notes and `results/baseline_results.json` for current measured output.
