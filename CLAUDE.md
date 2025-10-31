# CLAUDE context

Purpose
- Enable agents to manage Anthropic/Claude Batch API requests via a CLI.

Current state
- Project skeleton with hello-world CLI (`claude-batch`).
- MCP server planned; not implemented yet.

Conventions
- Python 3.12 only; use `uv` exclusively for Python and packages.
- Code style: PEP 8, Google-style docstrings required.
- Lint/format: ruff; Type-check: basedpyright (recommended); Tests: pytest.
- Development: use `basedpyright` (all levels) to check changes; auto-checks use `--level=error` only.

Usage
```bash
uv run claude-batch --help
uv run claude-batch -n NAME
```

Next
- Add CLI subcommands for batch submit/status/results.
- Implement MCP server that wraps the CLI.
