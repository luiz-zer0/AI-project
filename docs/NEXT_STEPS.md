# Next steps

## Before CAT 2

1. On each presenter's machine, install `requirements.txt`, obtain the local Delhi CSV as described in `docs/DATASET.md`, and run `python -m scripts.create_delhi_experiment` followed by all cells in `LogisticRegression_Base.ipynb`. The older campus check is `python -m scripts.run_cat2`.
2. Re-run the current notebook from the repository root on the presentation machine. Check all ten code cells, the four Delhi figures, and the data counts against the saved outputs.
3. Explain that the Delhi lost claims and pair labels were constructed. Independently review the older campus labels, especially `plausible`, if using that baseline. Do not silently edit raw files.
4. Each student should explain raw/clean data, features, X/y, training, grouped cross-validation, confusion matrix, precision, recall, F1 and a false negative.
5. Check the course's shared spreadsheet entry and presentation schedule. Commit the final notebook before the course deadline; review any public data for personal details.

## After CAT 2

1. Download and inspect licensed Roboflow images only if object detection serves a defined feature.
2. Collect consented same-item campus photographs with `instance_id`, pair labels and reviewer records.
3. Test frozen pretrained CLIP image/image and text/image similarities on held-out physical items.
4. Compare text-only and text-plus-image Logistic Regression on the same labelled pairs.
5. Compare Random Forest and Support Vector Machine on the same features, groups and metrics; report measured results only.
6. Build a durable, permission-controlled backend and integrate the tested matching flow with the Kotlin app. Preserve staff ownership verification.
