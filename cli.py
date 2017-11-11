import click

from configs import app_version
from cli.workercmds import workercmds


@click.group()
def cli():
    """openedge: Open Edge cli"""
    pass

@cli.command()
def version():
    """Show version information"""
    click.echo('Open Edge Core version {}'.format(app_version))

cli.add_command(workercmds)

if __name__ == '__main__':
    cli()
