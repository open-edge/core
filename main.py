import click

from configs import app_version


@click.group()
def cli():
    """openedge: Open Edge Core cli"""
    pass

@click.command()
def version():
    """Show version information"""
    click.echo('Open Edge Core version {}'.format(app_version))

cli.add_command(version)

if __name__ == '__main__':
    cli()
