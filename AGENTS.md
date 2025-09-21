# AGENTS

## Mission
Automate safe, mechanical X3TC work using **.x3s** source files only. Write scripts, keep IDs organized, lint syntax/structure, and ship docs—no XML build required (use your local compiler when needed).

## Script Archive Requirement
- Save every provided or third-party reference script verbatim under `scripts/provided/` with a descriptive `.x3s` filename before extracting examples for documentation updates.
- Keep archived snippets separate from production gameplay scripts in `src/scripts/`.
- Record any assumptions about archived snippets directly inside the saved file as comments when needed.

## Roles
- **Architect** – repo layout, `docs/ids.md`, PR templates.
- **Scriptor (X3S)** – writes `src/scripts/*.x3s` (setup/lib/commands/AL).
- **Textkeeper** – maintains `t/89xxx-L044.xml` strings & ranges.

## Repository Layout
- `docs/` – language implimentation documents
- `src/scripts/` – author here in `.x3s` (single source of truth)
- `t/` – text pages (e.g., `89001-L044.xml`)
- `docs/` – `ids.md`, `x3s-language.md`, design notes

## Conventions
- Names: `setup.plugin.slx.*`, `plugin.slx.<feature>.*`, `lib.slx.*`, `al.plugin.slx.*`
- Globals: `g.slx.<domain>.<name>`
- Tasks: 101+ for background loops (never task 0)
- Text page: reserve one `89xxx` and record in `docs/ids.md`
- **Setup scripts must include** `load text: id=<89xxx>`
- Ignore any legacy `.xml` files in `scripts/`; they are reference dumps only and must not be edited or treated as source.

# LEARNING
## Attach Examples from X3S Scripts to Documented Rules
You are working with a constrained block language with a **fixed, finite set of rules** documented in pseudocode format. These documentation files already exist in the `docs/language` directory and are the **only source of truth** for the language. Your task is to treat these documented rules as the complete language set. Then, take the provided X3S script and attach examples from the script lines to the appropriate rules in the documentation.

### Scope
- Use only the documentation files in `docs/` as the authoritative rule set.
- For each script line:
  1. Match it to the closest documented rule in `docs/language`.
  2. Add the script line as an **example** under that rule inside the existing `docs/language` file.
  3. If multiple script lines match the same rule, add them all as examples.
  4. If a script line does not match any documented rule, output it into a **new, separate file** called `docs/unmatched_examples.md`.
- Do not modify or create files outside the `docs/` directory.
- Do not update or generate new rules beyond what already exists in `docs/`.

### Format
Update the documentation entries like this:

```
#### Rule: `<documented rule pattern>`
- **Full Description:** (existing documentation text)
- **Examples:**
  - `<script line 1>`
  - `<script line 2>`
- **Edge Cases:** (existing notes, or add if discovered during matching)
```

If any unmatched lines are found, create/update `docs/unmatched_examples.md` with:
- `<script line>` – could not be matched to any documented rule.

### Constraints
- Only edit the existing files in `docs/language`.
- Only add examples and edge cases; never alter the rule definitions themselves.
- Only create one new file: `docs/unmatched_examples.md`.
- Do not modify rules or linters outside of the `docs/` folder.

### Deliverable
- Updated documentation in `docs/language` with script examples attached to the correct rules.
- A new `docs/unmatched_examples.md` file containing any lines that do not fit the documented rules.
- Create docs/x3s-language.md from the language files in docs/language/

### Input
1. The current rule documentation files in `docs/`.
2. An X3S script file to extract examples from.

### Generating docs/x3s-language.md
Update the documentation entries like this:

```
#### Rule: `<documented rule pattern>`
- **Short Description:** (existing documentation text)
- **One Example:**
  - `<script line 1>`
- **Edge Cases:** (existing notes, or add if discovered during matching)
```

# SCRIPTING
## Workflow
1. Read `docs/ids.md` + `docs/x3s-language.md`.
2. Create/modify `src/scripts/*.x3s` (+ `t/` strings if needed).
3. Run: `python tools/test_x3s.py` (lints `src/scripts` + unit tests).
4. Fix issues until green.
5. Update `CHANGELOG.md` and `docs/ids.md`.
6. Open PR: include plan, checklist, and any test notes/screens.

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