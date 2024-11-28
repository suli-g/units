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
        if not os.path.exists(self.destination):
            return
        shutil.rmtree(self.destination)

    def build(self):
        sp.run(self._command)

    def move(self):
        if self.source == self.destination:
            return
        shutil.move("html", "docs")

    @property
    def command(self) -> str:
        return " ".join(self._command)
