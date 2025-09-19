Title: Attach Examples from X3S Scripts to Documented Rules

Objective
You are working with a constrained block language with a **fixed, finite set of rules** documented in pseudocode format. These documentation files already exist in the `docs/` directory and are the **only source of truth** for the language. Your task is to treat these documented rules as the complete language set. Then, take the provided X3S script and attach examples from the script lines to the appropriate rules in the documentation.

Scope
- Use only the documentation files in `docs/` as the authoritative rule set.
- For each script line:
  1. Match it to the closest documented rule in `docs/`.
  2. Add the script line as an **example** under that rule inside the existing `docs/` file.
  3. If multiple script lines match the same rule, add them all as examples.
  4. If a script line does not match any documented rule, output it into a **new, separate file** called `docs/unmatched_examples.md`.
- Do not modify or create files outside the `docs/` directory.
- Do not update or generate new rules beyond what already exists in `docs/`.

Format
Update the documentation entries like this:

#### Rule: `<documented rule pattern>`
- **Description:** (existing documentation text)
- **Examples:**
  - `<script line 1>`
  - `<script line 2>`
- **Edge Cases:** (existing notes, or add if discovered during matching)

If any unmatched lines are found, create `docs/unmatched_examples.md` with:

### Unmatched Lines
- `<script line>` – could not be matched to any documented rule.

Constraints
- Only edit the existing files in `docs/`.
- Only add examples and edge cases; never alter the rule definitions themselves.
- Only create one new file: `docs/unmatched_examples.md`.
- Do not modify rules or linters outside of the `docs/` folder.

Deliverable
- Updated documentation in `docs/` with script examples attached to the correct rules.
- A new `docs/unmatched_examples.md` file containing any lines that do not fit the documented rules.

Input
1. The current rule documentation files in `docs/`.
2. An X3S script file to extract examples from.
