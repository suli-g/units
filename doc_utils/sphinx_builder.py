import os
import shutil
import subprocess as sp
from typing import Optional


class SphinxBuilder:
    _command: list[str]
    source: str
    destination: str

    def __init__(
        self,
        root_dir: str,
        source_path: str,
        output_path: str,
        output_type: Optional[str] = "html",
    ):
        self.source = os.path.join(root_dir, source_path)
        self.destination = os.path.join(root_dir, output_path)

        self._command = ["sphinx-build"]
        if output_type is not None:
            self._command.extend(["-M", output_type])
        self._command.extend([self.source, self.destination])

    def reset(self):
        html_directory = os.path.join(self.destination, "docs")
        if os.path.exists(html_directory):
            shutil.rmtree(html_directory)
        return self

    def build(self):
        sp.run(self._command)
        return self

    def move_to(self, docs_path: str):
        if self.destination != docs_path:
            shutil.move("html", docs_path)
        return self

    def add_no_jekyll(self, docs_path: str):
        open(os.path.join(docs_path, ".nojekyll"), "x").close()
        return self

    @property
    def command(self) -> str:
        return " ".join(self._command)
