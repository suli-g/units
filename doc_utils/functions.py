import subprocess as sp

from sphinx_builder import SphinxBuilder

SPHINX_COMMAND = ["sphinx-build", "-M", "html"]


def build_docs_and_move(
    source_path: str = ".",
    generated_directory: str = r"sphinx\source",
    docs_directory: str = "docs",
):
    builder = SphinxBuilder(source_path, generated_directory, docs_directory)
    print(builder.command)
    builder.build()
    # builder.move()
