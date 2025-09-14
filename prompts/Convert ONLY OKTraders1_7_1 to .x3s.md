Title: Convert ONLY OKTraders1_7_1 to .x3s and fix per-character line bug

Objective
Convert X3 Script XML under \tools\fixtures\mods\OKTraders1_7_1\ into .x3s and place results in tools/fixtures/known_good/OKTraders1_7_1/, copying t/ and director as-is. Fix the previous bug that emitted one output line per CHARACTER instead of one per <line> node.

Scope
- Edit/Create:
  - tools/convert_mods.py (limit to a single mod path; bugfix)
  - tools/test_x3s.py (add checks for OKTraders1_7_1)
  - tools/fixtures/known_good/OKTraders1_7_1/** (generated outputs + README)
- Read-only:
  - \tools\fixtures\mods\OKTraders1_7_1\**
- Do NOT touch src/scripts/** or gameplay code.

Inputs
- Mod root (Windows path): \tools\fixtures\mods\OKTraders1_7_1
- Expected output root (POSIX): tools/fixtures/known_good/OKTraders1_7_1

Conversion rules
- Detect X3 script XML by <codearray><line>…</line></codearray>.
- For each scripts/*.xml:
  - Output: tools/fixtures/known_good/OKTraders1_7_1/src/scripts/<basename>.x3s
  - Header (if discoverable):
    - #name: <basename>
    - #origin_mod: OKTraders1_7_1
    - #source: mods/OKTraders1_7_1/scripts/<basename>.xml
    - #page: <NNNNN> (from first “load text: id=NNNNN” line, if present)
    - #lang: 44 (if a -L044 t-file exists in the mod)
  - Body: **write exactly one output line for each XML <line>’s text** (trim trailing spaces). No per-character splits.
- Copy any t/*.xml verbatim to tools/fixtures/known_good/OKTraders1_7_1/t/
- If director/ exists, copy as-is to tools/fixtures/known_good/OKTraders1_7_1/director/

Bugfix (mandatory)
- The last attempt produced one line per character. Fix by:
  - When reading XML, collect `node.text` as a full string (coerce None → ""), do not iterate the string.
  - When writing, call `f.write(line.rstrip() + "\n")` once per input line. **Never loop over characters.**
  - Normalize newlines to LF (`newline="\n"`).

Implementation tasks
1) Update tools/convert_mods.py to accept a `--single-mod` (or `--mods-dir`) pointing to \tools\fixtures\mods\OKTraders1_7_1 and to write into tools/fixtures/known_good/OKTraders1_7_1. Normalize path separators via pathlib.
2) Ensure converter logic:
   - `is_x3_script_xml`: root.tag == "codearray" and contains at least one "line".
   - `extract_lines`: return a list of **full** line strings from each <line>.
   - `write_x3s`: write headers then each line once; no char iteration.
3) Write README.md in the output folder summarizing counts and timestamp.
4) Update tools/test_x3s.py to:
   - Run the converter for this one mod.
   - Assert: for every converted file, **# of XML <line> nodes == # of non-header lines** in the .x3s (blank lines allowed between header/body).
   - Run x3s linter (tools/x3s_lint.py) on the generated .x3s and expect pass.

Acceptance criteria
- Running:
  - `python tools/convert_mods.py --single-mod "\tools\fixtures\mods\OKTraders1_7_1" --out-dir tools/fixtures/known_good`
  prints a summary and generates outputs only under tools/fixtures/known_good/OKTraders1_7_1/**.
- For each converted script:
  - `<line>` count equals .x3s body line count (excluding header and empty separator lines).
  - **No .x3s contains more than 0 single-character body lines unless the source <line> was a single character.**
- `python tools/test_x3s.py` passes (converter + line-count assertions + linter).
- README.md exists with counts (converted/skipped, t-files copied, director copied) and a timestamp.
- No files outside tools/** and tools/fixtures/** are changed.

Notes
- Treat the provided Windows path as the input; use pathlib so the script works cross-platform.
- Skip non-<codearray> XML or .pck files; record in README notes.
- Keep diffs tight and avoid weakening linter rules.

Plan (suggested commits)
1) convert_mods.py: add single-mod mode + per-line write fix.
2) test_x3s.py: add conversion + equality-of-line-count check for OKTraders1_7_1.
3) Run conversion; commit generated fixtures and README.
4) Show test output in PR body.
