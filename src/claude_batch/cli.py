from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

import click


def _get_version() -> str:
    try:
        return version("claude-batch")
    except PackageNotFoundError:
        return "0.1.0"


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option(
    "--name", "name", "-n", default="world", show_default=True, help="Name to greet."
)
@click.version_option(_get_version(), prog_name="claude-batch")
def cli(name: str) -> None:
    """Hello-world entry point for claude-batch."""
    click.echo(f"Hello, {name}!")


def main() -> None:
    cli()
