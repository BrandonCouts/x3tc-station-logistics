# AGENTS

## Mission
Automate safe, mechanical X3TC work using **.x3s** source files only. Write scripts, keep IDs organized, lint syntax/structure, and ship docs—no XML build required (use your local compiler when needed).

## Roles
- **Architect** – repo layout, `docs/ids.md`, PR templates.
- **Scriptor (X3S)** – writes `src/scripts/*.x3s` (setup/lib/commands/AL).
- **Textkeeper** – maintains `t/89xxx-L044.xml` strings & ranges.
- **Linter** – runs `tools/x3s_lint.py src/scripts` (syntax/structure checks).
- **Packager** – version bump, changelog, `build/*.zip` (optional).

## Repository Layout
- `src/scripts/` – author here in `.x3s` (single source of truth)
- `t/` – text pages (e.g., `89001-L044.xml`)
- `docs/` – `ids.md`, `x3s-language.md`, design notes
- `tools/` – `x3s_lint.py`, `test_x3s.py`
- `build/` – artifacts (zips, version.txt)

## Conventions
- Names: `setup.plugin.slx.*`, `plugin.slx.<feature>.*`, `lib.slx.*`, `al.plugin.slx.*`
- Globals: `g.slx.<domain>.<name>`
- Tasks: 101+ for background loops (never task 0)
- Text page: reserve one `89xxx` and record in `docs/ids.md`
- **Setup scripts must include** `load text: id=<89xxx>`

## Workflow (every task)
1. Read `docs/ids.md` + `docs/x3s-language.md`.
2. Create/modify `src/scripts/*.x3s` (+ `t/` strings if needed).
3. Run: `python tools/test_x3s.py` (lints `src/scripts` + unit tests).
4. Fix issues until green.
5. Update `CHANGELOG.md` and `docs/ids.md`.
6. Open PR: include plan, checklist, and any test notes/screens.

## Acceptance Checklist
- `python tools/x3s_lint.py src/scripts` passes (no errors).
- Setup scripts contain `load text: id=<page>`.
- No busy loops: each `while` block contains a `wait`.
- IDs/tasks/command slots match `docs/ids.md`.
- No hardcoded UI text—strings live in `t/`.

## Example (.x3s)
```
* ****************************************************************************** 
* SCRIPT NAME: setup.plugin.slx
* DESCRIPTION: SLX Station Logistics X3  (setup + AL plugin registration + loop guard)
* AUTHOR:      Codex              DATE: 8 September 2025 
* ******************************************************************************

$PageId = 9055
load text: id=$PageId

$section = read text: page=$PageId id=101
$txt = read text: page=$PageId id=102

al engine: register script='al.plugin.slx'
al engine: set plugin 'al.plugin.slx' description to 'SLX Station Logistics'
al engine: set plugin 'al.plugin.slx' timer interval to 30 s
return null
```

### Additional Notes
- When required tools or directories are missing, coordinate with the **Architect** to bootstrap the repo structure.
- Keep commits focused; run tests after each change.
- Fixtures under `tools/fixtures/` are reference-only pseudo code; never treat them as canonical sources.
