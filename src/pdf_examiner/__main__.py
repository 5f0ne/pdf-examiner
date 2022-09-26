import os
import sys
import json
import argparse

from pdf_examiner.Controller import Controller

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path to examination directory")
    args = parser.parse_args()

    optionsPath = os.path.join(os.path.dirname(__file__), "data", "options.json")
    f = open(optionsPath, encoding="utf8")
    
    options = json.load(f)

    c = Controller(options)

    for path, dirs, files in os.walk(args.path):
        for file in files:
            currentFile = os.path.join(path, file)

            if(".pdf" in currentFile):
                with open(currentFile, "rb") as f:
                    c.setCurrentFile(currentFile)
                
                    bytes_ = f.read()
                    dataString = c.bytesToString(bytes_)

                    s = "".join("".join(d) for d in dataString)
                    
                    c.parse(s)

    c.printHeader(args.path)
    c.printResults()
    c.printExecutionTime()


if __name__ == "__main__":
    sys.exit(main())
