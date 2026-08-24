# Tokenomics

Practical unit economics for enterprise AI.

This repo models the cost mechanics that decide whether an AI system creates value after the demo: inference spend, context inflation, retry tax, human-review cost, platform cost, model-routing tradeoffs, and payback.

## Core questions

- What does one successful AI task actually cost?
- How much does retry behavior inflate that cost?
- When does human review erase expected savings?
- When should a request route to a cheaper model?
- How much context is useful before it becomes waste?
- What success rate is required to break even?

## Current model

The first implementation calculates:

- current-state annual labor cost
- realized automation benefit
- retry tax
- annual AI operating cost
- net annual value
- implementation payback

## Why `Tokenomics`

Token cost alone is a weak metric. Enterprise AI economics emerge from the interaction between tokens, retries, latency, human intervention, platform overhead, and task success. The unit of analysis should increasingly become **cost per successful business outcome**.

## Run

```bash
python economics.py
```

## Roadmap

- cost per successful task
- context inflation simulator
- model-routing break-even analysis
- caching economics
- batch vs realtime economics
- sensitivity analysis
- agent retry distributions
- dashboard
