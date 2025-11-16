
## This code is inspired from https://github.com/microsoft/genai-evals/blob/main/src/ai_evaluate_action/summarize.py

import json
from pathlib import Path
from statistics import mean
from typing import Any, TypeAlias, TypedDict

from jinja2 import Environment, FileSystemLoader
from pydantic import BaseModel
from archive_results import save_to_archive

class Results(BaseModel):
    rows: list[dict[str, Any]]
    metrics: dict[str, float]
    studio_url: str | None = None


EvaluatorName: TypeAlias = str
Category: TypeAlias = str
ValueName: TypeAlias = str


class ParsedRow(TypedDict):
    inputs: dict[str, Any]
    outputs: dict[EvaluatorName, dict[ValueName, Any]]


class ParsedResults(Results):
    rows: list[ParsedRow]


def template_parameters(parsed_results: ParsedResults) -> dict[str, Any]:
    
    class ExtraRow(ParsedRow):
        eval_scores: dict[str, float | int]

    tests: dict[tuple[str, str], list[ExtraRow]] = {}
    
    for row in parsed_results.rows:
        

        eval_scores = {
            evaluator_name: next(score for score in outputs.values() if isinstance(score, (float, int)))
            for evaluator_name, outputs in row["outputs"].items()
        }

        tests.setdefault(
            (row["inputs"]["query"], row["inputs"]["ground_truth"]),
            [],
        ).append(ExtraRow(**row, eval_scores=eval_scores))

    aggregated_eval_scores: dict[str, list[int | float]] = {}

    for rows in tests.values():
        for row in rows:
            for evaluator_name in row["outputs"]:
                aggregated_eval_scores.setdefault(evaluator_name, []).append(row["eval_scores"][evaluator_name]
                )

    template_params = {
        "tests": tests,
        "average_eval_scores": {
            evaluator_name: mean(v) for evaluator_name, v in aggregated_eval_scores.items()
        },
        "evaluator_names": list(parsed_results.rows[0]["outputs"].keys()),
    }
    
    # Create a JSON-serializable version for archiving
    serializable_params = {
        "tests": {
            f"{query} | {ground_truth}": [dict(row) for row in rows]
            for (query, ground_truth), rows in tests.items()
        },
        "average_eval_scores": template_params["average_eval_scores"],
        "evaluator_names": template_params["evaluator_names"],
    }
    
    save_to_archive(serializable_params, "template_parameters")
    
    return template_params


def summarize_results(results: dict, summary_path: Path, *, show_raw_output: bool = True) -> None:
    def parse_row(row: dict[str, Any]) -> ParsedRow:
        inputs = {k.removeprefix("inputs."): (v) for k, v in row.items() if k.startswith("inputs.")}
        outputs: dict[EvaluatorName, dict[ValueName, Any]] = {}

        for k, v in {k: v for k, v in row.items() if k.startswith("outputs.")}.items():
            _, evaluator_name, value_name = k.split(".")

            evaluator_dict = outputs.setdefault(evaluator_name, {})
            evaluator_dict[value_name] = v
        return {"inputs": inputs, "outputs": outputs}

    results_model = Results.model_validate(results)

    parsed_results = ParsedResults(
        rows=list(map(parse_row, results_model.rows)),
        metrics=results_model.metrics,
        studio_url=results_model.studio_url,
    )

    env = Environment(loader=FileSystemLoader(Path(__file__).parent.resolve()))
    template = env.get_template("summarize.md.jinja")

    summary_path.write_text(
        template.render(**template_parameters(parsed_results), show_raw_output=show_raw_output), encoding="utf-8"
    )


if __name__ == "__main__":
    import json

    with Path(__file__, "..", "results.jsonl").resolve().open() as f:
        results = json.load(f)

    summarize_results(results, Path(__file__, "..", "summary.md").resolve())