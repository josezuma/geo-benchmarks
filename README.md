<div align="center">
  <h1>📊 GEO Benchmarks</h1>
  <p><em>Weekly brand citation benchmark dataset. Which brands get cited for which queries across ChatGPT, Claude, Perplexity, Gemini. Published as structured JSON.</em></p>
  <p>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
    <a href="https://github.com/josezuma/geo-benchmarks/actions/workflows/benchmark.yml"><img src="https://github.com/josezuma/geo-benchmarks/actions/workflows/benchmark.yml/badge.svg" alt="Weekly Benchmark"></a>
  </p>
  <p>by <a href="https://brandvirality.com">BrandVirality</a> — <strong>SaaS for AI visibility.</strong><br>
  <strong>Author:</strong> <a href="https://github.com/josezuma">Jose Zuma</a></p>
</div>

---

## Quick Start

```bash
# Run a benchmark
python3 scripts/run_benchmark.py --queries data/queries.json --output results/

# View latest results
cat data/weekly/2026-W28.json | jq '.'
```

## What This Is

A weekly automated benchmark that answers: **"Which brands dominate AI search results?"**

Each week, we run a standardized set of 50 prompts across ChatGPT, Claude, Perplexity, and Gemini. For each response we record:
- Which brands were mentioned
- What position they appeared (1st, 2nd, 3rd...)
- Whether the mention was positive, neutral, or negative
- A snippet of the response context

## Dataset Format

```json
{
  "benchmark_week": "2026-W28",
  "run_date": "2026-07-10",
  "models": ["chatgpt", "claude", "perplexity", "gemini"],
  "results": [
    {
      "query_id": "crm-001",
      "query": "What is the best CRM for small businesses in 2026?",
      "responses": {
        "chatgpt": {
          "model": "gpt-4o",
          "brands": [
            {"name": "HubSpot", "rank": 1, "sentiment": "positive", "snippet": "HubSpot is widely considered the best CRM for small businesses due to its...",
            {"name": "Salesforce", "rank": 2, "sentiment": "neutral", "snippet": "Salesforce offers a more enterprise-focused solution but has small business tiers..."}
          ]
        }
      }
    }
  ]
}
```

## Weekly Schedule

Every Monday at 06:00 UTC, a GitHub Action runs the benchmark across all 4 models and commits the results.

## How to Contribute

Add queries to `data/queries.json` following the schema. Each query needs:
- `id`: unique identifier
- `category`: CRM, AI, Fintech, etc.
- `query`: the prompt text
- `target_brands`: brands we're tracking for this query

## Related

- [geo-prompts](https://github.com/josezuma/geo-prompts) — Benchmark prompt sets
- [ai-search-share-of-voice](https://github.com/josezuma/ai-search-share-of-voice) — CLI that queries LLMs
- [llm-citation-scanner](https://github.com/josezuma/llm-citation-scanner) — Deep-dive into responses
- [geo-watch](https://github.com/josezuma/geo-watch) — Schedule regular monitoring
- [mcp-geo](https://github.com/josezuma/mcp-geo) — MCP server for GEO tools
- [+14 more](https://github.com/josezuma?tab=repositories)

## License

[MIT](LICENSE) © 2026 [Jose Zuma](https://github.com/josezuma) / [BrandVirality](https://brandvirality.com)
