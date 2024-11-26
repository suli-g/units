import os
import doc_utils.constants as dc


import sys


def main():
    if len(sys.argv) == 1:
        print(
            "Valid flags: ",
            dc.COMMAND_HELP,
        )
        return

    flag = sys.argv[1]
    key = flag.lstrip("-")
    if len(key) == len(flag):
        print(
            f"'{flag}' is not a valid flag.",
            "Prefix the flag with -- to specify the full name of a flag",
            "Prefix the flag with - to specify an abbreviated flag",
            "Example:",
            "\t python generate_docs.py -b",
            sep="\n",
        )
        return

    if key in dc.ABBREVIATIONS:
        key = dc.ABBREVIATIONS[key]
    if key not in dc.COMMANDS:
        print(f"'{flag}' is not a valid flag.")
    else:
        dc.ACTIONS[key](os.path.dirname(__file__))


if __name__ == "__main__":
    main()
