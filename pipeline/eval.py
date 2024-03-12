from pipeline.data_reader import (
    read_correct_wikidata_ids,
    read_dataset_file,
    read_predicted_wikidata_ids,
)
from pipeline.eL_result_to_excel import compare_llm_predictions
from pipeline.llm_comparison_by_class import compare_llm_by_class


def calculate_evaluation_metrics(
    correct_ids: list[list[str]] | list[str], predicted_ids: list[list[str]], dataset: str
) -> tuple[float, float, float]:
    """Calculate evaluation metrics (precision, recall, F-measure)

    Args:
        correct_ids (list[list[str]] | list[str]): List of correct Wikidata IDs for each EL target sentence
        predicted_ids (list[list[str]]): List of predicted Wikidata IDs
                                            for each EL target sentence generated by Llama 2
        dataset (str): Name of the dataset to be evaluated

    Returns:
        tuple[float, float, float]: A tuple containing average precision, average recall, and average F-measure
    """
    metrics: dict[str, list[float]] = {"precision": [], "recall": [], "f1": []}

    for true_ids, predicted_ids_for_line in zip(correct_ids, predicted_ids):
        if dataset == "simpleqs":
            true_ids = [true_ids]  # type: ignore

        true_positive = len(set(predicted_ids_for_line) & set(true_ids))
        false_positive = len(set(predicted_ids_for_line) - set(true_ids))

        """
        When the correct ID of the dataset is null, consider not outputting anything as correct (possible with WebQSP)
        """
        if not true_ids and not predicted_ids_for_line:
            true_positive = 1
            false_positive = 0

        precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
        recall = true_positive / len(true_ids) if len(true_ids) > 0 else 0  # Number of correct IDs=TP+FN
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

        metrics["precision"].append(precision)
        metrics["recall"].append(recall)
        metrics["f1"].append(f1)

    total_lines = len(correct_ids)
    average_metrics = {key: sum(values) / total_lines for key, values in metrics.items() if total_lines > 0}

    return average_metrics.get("precision", 0), average_metrics.get("recall", 0), average_metrics.get("f1", 0)


def evaluate_model_prediction(model: str, dataset: str, language: str) -> None:
    file_extension = ".txt" if dataset == "simpleqs" else ".json"
    correct_wikidata_file_path = f"datasets/test_datasets/{dataset}_test{file_extension}"
    predicted_wikidata_file_path = f"result/{dataset}/{model}/wikidata_id.json"

    correct_wikidata_ids = read_correct_wikidata_ids(correct_wikidata_file_path, dataset)
    predicted_wikidata_ids = read_predicted_wikidata_ids(predicted_wikidata_file_path)
    data = read_dataset_file(correct_wikidata_file_path)

    precision, recall, f1 = calculate_evaluation_metrics(correct_wikidata_ids, predicted_wikidata_ids, dataset)

    print_results(precision, recall, f1)
    if dataset == "webqsp" and language == "english":
        compare_llm_by_class(correct_wikidata_ids, predicted_wikidata_ids, dataset, data)
    if dataset in ["lcquad2", "webqsp"] and language == "english":
        response = input("Would you like to output excel file? (yes/no): ").strip().lower()
        if response == "yes":
            compare_llm_predictions(
                correct_wikidata_ids, predicted_wikidata_ids, model, dataset, correct_wikidata_file_path, language
            )


def print_results(precision: float, recall: float, f1: float) -> None:
    print("\nResult:")
    print(f"Precision: {precision:.3f}")
    print(f"Recall: {recall:.3f}")
    print(f"F-measure: {f1:.3f}")
