# Updated Stock Picker V5.2 (Enhanced with Additional Agents and Tasks)

A CrewAI-based, multi-agent stock research workflow that screens technology equities, reviews fundamentals, valuation, technical signals, institutional activity, catalysts, and risk, then produces an evidence-audited **Top 50 ranking** and **Top 5 shortlist**.

## Setup (Windows CMD)

Requires Python 3.10–3.13, [uv](https://docs.astral.sh/uv/), and API credentials for the configured LLM and search tools.

```bat
cd path\to\stock_picker
copy .env.example .env
notepad .env
set SSL_CERT_FILE=
set SSL_CERT_DIR=
set UV_SYSTEM_CERTS=true
uv sync --system-certs
```

Add your API keys to `.env` before running. Never commit this file.

## Run

```bat
uv run --no-sync stock_picker
```

The default input sector is **Technology**; change it in `src/stock_picker/main.py`.

## Project files

- `src/stock_picker/crew.py` — agents, tools, execution limits, and sequential workflow.
- `src/stock_picker/config/agents.yaml` — agent roles and instructions.
- `src/stock_picker/config/tasks.yaml` — task definitions and expected outputs.
- `src/stock_picker/main.py` — entry point and inputs.
- `knowledge/` — investment research criteria and preferences.



## Executive conclusion (Recommended Results)

The only defensible candidates are the **five names with nonzero conditional evidence scores** in the supplied audited table:

1. **NVDA**
2. **GOOGL**
3. **MSFT**
4. **AAPL**
5. **AMZN**


## Limitations

This CrewAI project is intended for educational and practical learning purposes only. Its stock analyses and recommendations are not guaranteed to be accurate or reliable and should not be considered financial advice.

Research agents have bounded iterations and execution times; audit, ranking, and final-review agents do not use web search. Findings should identify sources, dates, uncertainty, and missing evidence. Rankings are **LLM-generated, not deterministic or backtested**. Agent limits do not impose a global Serper search cap. Validate all financial data before making investment decisions.

## Acknowledge

I would like to thank Ed Donner for providing the reference implementation in his Udemy course.




