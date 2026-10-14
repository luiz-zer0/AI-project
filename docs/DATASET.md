# Dataset provenance and use

Accessed source pages on 14 October 2026. The repository's CSV acquisition dates and original survey export location are unknown. Raw root CSV files remain unchanged; generated files live under `data/processed/`.

## University requirements survey

- Source/creator: university project team; original file is not in this repository. The existing Chapter 3 describes an 11-response student extract dated 17–21 September 2026.
- Purpose: requirements, reporting behaviour, AI acceptance and verification expectations; **never** matcher training or performance ground truth.
- Licence/approval, exact questions, missing values and response distribution: not independently verifiable from this repository. Confirm against the original export and university approval.
- Coverage: one university, student respondents only; convenience sample. Language and exact institution are not established here.
- Processing/split: no survey processing is implemented in this repository.

## Delhi Metro Lost and Found

- Publisher: [Abhishek Tiwari (`forgetabhi`) on Kaggle](https://www.kaggle.com/datasets/forgetabhi/delhi-metro-lost-and-found-dataset); page accessed 14 October 2026. Kaggle identifies Delhi Metro Rail Corporation as the underlying data source and [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
- Raw file: `delhimetrorail (1).csv`, SHA-256 `38a91688e2ff5acaf1261e8893d006f254cdfd9597d48bc8564a9573f1bf475a`.
- Raw size: 13,713 rows, six fields: `item_name`, `description`, `item_quantity`, `station_name`, `receiving_date`, `receiving_time`. Dates parse from 15 December 2021 through 21 March 2024. There are 229 station names and 2,977 distinct raw item-name strings.
- Missing: 8,208 descriptions and 10,511 quantities; no missing values in the other four fields. Exact duplicate rows: zero. Language varies and is not fully assessed.
- Purpose: real-world found-item text reference and robustness testing. No photographs, paired lost reports or verified matching labels. It cannot support matching accuracy claims by itself.
- Processing: `python scripts/prepare_delhi_data.py` validates the six-column schema; retains all 13,713 rows and original field values except collapsed whitespace; adds casefolded text and parsed ISO date/time columns. It removes no duplicates or incomplete records. Audit counts and source hash are in `data/processed/delhi_preprocessing_report.json`. Processed output is `data/processed/delhi_metro.csv`.
- Limitation: metro context differs from campus; descriptions can include personal details and must be screened before API use or public redistribution. No train/development/test split is assigned.

## Roboflow Lost and Found image dataset

- [Roboflow Universe project](https://universe.roboflow.com/rnomo/lost-and-found-nlb4x-e6ayk), creator `rnomo`; version [2](https://universe.roboflow.com/rnomo/lost-and-found-nlb4x-e6ayk/dataset/2), generated 13 June 2025; source page accessed 14 October 2026. Project states [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), requiring attribution.
- Version 2 page states 4,546 object-detection images: 3,501 train, zero validation and 1,045 test. It states no source preprocessing or augmentations. Overview lists Bottle, Umbrella, Calculator, Charger, Key and a `None` class; the meaning of `None` requires verification from downloaded annotations.
- Images and annotations are **not present in this repository**. The page totals and licence are source-page claims, not a local file audit. Image dimensions, corruption, class counts, annotation encoding and original acquisition date remain unverified. Do not connect these images to Delhi Metro records.
- `scripts/prepare_image_data.py` is a prepared YOLO-export inventory command. Once the versioned export is downloaded to `data/raw/roboflow/`, install Pillow and run it to create `data/metadata/image_metadata.csv`. No metadata CSV or image-derived result is claimed before that execution.
- Limited object classes and object detection do not establish same-item identity. No image similarity experiment is completed.

## Synthetic campus reports

- Source: 46 repository-authored synthetic examples, 14 lost and 32 found. Creator method and any generative AI tool/model are not documented in the original repository; human checking history is unknown. No real campus incident is implied. Licence is not specified.
- Fields: IDs, report type, description, category, brand, model, colour, material, distinctive features, location, timestamp, status and image reference. Examples span backpacks, laptops, phones, bottles, wallets, umbrellas, earbuds, notebooks, keys, clothing, calculators, jewellery, chargers and books. All image references are blank.
- Raw `synthetic_campus_reports.csv` contains six rows shifted by an extra empty CSV field. `python scripts/prepare_campus_data.py` produces `data/processed/synthetic_campus_reports.csv`, correcting `lost-006`, `found-015`, `found-016`, `lost-010`, `found-023`, `found-024` without deleting rows. The raw file is preserved. No other synthetic examples were added.
- Purpose: controlled prototype and evaluation. Small, designed examples cannot establish real campus accuracy or natural writing distribution.

## Labelled campus pairs

- Source: repository-authored synthetic ground truth, 32 pairs: 14 `match`, 8 `plausible`, 10 `non_match`. Original creator/reviewer and licence are unknown. No labels were changed.
- Fields: lost/found IDs, label, `match_type`, and rationale notes. See [LABELLING_GUIDE.md](LABELLING_GUIDE.md). All 14 lost reports have one intended match, but most possible lost-found combinations have no label.
- `scripts/split_campus_data.py` uses seed 42 and groups a lost report with its labelled found candidates. The manifest has 10 development lost reports/24 pairs and 4 test lost reports/8 pairs; the sets of found IDs do not overlap. This is a split for repeatable prototype evaluation, not model training.
- The matching weights existed before the split and may have been informed by the synthetic examples. Therefore, the current held-out numbers are a reproducible partition, **not evidence of a prospectively untouched test**. Freeze future tuning to development cases and collect new independent test cases.
