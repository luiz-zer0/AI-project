# Pair classification model

**AI Application: Classification. Algorithm/Approach: Logistic Regression.**

```text
Lost report + found report
            |
    normalize and compare
            |
 numeric feature vector X
            |
  Logistic Regression
            |
 match score in [0, 1]
            |
 class 0 or 1 at threshold 0.5
```

The features include normalized description overlap, exact attribute matches or conflicts, distinctive-feature overlap, location wording overlap, and capped time distance. Missing attributes create neither a match nor a conflict. `matching_system/feature_builder.py` defines the calculations; `data/processed/modelling_pairs.csv` lets a student inspect every input row.

The current notebook uses real Delhi **found-item records** and synthetic lost claims. Its 120 positives are linked to their source found rows by construction; its 240 negatives assume that other source rows are different physical items. StandardScaler and Logistic Regression are fitted together inside each development fold. The grouped split separates synthetic lost claim IDs and their three candidate found rows; each found row is used once. The held-out partition has 108 constructed pairs, so even strong scores cannot be presented as real lost-and-found accuracy. Its local coefficients are in `results/delhi_experiment/coefficients.csv`.

The older campus baseline uses 32 designed pairs. There, `match` maps to 1 and `plausible` and `non_match` map to 0; a separate analysis excludes `plausible`. Its eight-pair test and `results/ml/coefficients.csv` remain available for comparison. Neither experiment contains verified real handovers.

In a future application, the same model's scores could sort several found reports. The API and Android starter do not run it yet. The current `matching_system/matcher.py` is the separately evaluated **Rule-Based Baseline**. Candidate ranking and ownership verification are different tasks: staff must verify a claimant before releasing an item.

## Future image extension

```text
Text features + metadata features + measured image similarity
                          |
               retrained classifier
                          |
             score and candidate order
```

Images require labelled photographs of the same physical items and comparable different items. A frozen CLIP encoder could supply image/image or text/image similarity values. Only then should we compare text-only against text-plus-image results. Roboflow object-detection categories alone cannot establish item identity. No image embeddings or CLIP scores are measured in this repository.
