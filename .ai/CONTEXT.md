Agent-facing technical context

What this repo is
- Python 3.12 project providing CLI `claude-batch`
- Goal: manage Anthropic/Claude Batch API workflows
- MCP server planned (will reuse CLI); not implemented yet

Tooling & conventions
- Package/runtime: uv only (no pip/poetry/virtualenv)
- Code style: PEP 8, Google-style docstrings required
- Lint/format: ruff (format + check --fix)
- Type checking: basedpyright (recommended mode)
- Tests: pytest with pytest-mock

Type checking workflow
- Development: run `basedpyright` (all levels) to check changes
- Automatic (CI/pre-commit): `basedpyright --level=error` only
- Minimize warnings/info diagnostics during development

Current CLI (hello-world)
- `claude-batch --help` for usage
- `claude-batch --version` prints version
- `claude-batch -n NAME` prints greeting


