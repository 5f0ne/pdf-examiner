import os
import re
import time

from datetime import datetime

from pdf_examiner.Action import Action
from pdf_examiner.FileResult import FileResult
from pdf_examiner.PatternResult import PatternResult

class Controller():
    def __init__(self, patterns) -> None:
        self.startTime = time.time()
        self.fileResults = []
        self.patterns = patterns
        self.currentFile = ""

    def printHeader(self, path):
        print("################################################################################")
        print("")
        print("PDF Examiner by 5f0")
        print("Provides an overview of the inner file structure of a PDF")
        print("")
        print("Current working directory: " + os.getcwd())
        print("Investigated PDFs in: " + path)
        print("")
        print("Total numbers of examined PDFs: " + str(self.getTotalNoOfPdfs()))
        print("")
        print("Datetime: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("")
        print("################################################################################")

    def printExecutionTime(self):
        end = time.time()
        print("")
        print("Execution Time: " + str(end-self.startTime)[0:8] + " sec")
        print("")

    def getTotalNoOfPdfs(self):
        return(len(self.fileResults))

    def bytesToString(self, bytes_):
        return str(bytes_)

    def setCurrentFile(self, file):
        self.currentFile = file

    def printResults(self):
        for r in self.fileResults:
            r.print()

    def parse(self, s):
        fileResult = FileResult(self.currentFile)
        
        for p in self.patterns:
            result = None
            for regex in p["regexes"]:
                r = re.findall(regex, s)

                if(p["action"] == Action.COUNT):
                    result = PatternResult(p["name"], p["type"], p["action"], len(r))
                elif(p["action"] == Action.VALUE):
                    result = PatternResult(p["name"], p["type"], p["action"], r)
                
                if(result != None):
                    fileResult.patternResults.append(result)
        
        self.fileResults.append(fileResult)

    def clear(self):
        self.results.clear()

