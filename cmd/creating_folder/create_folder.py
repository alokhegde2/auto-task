"""
This is the test folder created 
This should be deleted once project reaches one stage

"""

import typer
import os

app = typer.Typer()


@app.command()
def create(path: str):
    """
    Please run this command in the base directory or root directory 
    """
    try:
        data = os.system(f"cd cmd && dir")
    except:
        typer.echo(f"Error")
        exit()

    typer.echo(f"Creating user:")


@app.command()
def delete(user_name: str):
    typer.echo(f"Deleting user: {user_name}")


if __name__ == "__main__":
    app()
