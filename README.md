# claude-batch

CLI to send and manage Anthropic/Claude Batch API requests.

Status: project skeleton with hello-world CLI. MCP server not implemented yet.

## Requirements
- Python 3.12
- uv (package and runtime manager)

## Quickstart
```bash
# Install uv if needed: https://docs.astral.sh/uv/
uv run claude-batch --help
uv run claude-batch -n Alice
```

## Development
```bash
uv sync
uv run ruff format
uv run ruff check --fix
uv run basedpyright --level=error
uv run pytest -q
```

## Pre-commit
On commit, hooks run:
- ruff format (check)
- ruff check --fix
- basedpyright (errors only)
- pytest

Install pre-commit locally if desired:
```bash
uvx pre-commit install
```

## Roadmap
- Implement batch submission/status/results subcommands
- Add MCP server that wraps the CLI for agents
