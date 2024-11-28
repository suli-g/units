from sphinx_builder import SphinxBuilder

SPHINX_COMMAND = ["sphinx-build", "-M", "html"]


def build_docs_and_move(
    root_dir: str = ".",
    source_path: str = "sphinx/source",
    output_path: str = ".",
    docs_path: str = "docs",
):
    builder = SphinxBuilder(root_dir, source_path, output_path)
    builder.reset().build().move_to(docs_path).add_no_jekyll(docs_path)
