Title: Learn from known-good .x3s and update our linter (no XML build)

Objective
Given a set of .x3s files that are known to compile in-game, update our verification tooling so these files lint cleanly while preserving all safety checks (control-flow matching, wait-in-while, setup load-text rule).

Scope
- Modify only: tools/x3s_lint.py, tools/test_x3s.py, docs/x3s-language.md
- If helpful, introduce: tools/x3s_rules.json and tools/fixtures/**
- Do NOT edit src/scripts/*.x3s or game logic.

Inputs
I will paste one or more .x3s files after the marker:
--- FILES START ---
... (one or more .x3s file contents)
--- FILES END ---

Tasks
1) Parse the provided .x3s lines (ignore headers/comments).
2) For any line-shape that currently triggers “unrecognized line” warnings, derive a minimal, specific regex that matches ONLY that statement family (anchor with ^…$, avoid overly broad patterns like `.*`).
3) Externalize patterns:
   - If tools/x3s_rules.json does not exist, create it with schema:
     {
       "patterns": [
         { "name": "al.register", "regex": "^al engine:\\s*register script='[^']+'$", "examples": ["al engine: register script='al.plugin.slx'"] },
         ...
       ]
     }
   - Refactor tools/x3s_lint.py to load allowlist patterns from x3s_rules.json (case-insensitive), keeping structural/safety checks hard-coded (if/else/end stack, while→wait rule, setup load text).
4) Add fixtures:
   - Place all provided .x3s under tools/fixtures/known_good/*.x3s
   - Create ONE negative test file tools/fixtures/should_fail/missing_wait.x3s with a while loop lacking a wait to ensure the safety rule still fails.
5) Update tools/test_x3s.py to:
   - Lint src/scripts/*.x3s and tools/fixtures/known_good/*.x3s (must pass)
   - Lint tools/fixtures/should_fail/*.x3s and assert it fails (nonzero exit)
6) Documentation:
   - Append a “New Statements Recognized” section to docs/x3s-language.md listing the added pattern names and an example line for each.
7) Keep diffs tight and readable. Prefer multiple small regex additions over one permissive catch-all.

Acceptance Criteria
- `python tools/x3s_lint.py` returns OK for all provided .x3s and existing repo files.
- `python tools/test_x3s.py` passes: known_good passes; should_fail fails.
- Safety checks preserved:
  - Unclosed if/while still error
  - while without wait still error
  - setup.* without “load text: id=NNNNN” still error
- Regexes are anchored (^…$), case-insensitive, and not overbroad.
- docs/x3s-language.md updated with the new recognized statements.

Deliverables
- tools/x3s_rules.json (new or updated) with added patterns and examples
- Updated tools/x3s_lint.py loading from x3s_rules.json
- Updated tools/test_x3s.py to include fixtures
- tools/fixtures/known_good/*.x3s and tools/fixtures/should_fail/missing_wait.x3s
- docs/x3s-language.md appendix listing new patterns
- PR body sections: Plan • Changes • Test Results • Pattern List • Safety Checks

Notes
- If a provided line uses variable assignment or general script calls already handled by existing heuristics, do not add redundant patterns.
- Prefer one pattern per statement family (e.g., “al engine: set plugin … description …” and “… timer interval …” are two patterns).
- Never disable or weaken structural/safety checks to make inputs pass; add allowlist patterns instead.
