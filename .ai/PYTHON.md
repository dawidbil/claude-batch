Python conventions (for agents)

Version & environment
- Python 3.12 required
- Use uv exclusively for Python and dependencies (no pip/poetry/virtualenv)

Code style
- Follow PEP 8
- Use Google-style docstrings for all functions, classes, and modules
- Example:
  ```python
  def function_name(arg: str) -> int:
      """Brief description.

      Longer description if needed.

      Args:
          arg: Description of arg.

      Returns:
          Description of return value.
      """
  ```

Type checking
- Automatic checks (CI/pre-commit): `basedpyright --level=error` only
- Development: run `basedpyright` (all levels) to check changes, but limit warnings/info diagnostics
- Type checking mode: recommended

Common commands
- Sync deps: `uv sync`
- Install dev deps: `uv sync --extra dev`
- Run CLI: `uv run claude-batch`
- Run tests: `uv run pytest -q`
- Format: `uv run ruff format`
- Lint (fix): `uv run ruff check --fix`
- Type check (dev): `uv run basedpyright`
- Type check (auto): `uv run basedpyright --level=error`


