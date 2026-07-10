<div align=center>
  <h1>📊 GEO Benchmarks</h1>
  <p><em>Weekly dataset: which brands get cited for which queries across ChatGPT, Claude, Perplexity, Gemini.</em></p>
  <p><a href=LICENSE><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt=License></a>
  <a href=https://github.com/josezuma/geo-benchmarks/actions/workflows/ci.yml><img src="https://img.shields.io/badge/CI-passing-green.svg"></a></p>
  <p>by <a href=https://brandvirality.com>BrandVirality</a> — <strong>SaaS for AI visibility.</strong><br>
  <strong>Author:</strong> <a href=https://github.com/josezuma>Jose Zuma</a></p>
</div>

---

## Quick Start

```bash
python3 scripts/runner.py --queries prompts/standard.json --models chatgpt,claude,perplexity,gemini
```

## Dataset Format

Each benchmark run produces a JSON file with format:

```json
{
  "benchmark_date": "2026-07-10",
  "model": "chatgpt",
  "queries": [
    {
      "query": "What is the best CRM for small business?",
      "brands_cited": [
        {"name": "HubSpot", "rank": 1, "snippet": "HubSpot is widely considered the best...", "sentiment": "positive"},
        {"name": "Salesforce", "rank": 2, "snippet": "Salesforce is a strong option for...", "sentiment": "neutral"}
      ]
    }
  ]
}
```

## Related
awesome-ai-visibility, geo-prompts, geo-watch, ai-search-share-of-voice, llm-citation-scanner
