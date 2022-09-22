import os
import json
import argparse

from src.Controller import Controller
        
parser = argparse.ArgumentParser()
parser.add_argument("--path", "-p", type=str, required=True, help="Path to examination directory")
args = parser.parse_args()


f = open('options.json', encoding="utf8")
  
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