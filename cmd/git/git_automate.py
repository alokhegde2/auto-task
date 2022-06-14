"""
Git automate contains all the dails commands which will be runned daily
"""

import subprocess
import typer

app = typer.Typer()


def asciiLetterPrint():
    typer.secho("""

░█████╗░██╗░░░██╗████████╗░█████╗░  ████████╗░█████╗░░██████╗██╗░░██╗
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗  ╚══██╔══╝██╔══██╗██╔════╝██║░██╔╝
███████║██║░░░██║░░░██║░░░██║░░██║  ░░░██║░░░███████║╚█████╗░█████═╝░
██╔══██║██║░░░██║░░░██║░░░██║░░██║  ░░░██║░░░██╔══██║░╚═══██╗██╔═██╗░
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝  ░░░██║░░░██║░░██║██████╔╝██║░╚██╗
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝

""")


@app.command()
def push_code(msg: str, branch: str = "main"):
    """

░█████╗░██╗░░░██╗████████╗░█████╗░  ████████╗░█████╗░░██████╗██╗░░██╗
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗  ╚══██╔══╝██╔══██╗██╔════╝██║░██╔╝
███████║██║░░░██║░░░██║░░░██║░░██║  ░░░██║░░░███████║╚█████╗░█████═╝░
██╔══██║██║░░░██║░░░██║░░░██║░░██║  ░░░██║░░░██╔══██║░╚═══██╗██╔═██╗░
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝  ░░░██║░░░██║░░██║██████╔╝██║░╚██╗
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝

    """

    # Variable to store

    # Checking for the git repository already initialized or not

    try:
        output = subprocess.check_output(
            ['git', 'status'], stderr=subprocess.STDOUT)
        # typer.echo(output)

    except subprocess.CalledProcessError as e:
        if e.returncode == 128:
            asciiLetterPrint()
            typer.secho(f"Git repository is not initialized\n\n\nWe are terminating the process",
                        fg=typer.colors.RED)

            # Ask for initializing new repo
            newRepoInitStatus = typer.prompt(
                "Do you want to initialize new repo(Y/n)?", default="Y",)

            # IF yes
            if (newRepoInitStatus == "n" or newRepoInitStatus == "N"):
                exit()

            # getting all info before initializing repo

            repoFormat = typer.prompt(
                "Type of repo you want create (rem(Remote),loc(Only-Local))?")

            while (repoFormat != "rem" and repoFormat != "loc"):
                repoFormat = typer.prompt(
                    "Type of repo you want create (rem(Remote),loc(Only-Local))?")

            try:

                # Initializing git repo

                subprocess.check_output(
                    ['git', 'init'], stderr=subprocess.STDOUT)

                typer.secho(f"Git repo initialized.",
                            fg=typer.colors.GREEN)

                subprocess.check_output(
                    ['git', 'branch', '-M', "main"], stderr=subprocess.STDOUT)

                typer.secho(f"Added main as the default branch.",
                            fg=typer.colors.GREEN)

                # if the repo format is remote
                # Or user want to connect the local repo with cloud
                if repoFormat == "rem":

                    # Getting remote url

                    remoteUrl = typer.prompt(
                        "What is the remote url of your github repo?")

                    while(remoteUrl == "" and remoteUrl == " "):
                        remoteUrl = typer.prompt(
                            "What is the remote url of your github repo?")

                    subprocess.check_output(
                        ['git', 'remote', 'add', 'origin', remoteUrl], stderr=subprocess.STDOUT)

                    typer.secho(f"Added remote url.",
                                fg=typer.colors.GREEN)

            except subprocess.CalledProcessError as e:

                typer.secho(f"{e.output}",
                            fg=typer.colors.RED)

                exit()

    # If repository is already exists

    # Check for the branches available

    branchStatus = subprocess.check_output(
        ['git', 'branch'], stderr=subprocess.STDOUT)

    decodedBranchStatus = branchStatus.decode()

    # typer.secho(f"{decodedBranchStatus.split('\t')[1]}")

    # Decoding the output message
    # Before decoding output in the format of buffer

    decodedOutputStatus = output.decode()

    currentStatusOfTheRepo = decodedOutputStatus.find("nothing to commit")

    # currentStatusOfTheRepo = -1 means the given message is not found
    if currentStatusOfTheRepo != -1:
        messageIfRepoIsUptoDate = decodedOutputStatus.split('\n')

        asciiLetterPrint()

        typer.secho(f"{messageIfRepoIsUptoDate[1]}\n\n\nWe are terminating the process",
                    fg=typer.colors.GREEN)

        exit()

    # If repo is not upto date
    # Run the following command to push untracked code

    try:
        subprocess.check_output(
            ['git', 'add', '.'], stderr=subprocess.STDOUT)

        subprocess.check_output(
            ['git', 'commit', '-m', msg], stderr=subprocess.STDOUT)

        subprocess.check_output(
            ['git', 'push','--set-upstream','origin',branch], stderr=subprocess.STDOUT)

    except subprocess.CalledProcessError as e:
        asciiLetterPrint()
        typer.secho(f"{e.output}",
                    fg=typer.colors.RED)

        exit()

    asciiLetterPrint()

    typer.secho(f"Code pushed to the repository successfully",
                fg=typer.colors.GREEN)


if __name__ == "__main__":
    app()
