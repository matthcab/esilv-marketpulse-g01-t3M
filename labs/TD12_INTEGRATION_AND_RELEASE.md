# TD12 - Integration + Release

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"We need a reproducible version of MarketPulse that another person can run."
```

## Context

TD12 closes the 18-hour guided MarketPulse sequence.

No major feature is introduced here.

The application contracts are already frozen:

```text
Terminal
python src/main.py

Dashboard
python src/dashboard.py

Application result
build_market_snapshot(...)

Evidence contract
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

The release task is therefore:

```text
clean
+
document
+
install
+
run
+
review
+
merge
+
reproduce
+
capture evidence
```

## Learning objectives

At the end of TD12, you should be able to:

- confirm the final authorized provider honestly;
- remove temporary development artefacts;
- verify direct dependencies;
- make README execution instructions accurate;
- validate both frozen runtime commands;
- reproduce MarketPulse from a fresh or clean setup;
- review and merge final integration work;
- prepare Checkpoint C without manufacturing evidence;
- explain your own late-stage contribution.

## CORE definition of done

TD12 is complete when the team can confirm:

```text
[ ] final provider or access mode is documented honestly
[ ] no temporary debug artefact remains
[ ] requirements.txt contains required direct dependencies
[ ] README commands match the repository
[ ] python src/main.py works
[ ] python src/dashboard.py works
[ ] dashboard consumes the shared snapshot
[ ] no secret is committed
[ ] fresh or clean setup succeeds using documented steps
[ ] final integration work received review
[ ] merged team main was run again
[ ] Checkpoint C can be captured from real project state
```

Do not add a large new feature.

Do not redesign the package structure.

Do not add CI/CD, Docker or deployment requirements to the common CORE.

## Prerequisites

Before starting:

```text
[ ] TD01-TD11 completed
[ ] team main is synchronized
[ ] selected authorized provider path works
[ ] build_market_snapshot(...) works
[ ] python src/main.py works
[ ] python src/dashboard.py works
[ ] branch / PR / review workflow is understood
[ ] Checkpoint C canonical contract is known
```

Start with:

```bash
git switch main
git pull
git status
python src/main.py
```

## Session plan

The CORE is designed for approximately 80 minutes.

The final 10 minutes are reserved for Checkpoint C capture and troubleshooting.

| Time | Activity |
|---|---|
| 00-08 min | Confirm final provider + release scope |
| 08-20 min | Repository cleanup + dependency check |
| 20-32 min | README and run instructions |
| 32-52 min | Fresh or clean reproducibility test |
| 52-65 min | Final integration PR |
| 65-75 min | Review + merge |
| 75-80 min | Final run from merged main |
| 80-90 min | Checkpoint C capture / buffer |

# CORE

# Part 1 - Confirm the final provider

Record the provider or access mode actually used.

Examples:

```text
Yahoo Finance via yfinance
Bloomberg - LIVE
Bloomberg stage - APPROVED_SAMPLE
```

Do not write:

```text
Bloomberg - LIVE
```

if the final run actually used:

```text
APPROVED_SAMPLE
```

Accuracy is part of the release contract.

# Part 2 - Create the final integration branch

Use:

```bash
git switch main
git pull
git status
git switch -c feature/final-integration
```

The branch is for:

```text
cleanup
documentation
dependency correction
release-readiness fixes
```

not a new feature line.

# Part 3 - Clean the repository

Inspect:

```bash
git status
git diff
```

Review the project for:

```text
temporary debug output
obsolete exercise files
accidental local paths
unrelated screenshots
credentials
unused dependencies
duplicate temporary code
```

Keep useful application output.

Remove only artefacts that are genuinely temporary.

Do not reorganize the frozen CORE architecture during release cleanup.

Reference:

```text
docs/05_TARGET_REPOSITORY_STRUCTURE.md
```

# Part 4 - Verify direct dependencies

Open:

```text
requirements.txt
```

The final team repository should list direct dependencies actually required by its code.

Typical later-stage dependencies include:

```text
yfinance
dash
plotly
```

A Bloomberg-specific dependency belongs there only if the instructor-approved LIVE implementation really imports it.

Do not add packages merely because they were discussed.

Verify installation:

```bash
python -m pip install -r requirements.txt
```

# Part 5 - Finalize the README

The team README must let another student or evaluator answer:

```text
What is MarketPulse?
What is the instrument?
What is the benchmark?
What provider or mode is used?
How do I install dependencies?
How do I run the terminal path?
How do I run the dashboard?
What environment constraint exists?
Where is the evidence?
```

Use the root instructor README as a presentation reference.

At minimum, retain accurate commands:

```bash
python -m pip install -r requirements.txt
python src/main.py
python src/dashboard.py
```

Do not add badges for CI, security, releases or licenses unless the team repository actually contains and supports those contracts.

Static course or technology badges are acceptable.

# Part 6 - Validate the terminal path

Run:

```bash
python src/main.py
```

Verify:

```text
[ ] provider or mode is honest
[ ] instrument is correct
[ ] benchmark is correct
[ ] lookback is 1 month
[ ] interval is Daily
[ ] instrument return is visible
[ ] benchmark return is visible
[ ] relative performance is visible
[ ] no temporary debug output remains
```

# Part 7 - Validate the dashboard path

Run:

```bash
python src/dashboard.py
```

Verify:

```text
[ ] dashboard loads
[ ] provider is visible
[ ] instrument is visible
[ ] benchmark is visible
[ ] lookback is visible
[ ] interval is visible
[ ] instrument return is visible
[ ] benchmark return is visible
[ ] relative performance is visible
[ ] one base-100 chart contains both series
```

The dashboard should consume the shared snapshot contract.

Do not repair a presentation issue by duplicating provider or analytical logic inside `dashboard.py`.

# Part 8 - Perform a fresh or clean reproducibility test

Use a fresh directory, fresh Codespace or other instructor-approved clean environment.

Do not destroy your current working copy.

A typical sequence is:

```bash
git clone <team-repository-url> marketpulse-repro
cd marketpulse-repro
python -m pip install -r requirements.txt
python src/main.py
python src/dashboard.py
```

If a provider requires a documented classroom environment, use that prerequisite honestly.

Reproducibility means:

```text
repository
+
dependencies
+
documented environment
+
documented commands
=
working application
```

It does not mean that an external proprietary provider must work outside its authorized environment.

# Part 9 - Fix only release blockers

If the clean run fails, fix the actual cause.

Common release blockers:

```text
missing dependency
wrong import
hard-coded local path
missing required file
README command mismatch
undocumented provider prerequisite
temporary debug code
```

Do not use TD12 to redesign the provider architecture.

# Part 10 - Open the final integration PR

Inspect:

```bash
git status
git diff
```

Stage only required release changes.

Suggested commit:

```text
chore: prepare MarketPulse final release
```

Suggested PR title:

```text
chore: prepare MarketPulse final release
```

The PR description should summarize:

```text
cleanup
dependency verification
README changes
runtime validation
fresh-run result
final provider or access mode
known environment constraints
```

# Part 11 - Review and merge

Another student reviews the integration PR.

Reviewer checklist:

```text
[ ] README commands match the repository
[ ] requirements.txt matches direct imports
[ ] no secret is committed
[ ] no temporary debug artefact remains
[ ] final provider is documented honestly
[ ] terminal path works
[ ] dashboard path works
[ ] snapshot architecture is preserved
[ ] no unrelated feature was introduced
```

Merge only after a real review.

# Part 12 - Validate merged main

After merge:

```bash
git switch main
git pull
git status
python src/main.py
```

Then:

```bash
python src/dashboard.py
```

The final validation must use the merged version.

# Part 13 - Checkpoint C capture

Checkpoint C is now captured.

Canonical contract:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

Required filenames:

```text
README.md
01_final_market_data.png
02_dash_dashboard.png
03_final_pull_request.png
04_reproducible_run.png
```

Optional:

```text
05_advanced_deployment.png
```

Store under:

```text
evidence/checkpoint-c/<github-username>/
```

For `03_final_pull_request.png`:

```text
meaningful TD09-TD12 PR
+
attributable to the student
```

For `04_reproducible_run.png`, capture a successful clean or freshly prepared run.

If an external package index or platform outage prevents the clean installation during the scheduled capture, use the `PENDING_EXTERNAL` recovery rule defined in:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

Do not present a failed install as successful reproducibility evidence.

It does not have to be the single team final integration PR.

Do not create duplicate release PRs just to manufacture evidence.

# Part 14 - Capture checklist

Before leaving:

```text
[ ] final market-data provider or mode is visible honestly
[ ] dashboard shows instrument + benchmark
[ ] lookback and interval are visible
[ ] three performance values are visible
[ ] base-100 comparison is visible
[ ] my PR evidence is attributable to me
[ ] reproducible run uses final integrated code
[ ] no secret appears in evidence
```

Screenshots do not replace live execution and explanation.

# OPTIONAL / REFERENCE

The following are outside TD12 CORE.

## Optional 1 - Advanced deployment

Use only if the team already has a legitimate optional deployment path.

Possible examples from the broader optional track include remote Linux or a simple service setup.

Do not add deployment infrastructure solely for the screenshot.

## Optional 2 - Docker

Docker is optional.

Do not introduce it as a release blocker.

## Optional 3 - GitHub Actions

GitHub Actions is showcase material only.

Do not add CI badges to a team README unless the corresponding workflow really exists and passes.

## Reference - Full evidence rules

Use:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

for:

```text
evidence meaning
individual README fields
live validation
assessment guidance
advanced optional evidence
```

Do not duplicate those rules in TD12.

# ADVANCED

Advanced work starts only after TD12 CORE and Checkpoint C preparation are complete.

Advanced work is not required for Checkpoint C.

## ADV-GIT-04 - Tags and Releases

Status:

```text
READY_TO_TEACH
```

Prerequisites:

```text
TD12 CORE complete
clean completed repository
```

Estimated duration:

```text
30-45 minutes
```

Support:

[ADV-GIT-04 - Tags and Releases](../advanced/ADV_GIT_04_TAGS_RELEASES.md)

## External-gated advanced paths

The following P1 supports exist but are not active student exercises yet:

```text
ADV-RMT-01 - SSH Fundamentals
ADV-RMT-03 - systemd Service
```

Current status:

```text
PENDING_EXTERNAL
```

They require an approved remote Linux teaching environment before activation.

# Final readiness check

The team should confirm:

```text
[ ] repository can be cloned
[ ] dependencies install from requirements.txt
[ ] documented provider prerequisite is accurate
[ ] python src/main.py works
[ ] python src/dashboard.py works
[ ] final main was reviewed
[ ] fresh or clean run was demonstrated
[ ] Checkpoint C filenames are exact
[ ] no invented evidence exists
```

Each student should be able to explain:

```text
provider
canonical rows
analytics
snapshot
terminal
dashboard
Pull Request
review
reproducibility
personal contribution
```

# What comes next?

The guided 18-hour MarketPulse practical path is complete.

```text
Wave 1 - Foundations
Wave 2 - Git and Collaboration
Wave 3 - Comparison and Yahoo Finance
Wave 4 - Professional Integration
```

The separate final project remains an autonomous assessment.

MarketPulse provides the reusable principles:

```text
Python
Git
Linux
provider boundaries
normalization
analytics
Dash
collaboration
reproducibility
```

The guided sequence is complete.

For future course delivery, instructor readiness and recovery are governed by:

```text
docs/15_INSTRUCTOR_CONTINGENCY_AND_RECOVERY_PLAYBOOK.md
docs/16_TEACHING_BASELINE_RELEASE.md
```
