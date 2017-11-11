"""List of cli commands for working with Open Edge workers"""

import click

@click.group(name='worker')
def workercmds():
    """Working with Open Edge workers"""
    pass


@workercmds.command()
def list():
    """List current workers"""
    pass


@workercmds.command()
def add():
    """Add new worker"""
    pass
