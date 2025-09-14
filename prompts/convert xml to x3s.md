Title: Convert fixtures in tools/fixtures/known_good/mods/* to per-mod .x3s folders

Objective
For every mod folder under tools/fixtures/known_good/mods/<mod_name>/, convert X3 Script XML files (codearray/line) to .x3s and place results in tools/fixtures/known_good/<mod_name>/. Preserve text pages; do not modify sources in mods/.

Scope
- Create/update: tools/convert_mods.py, tools/test_x3s.py (globs), docs/x3s-language.md (note about fixtures).
- Write only under: tools/fixtures/known_good/<mod_name>/**.
- Read-only from: tools/fixtures/known_good/mods/**.
- Do NOT edit src/scripts/** or game code.

Desired output layout (per mod)
tools/fixtures/known_good/<mod_name>/
  src/scripts/*.x3s        # converted scripts (source of truth)
  t/*.xml                  # copied text pages (e.g., 89xxx-L044.xml)
  director/ (optional)     # copy MD XML if present (no conversion)
  README.md                # auto note: generated from mods/<mod_name> on <date>

Conversion rules
- Detect X3 script XML by root/tag path: <codearray><line>…</line>…</codearray>.
- For each script XML:
  - Output filename: <original_basename>.x3s (e.g., plugin.slx.foo.xml → plugin.slx.foo.x3s).
  - Prepend header lines if discoverable:
    - #name: <original_basename>
    - #page: <NNNNN> (from first "load text: id=NNNNN" line if present)
    - #lang: 44 (if a matching -L044 t-file is also copied)
    - #origin_mod: <mod_name>
    - #source: mods/<mod_name>/scripts/<original_basename>.xml
  - Body: one line per <line> text, trimmed of trailing spaces; preserve order and decode entities.
- Copy any t/*-L*.xml into <mod_name>/t/ unchanged.
- If director/ exists, copy directory as-is into <mod_name>/director/ (no conversion).
- Skip files that are not XML (e.g., .pck) and log a note in README.md.

Tooling to add/change
1) tools/convert_mods.py
   - Walk mods/* (only immediate children as <mod_name>).
   - For each <mod_name>, create target dirs (src/scripts, t, director).
   - Convert scripts/*.xml as above; copy t/*.xml; copy director/ if present.
   - Write/append README.md with a summary (counts, skipped files).
   - Exit nonzero if zero scripts were converted for a mod folder that has scripts/.

2) tools/test_x3s.py
   - Update globbing to lint recursively:
     - known-good .x3s: tools/fixtures/known_good/**/src/scripts/*.x3s
     - (Keep negative tests in tools/fixtures/should_fail/**, if present.)
   - Run the linter over all discovered .x3s and assert pass.

3) docs/x3s-language.md
   - Append a short “Fixtures” note describing the per-mod layout and that .x3s are canonical for tests.

Safety & non-goals
- Never overwrite mods/ content.
- If output exists, overwrite files idempotently but do not delete unexpected files.
- Do not weaken linter safety checks.

Acceptance Criteria
- Running: `python tools/convert_mods.py` prints a summary and creates per-mod folders under tools/fixtures/known_good/.
- Running: `python tools/test_x3s.py` lints all newly created .x3s successfully.
- Each generated .x3s has headers (#name, #origin_mod; #page/#lang when discoverable).
- Text pages are present under each <mod_name>/t/ when they existed in the source.
- No changes outside tools/** and tools/fixtures/known_good/**.
- README.md in each <mod_name>/ explains provenance and timestamp.

Nice-to-have (if trivial)
- Detect `load text: id=NNNNN` by scanning lines while converting to set #page.
- Count and report skipped .pck files per mod.
- Normalize line endings to LF.

Plan (suggested commit order)
1) Add tools/convert_mods.py + docs note.
2) Update tools/test_x3s.py recursive globs.
3) Run convert script locally; commit generated fixtures.
4) Show test output in PR body.