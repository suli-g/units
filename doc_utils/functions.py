from sphinx_builder import SphinxBuilder

SPHINX_COMMAND = ["sphinx-build", "-M", "html"]


def build_docs_and_move(
    root_dir: str = ".",
    source_path: str = "sphinx/source",
    output_path: str = ".",
    docs_path: str = "docs",
):
    builder = SphinxBuilder(root_dir, source_path, output_path)
    print(builder.command)
    builder.reset()
    builder.build()
    builder.move_to(docs_path)
