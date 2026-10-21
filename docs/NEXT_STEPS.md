# Next steps

## Before CAT 2

1. Install `requirements.txt`; run `python -m scripts.run_cat2`, `python run_evaluation.py` and `python -m pytest -q`.
2. Open `LogisticRegression_Base.ipynb` from the repository root and run every cell; verify that four EDA figures render after Matplotlib is installed and observations match their counts.
3. Independently review the original pair labels, especially `plausible`, and document any change separately. Do not silently edit raw files.
4. Each student should explain raw/clean data, features, X/y, training, grouped cross-validation, confusion matrix, precision, recall, F1 and a false negative.
5. Check the course's shared spreadsheet entry and presentation schedule. Commit the final notebook before the course deadline; review any public data for personal details.

## After CAT 2

1. Download and inspect licensed Roboflow images only if object detection serves a defined feature.
2. Collect consented same-item campus photographs with `instance_id`, pair labels and reviewer records.
3. Test frozen pretrained CLIP image/image and text/image similarities on held-out physical items.
4. Compare text-only and text-plus-image Logistic Regression on the same labelled pairs.
5. Compare Random Forest and Support Vector Machine on the same features, groups and metrics; report measured results only.
6. Build a durable, permission-controlled backend and integrate the tested matching flow with the Kotlin app. Preserve staff ownership verification.
