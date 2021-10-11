import typer
import time
import os
from rich.console import Console
from rich.tree import Tree
from rich.table import Table
from rich.progress import track
from rich import inspect

APP_NAME = 'multi_command'  # same name specified in setup.cfg
APP_DIR = typer.get_app_dir(APP_NAME)
app = typer.Typer()
console = Console(record=True)


@app.callback()
def app_callback():
    """this is the app_callback docstring"""
    console.log(
        f':briefcase: config directory for {APP_NAME}: {APP_DIR}',
        style='bold blue'
    )


@app.command()
def progress():
    """How do progress bars look?"""
    n_tasks = 100
    console.log(f'performing {n_tasks} tasks :rocket:', style='bold magenta')
    for n in track(range(n_tasks), description='doing stuff'):
        # Fake processing time
        time.sleep(1.2 / n_tasks)
    console.log(f'[blue underline]finished doing stuff! :pile_of_poo:')
    save_output()


@app.command()
def list():
    """What do lists look like?"""
    console.log('lists look like...')
    console.log(os.listdir('.'))
    save_output()

@app.command()
def tree():
    """can it do trees?"""
    console.log('of course it can...')
    tree = Tree("🙂 Alister Burt", guide_style="bold bright_black")

    python_tree = tree.add("📦 Open Source Packages", guide_style="bright_black")
    python_tree.add(
        "[bold link=https://scikit-lego.netlify.app/]napari[/] - [bright_black]nD data viewer in Python"
    )
    employer_tree = tree.add("👨‍💻 Employer", guide_style="bright_black")
    employer_tree.add(
        "[bold link=https://www2.mrc-lmb.cam.ac.uk/]MRC-LMB[/] - [bright_black]Barford Group"
    )

    console.log(tree)
    console.log("")
    console.log(
        "[green]Follow me on twitter [bold link=https://twitter.com/alisterburt]@alisterburt[/]"
    )
    save_output()

@app.command()
def table():
    """What about tables?"""
    table = Table(title="Pandas Versions")

    table.add_column("Released", style="cyan")
    table.add_column("Version Number", justify="right", style="magenta")
    table.add_column("Description", style="green")

    table.add_row("May 29, 2020", "v1.0.4", "Just an update.")
    table.add_row("Mar 18, 2020", "v1.0.3", "Just an update.")
    table.add_row("Mar 15, 2020", "v1.0.2", "Just an update.")
    table.add_row("Feb 05, 2020", "v1.0.1", ":thumbs_up: [underline]Big[/] update.")
    console.log(table)
    save_output()


def save_output():
    output_filename = f'multi_command_output.html'
    console.save_html(output_filename)
    console.log(f'output saved to {output_filename}')