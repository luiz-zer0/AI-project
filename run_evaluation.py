from matching_system.data_loader import load_labelled_pairs, load_reports
from matching_system.evaluation import evaluate


def main() -> None:
    reports = load_reports("synthetic_campus_reports.csv")
    labels = load_labelled_pairs("labelled_campus_pairs.csv")
    metrics = evaluate(reports, labels, k=3)
    print("Evaluation metrics")
    print(f"Precision@3: {metrics['precision_at_k']}")
    print(f"Recall@3: {metrics['recall_at_k']}")
    print(f"Mean reciprocal rank: {metrics['mean_reciprocal_rank']}")
    print(f"False positives in top 3: {len(metrics['false_positives'])}")
    for item in metrics["false_positives"][:10]:
        print(item)


if __name__ == "__main__":
    main()

