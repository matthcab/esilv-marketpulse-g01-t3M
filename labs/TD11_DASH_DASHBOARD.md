# TD11 - Dash Dashboard

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"Traders want a visual interface instead of terminal output."
```

## Context

TD10 completed the provider stage.

Before TD11, MarketPulse also froze one shared application result:

```text
docs/12_MARKETPULSE_APPLICATION_SNAPSHOT_CONTRACT.md
```

The dashboard must consume:

```python
build_market_snapshot(...)
```

rather than calling providers or recomputing analytics.

The target flow is:

```text
providers
   |
   v
canonical rows
   |
   v
analytics.py
   |
   v
build_market_snapshot()
   |
   +----------------+
   |                |
   v                v
terminal          Dash
```

TD11 adds only the presentation layer.

The central visual remains:

```text
Instrument vs Benchmark
Base 100
```

## Learning objectives

At the end of TD11, you should be able to:

- install and record Dash dependencies;
- create one simple `src/dashboard.py`;
- consume the shared MarketPulse snapshot;
- display provider and comparison context;
- display instrument return;
- display benchmark return;
- display relative performance;
- plot both base-100 series;
- explain why the dashboard does not own provider logic;
- explain why the dashboard does not own analytical formulas;
- run the dashboard with the frozen CORE command;
- complete the established Git workflow.

## CORE definition of done

TD11 is complete when the team can confirm:

```text
[ ] dash is recorded in requirements.txt
[ ] plotly is recorded in requirements.txt
[ ] src/dashboard.py exists
[ ] dashboard.py imports build_market_snapshot
[ ] dashboard.py does not call Yahoo directly
[ ] dashboard.py does not call Bloomberg directly
[ ] dashboard.py does not calculate period return
[ ] dashboard.py does not calculate base 100
[ ] dashboard.py does not calculate relative performance
[ ] provider is visible
[ ] instrument is visible
[ ] benchmark is visible
[ ] lookback is visible
[ ] interval is visible
[ ] instrument return is visible
[ ] benchmark return is visible
[ ] relative performance is visible
[ ] one base-100 chart contains both series
[ ] terminal and dashboard values are consistent for the same snapshot
[ ] python src/main.py works
[ ] python src/dashboard.py works
[ ] the change follows the standard branch / PR / review workflow
```

Callbacks are not required.

Selectors are not required.

Daily-return and volume charts are not required.

Advanced styling is not required.

## Prerequisites

Before starting:

```text
[ ] TD01-TD10 completed
[ ] team main is synchronized
[ ] python src/main.py works
[ ] build_market_snapshot(...) exists
[ ] snapshot contract matches docs/12_MARKETPULSE_APPLICATION_SNAPSHOT_CONTRACT.md
[ ] snapshot returns instrument and benchmark context
[ ] snapshot returns period returns
[ ] snapshot returns relative performance
[ ] snapshot returns two base-100 series
[ ] provider mode is labelled honestly
[ ] no credentials are exposed
```

Update local main:

```bash
git switch main
git pull
git status
python src/main.py
```

Start from a clean working tree.

## Session plan

The CORE is designed for approximately 80 minutes.

The final 10 minutes are reserved for browser startup, debugging, review and optional polish.

| Time | Activity |
|---|---|
| 00-08 min | Dashboard boundary + snapshot contract |
| 08-18 min | Install and record Dash dependencies |
| 18-30 min | Create minimal dashboard entry point |
| 30-45 min | Consume snapshot + display context |
| 45-58 min | Add three performance indicators |
| 58-70 min | Build one base-100 comparison chart |
| 70-78 min | Run terminal + dashboard and compare |
| 78-80 min | CORE validation |
| 80-90 min | Review / troubleshooting / OPTIONAL |

## Repository evolution

TD11 adds one file:

```text
src/
├── main.py
├── analytics.py
├── dashboard.py
└── providers/
    ├── __init__.py
    ├── yahoo_provider.py
    └── bloomberg_provider.py
```

Responsibilities remain:

```text
providers/
=
acquisition + normalization

analytics.py
=
alignment + calculations

main.py
=
build_market_snapshot(...)
+
terminal presentation

dashboard.py
=
Dash presentation only
```

# CORE

# Part 1 - Understand the dashboard boundary

The dashboard is a consumer of application data.

It is not another MarketPulse engine.

Required separation:

```text
provider-specific input
        |
        v
canonical rows
        |
        v
analytics
        |
        v
snapshot
        |
        v
Dash presentation
```

Avoid:

```text
dashboard.py
   |
   +-> fetch_yahoo_prices()
   +-> fetch_bloomberg_prices()
   +-> calculate return again
   +-> calculate base 100 again
```

The snapshot contract exists specifically to prevent that duplication.

# Part 2 - Create the TD11 feature branch

Use the established workflow:

```bash
git switch main
git pull
git status
git switch -c feature/dash-dashboard
```

TD11 does not reteach Git theory.

# Part 3 - Install and record direct dependencies

Check:

```bash
python -m pip show dash
python -m pip show plotly
```

If needed:

```bash
python -m pip install dash plotly
```

Add direct dependencies to:

```text
requirements.txt
```

Required entries:

```text
dash
plotly
```

Keep previously required dependencies such as:

```text
yfinance
```

if the project still uses them.

Do not manually list every transitive dependency.

# Part 4 - Create src/dashboard.py

Create:

```text
src/dashboard.py
```

Start with:

```python
from dash import Dash, dcc, html
import plotly.graph_objects as go

from main import build_market_snapshot
```

Then create the application:

```python
app = Dash(__name__)
```

The CORE uses one file.

Do not create:

```text
src/dashboard/
src/dashboard/app.py
src/dashboard/layout.py
src/dashboard/callbacks.py
```

for the required lab.

# Part 5 - Build the snapshot once

Use:

```python
snapshot = build_market_snapshot()
```

Read the fields defined by:

```text
docs/12_MARKETPULSE_APPLICATION_SNAPSHOT_CONTRACT.md
```

For example:

```python
provider = snapshot["provider"]
lookback = snapshot["lookback"]
interval = snapshot["interval"]

instrument = snapshot["instrument"]
benchmark = snapshot["benchmark"]

instrument_return = snapshot["instrument_return"]
benchmark_return = snapshot["benchmark_return"]
relative_performance = snapshot["relative_performance"]

instrument_base_100 = snapshot["instrument_base_100"]
benchmark_base_100 = snapshot["benchmark_base_100"]
```

Do not add formulas here.

The dashboard may format values for display.

# Part 6 - Create the minimal application first

Before building the complete page, verify that Dash starts.

Example:

```python
app.layout = html.Div(
    [
        html.H1("MarketPulse"),
        html.P(
            "Instrument vs Benchmark market comparison"
        ),
    ]
)


if __name__ == "__main__":
    app.run(debug=False)
```

Run:

```bash
python src/dashboard.py
```

Open the local URL displayed by Dash.

Confirm that the page loads before adding more components.

# Part 7 - Display comparison context

The dashboard must display:

```text
Provider
Instrument
Benchmark
Lookback
Interval
```

Use snapshot values rather than hard-coded provider state.

Example:

```python
context = html.Div(
    [
        html.P(f"Provider: {provider}"),
        html.P(
            f"Instrument: "
            f"{instrument['ticker']} - {instrument['name']}"
        ),
        html.P(
            f"Benchmark: "
            f"{benchmark['ticker']} - {benchmark['name']}"
        ),
        html.P(f"Lookback: {lookback}"),
        html.P(f"Interval: {interval}"),
    ]
)
```

If the provider label says:

```text
Bloomberg stage - APPROVED_SAMPLE
```

keep that wording visible.

Do not shorten it to LIVE Bloomberg.

# Part 8 - Display three performance indicators

Required values:

```text
Instrument return
Benchmark return
Relative performance
```

Formatting can happen in the presentation layer.

Example:

```python
performance = html.Div(
    [
        html.Div(
            [
                html.H3("Instrument Return"),
                html.P(
                    f"{instrument_return:+.2f}%"
                ),
            ]
        ),
        html.Div(
            [
                html.H3("Benchmark Return"),
                html.P(
                    f"{benchmark_return:+.2f}%"
                ),
            ]
        ),
        html.Div(
            [
                html.H3("Relative Performance"),
                html.P(
                    f"{relative_performance:+.2f} pts"
                ),
            ]
        ),
    ]
)
```

The formatting is local.

The analytical values come from the snapshot.

# Part 9 - Build one base-100 figure

The central chart uses:

```text
instrument_base_100
benchmark_base_100
```

Create:

```python
figure = go.Figure()
```

Add the instrument:

```python
figure.add_trace(
    go.Scatter(
        x=[
            row["date"]
            for row in instrument_base_100
        ],
        y=[
            row["value"]
            for row in instrument_base_100
        ],
        mode="lines",
        name=instrument["ticker"],
    )
)
```

Add the benchmark:

```python
figure.add_trace(
    go.Scatter(
        x=[
            row["date"]
            for row in benchmark_base_100
        ],
        y=[
            row["value"]
            for row in benchmark_base_100
        ],
        mode="lines",
        name=benchmark["ticker"],
    )
)
```

Add simple labels:

```python
figure.update_layout(
    title="Instrument vs Benchmark - Base 100",
    xaxis_title="Date",
    yaxis_title="Base 100",
)
```

Do not calculate base 100 inside this section.

# Part 10 - Assemble the final CORE layout

One simple layout is enough:

```python
app.layout = html.Div(
    [
        html.H1("MarketPulse"),
        context,
        performance,
        dcc.Graph(figure=figure),
    ]
)
```

The required dashboard is static.

No callback is required.

# Part 11 - Run the complete dashboard

Run:

```bash
python src/dashboard.py
```

Verify:

```text
[ ] page loads
[ ] provider is visible
[ ] instrument is visible
[ ] benchmark is visible
[ ] lookback is visible
[ ] interval is visible
[ ] instrument return is visible
[ ] benchmark return is visible
[ ] relative performance is visible
[ ] chart contains instrument series
[ ] chart contains benchmark series
```

Both base-100 series should start at:

```text
100
```

If they do not, inspect the snapshot and analytics.

Do not correct the formula inside the dashboard.

# Part 12 - Compare terminal and dashboard

Run the terminal path:

```bash
python src/main.py
```

Then run the dashboard:

```bash
python src/dashboard.py
```

For the same application snapshot, compare:

```text
provider
instrument
benchmark
lookback
interval
instrument return
benchmark return
relative performance
```

The values should be consistent.

The two presentations may format values differently.

They must not calculate different business results.

# Part 13 - Validate dashboard isolation

Inspect:

```text
src/dashboard.py
```

It must not contain provider-specific calls such as:

```text
fetch_yahoo_prices(...)
fetch_bloomberg_prices(...)
fetch_raw_bloomberg_history(...)
```

It must not contain formulas equivalent to:

```text
last / first - 1
instrument return - benchmark return
close / first close * 100
```

Those responsibilities already belong elsewhere.

# Part 14 - Standard Git handoff

Before committing:

```bash
git status
git diff
```

Typical required changes:

```text
requirements.txt
src/dashboard.py
```

`src/main.py` should change only if the snapshot contract still needs a small correction to match the frozen document.

Do not duplicate or move provider logic into dashboard code.

Run both CORE commands:

```bash
python src/main.py
python src/dashboard.py
```

Suggested commit and PR title:

```text
feat: add MarketPulse Dash dashboard
```

Reviewer checklist:

```text
[ ] dash dependency is recorded
[ ] plotly dependency is recorded
[ ] dashboard consumes build_market_snapshot()
[ ] dashboard has no provider-specific request
[ ] dashboard has no analytical formula
[ ] provider context is visible
[ ] instrument and benchmark are visible
[ ] three performance values are visible
[ ] chart contains both base-100 series
[ ] no credential is exposed
```

Merge after review.

# Checkpoint relation

Checkpoint C is performed after TD12.

TD11 prepares:

```text
02_dash_dashboard.png
```

The canonical evidence contract is:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

Do not duplicate the full evidence rules here.

The future screenshot must demonstrate the functional comparative dashboard, not merely that Dash started.

# OPTIONAL

Complete optional work only after the CORE definition of done is satisfied.

## Optional 1 - Daily-return chart

Only if the team already implemented optional daily returns earlier.

Add a secondary chart.

Do not add daily-return calculations to TD11.

## Optional 2 - Instrument volume chart

Add a chart for primary instrument volume if the selected provider supplies meaningful values.

Benchmark volume is not a CORE requirement.

## Optional 3 - Styling polish

Improve spacing, typography or layout after all required information is correct.

Do not spend CORE time building a design system.

## Optional 4 - Layout helper

If `dashboard.py` becomes difficult to read, extract a small local helper function inside the same file.

Do not introduce a nested dashboard package for the CORE.

# ADVANCED

Interactive Dash work has been reclassified from OPTIONAL to ADVANCED.

The two planned activities are:

```text
ADV-DASH-01 - Callback
ADV-DASH-02 - Instrument Selector
```

Current status:

```text
PENDING_EXTERNAL
```

They are not active student exercises yet.

Activation requires a real Dash runtime validation and, for the selector, an application layer that genuinely supports parameterized instruments.

The TD11 CORE remains a static dashboard and is sufficient for Checkpoint C preparation.

# TROUBLESHOOTING

## ModuleNotFoundError: dash

Run:

```bash
python -m pip install -r requirements.txt
```

Verify:

```bash
python -m pip show dash
```

## ModuleNotFoundError: plotly

Verify:

```bash
python -m pip show plotly
```

and confirm `plotly` is in `requirements.txt`.

## Cannot import build_market_snapshot

Run the dashboard from the repository root:

```bash
python src/dashboard.py
```

Verify:

```text
src/main.py
src/dashboard.py
```

and confirm `main.py` keeps:

```python
if __name__ == "__main__":
    main()
```

Do not solve the import problem by copying the snapshot builder into `dashboard.py`.

## Dashboard starts but chart is empty

Inspect the snapshot before changing Plotly code:

```python
print(snapshot["instrument_base_100"])
print(snapshot["benchmark_base_100"])
```

Remove temporary debug output afterward.

## One series does not start at 100

The issue is upstream.

Inspect:

```text
align_series()
calculate_base_100()
snapshot content
```

Do not add a correction factor in the chart.

## Dashboard values differ from terminal values

Confirm both presentations consume the same snapshot contract.

Check for duplicated calculations or direct provider calls inside `dashboard.py`.

## Remote provider is temporarily unavailable

Follow the provider-specific authorized fallback rules established in TD08-TD10.

Do not fabricate dashboard values.

# Final readiness check

Each student should be able to explain:

```text
[ ] Dash's role as presentation
[ ] build_market_snapshot(...) role
[ ] provider vs analytics vs snapshot vs dashboard
[ ] why dashboard.py does not call providers
[ ] why dashboard.py does not calculate returns
[ ] why base 100 is the central comparison chart
[ ] why both series use aligned dates
[ ] why dash and plotly are recorded dependencies
```

The team should confirm:

```text
[ ] src/dashboard.py exists
[ ] python src/main.py works
[ ] python src/dashboard.py works
[ ] dashboard consumes the snapshot
[ ] required context is visible
[ ] three performance values are visible
[ ] two base-100 series are visible
[ ] dashboard change was reviewed
[ ] no credentials are exposed
```

# What comes next?

TD11 completes the visual application path:

```text
providers
   |
   v
analytics
   |
   v
snapshot
   |
   +----------+
   |          |
   v          v
terminal     Dash
```

TD12 introduces no major new feature.

It focuses on:

```text
integration
documentation
clean setup
reproducibility
final review
Checkpoint C
```
