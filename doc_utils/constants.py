from functions import build_docs_and_move

ABBREVIATIONS = {
    "b": "build",
}

COMMANDS = {
    "build": "Builds the documentation and moves it to the 'docs' folder",
}
ACTIONS = {"build": build_docs_and_move}

COMMAND_HELP = "\n".join(
    f"-{short_name}, --{full_name} - {COMMANDS[full_name]}"
    for short_name, full_name in ABBREVIATIONS.items()
)
