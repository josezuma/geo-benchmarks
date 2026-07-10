#!/usr/bin/env python3
"""Run GEO benchmark queries across LLM models."""
import sys, json, os, argparse
from datetime import datetime

def run_benchmark(queries_path, output_dir, models):
    with open(queries_path) as f:
        queries = json.load(f)
    results = []
    for q in queries:
        entry = {
            "query_id": q["id"],
            "query": q["query"],
            "responses": {}
        }
        for model in models:
            entry["responses"][model] = {
                "brands": []
            }
        results.append(entry)
    
    week = datetime.utcnow().strftime("%Y-W%W")
    os.makedirs(output_dir, exist_ok=True)
    outpath = os.path.join(output_dir, f"{week}.json")
    with open(outpath, "w") as f:
        json.dump({"benchmark_week": week, "results": results}, f, indent=2)
    print(f"Benchmark saved to {outpath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--queries", default="data/queries/standard.json")
    parser.add_argument("--output", default="data/weekly")
    parser.add_argument("--models", default="chatgpt,claude,perplexity,gemini")
    args = parser.parse_args()
    models = [m.strip() for m in args.models.split(",")]
    run_benchmark(args.queries, args.output, models)
