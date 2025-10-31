from __future__ import annotations

from click.testing import CliRunner

from claude_batch.cli import cli


def test_cli_default_greeting() -> None:
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert "Hello, world!" in result.output


def test_cli_custom_name() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["--name", "Alice"])
    assert result.exit_code == 0
    assert "Hello, Alice!" in result.output


def test_cli_version_flag() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    assert "claude-batch" in result.output
