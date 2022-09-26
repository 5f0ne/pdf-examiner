import hashlib

from hash_calc.HashCalc import HashCalc
from pdf_examiner.Type import Type

class FileResult():
    def __init__(self, fileName) -> None:
        self.fileName = fileName
        self.patternResults = []
        self.hashCalc = HashCalc(fileName)
        self.pdfVersion = ""

    def print(self):
        print("")
        print("Examined file: " + self.fileName)
        print("")
        print("     MD5 Hash: " + self.hashCalc.md5)
        print("  SHA256 Hash: " + self.hashCalc.sha256)
        print("")
        print("--> Version: " + self.__getVersion())
        self.__printTypes(Type.METADATA, "--> Metadata")
        self.__printTypes(Type.TAG, "--> Tags")
        self.__printTypes(Type.ACTION, "--> Actions")
        self.__printTypes(Type.CODE, "---> Code")
        self.__printTypes(Type.EMBEDDED, "---> Embedded")
        print("")
        print("################################################################################")

    def __getVersion(self):
        r = ""
        with open(self.fileName, "rb") as f:
            data = f.read(8)
        return data.decode("utf8")

    def __printTypes(self, type_, str_):
        print("")
        print(f"{str_}:")
        print("")
        for pR in self.patternResults:
            if(pR.type == type_):
                formatStr = "{:20}: {}"
                print(formatStr.format(pR.name, str(pR.result)))