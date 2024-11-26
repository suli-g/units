import os
import shutil
import subprocess as sp

SPHINX_COMMAND = ["sphinx-build", "-M", "html"]


def build_docs_and_move(
    source_path: str = ".",
    generated_directory="html",
    docs_directory="docs",
):
    os.chdir(source_path)

    def process():
        source = os.path.join(source_path, generated_directory)
        destination = os.path.join(source_path, docs_directory)
        command = SPHINX_COMMAND + [
            os.path.join(source_path, "sphinx", "source"),
            source_path,
        ]
        print("Removing old documentation at", destination)
        shutil.rmtree(destination)
        print(
            "Generating documentation...",
            f"Executing command: {" ".join(command)}",
            sep="\n",
        )
        sp.run(
            command,
            cwd=source_path,
            capture_output=True,
        )
        if source == destination:
            return

        print(f"Renaming directory '{source}' to '{destination}' ")
        os.rename(
            "html",
            "docs",
        )
        print(f"Documentation generated at '{destination}' ")

    process()
