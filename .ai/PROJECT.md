claude-batch: project overview

Scope
- CLI tool to send and manage Anthropic/Claude Batch API requests
- MCP server: planned, not implemented yet

Core principles
- Python 3.12 only
- Strictly use uv for Python and package management
- Code quality: PEP 8, Google-style docstrings, ruff (format + check --fix), basedpyright (recommended)
- Tests: pytest with pytest-mock

Repository policies
- Pre-commit: ruff format (check), ruff check --fix, basedpyright (errors only), pytest
- CI: same checks via GitHub Actions on push/PR

Next milestones
- Define CLI subcommands for batch submission, status, and results retrieval
- Implement MCP server that wraps the CLI for agents


