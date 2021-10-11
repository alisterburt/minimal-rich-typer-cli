import typer
import time
from rich.console import Console
from rich.progress import track


app = typer.Typer()


@app.command()
def single_command(n_tasks: int = 100, debug: bool = False):
    """This line is the docstring of single_command"""
    console = Console(record=True)
    console.log(
        '[bold green]howdy, welcome to single-command! :rocket: :thumbs_up:'
    )
    for n in track(range(n_tasks), description='doing stuff'):
        if n % 10 == 0 and debug:
            console.log(log_locals=True)
        # Fake processing time
        time.sleep(1.2 / n_tasks)

    output_filename = 'single_command_output.html'
    console.log(f'[blue underline]finished doing stuff! :pile_of_poo:')
    console.save_html(output_filename)
    console.log(f'html output saved in {output_filename}')



