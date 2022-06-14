import typer

from cmd.creating_folder import create_folder
from cmd.git import git_automate

app = typer.Typer()

app.add_typer(create_folder.app, name='createfolder')

# All git automation will be done using this command

app.add_typer(git_automate.app, name='git')



if __name__ == "__main__":
    app()
