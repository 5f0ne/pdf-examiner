# Description

Provides an overview of the inner file structure of a PDF and extracts /URI and /JS data.

# Configuration

`options.json` contains the rules for searching the PDF document.
If you want to have additional information, just add a new object to this file. The following provides an example of an object:

```json
[
    {
        "name": "obj",                  // The name of the entity which shall
                                        // be found. Just acts as a display name
        "type": "tag",                  // There are 5 different types:
                                        //      - metadata 
                                        //      - action
                                        //      - tag
                                        //      - code
                                        //      - embedded
                                        // These types take care of the order within
                                        // the output (see example.txt)
        "action": "count",              // There are 2 different actions:
                                        //      - count (Counts all regex matches)
                                        //      - value (Provides the value of a 
                                        //               regex)
        "regexes": ["(?<!end)obj"]      // The regex to find what you need. Make
                                        // sure, it matches the selected action
    }
]
```

# Usage

`main.py [-h] --path PATH`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path to the PDF directory |


# Example

`python main.py -p "path/to/pdf" > result.txt`

You can find the following result [here](./example/example.txt):

```
################################################################################

PDF Examiner by 5f0
Provides an overview of the inner file structure of a PDF

Current working directory: /path/to/pdfs
Investigated PDFs in: ./sample-files

Total numbers of examined PDFs: 1

Datetime: 01/01/1980 11:12:13

################################################################################

Examined file: ./sample-file/sample.pdf

     MD5 Hash: 851acee02bd8d002e3b9af184d0c8959
  SHA256 Hash: f723638db6e763cf4ccadad38a3d38a02d9ecab95dab1f0aebf00e801991b5f92

--> Version: %PDF-1.5

--> Metadata:

/Author             : ['5f0']
/Creator            : ['LaTeX with hyperref package']
/Producer           : ['pdfTeX-1.40.16']
/CreationDate       : ["D:19700101193102+02\\'00\\'"]
/ModDate            : ["D:19700101193102+02\\'00\\'"]


--> Tags:

obj                 : 6
endobj              : 6
stream              : 5
endstream           : 5
xref                : 0
startxref           : 1
trailer             : 0

--> Actions:

/Action             : 1
/URI                : 2
/URI values         : ['http://example.com/']
/OpenAction         : 1
/Named              : 0
/Launch             : 0
/AcroForm           : 0

---> Code:

/JavaScript         : 2
/JS                 : 1
/JS values          : ['var v = app.viewerVersion;']

---> Embedded:

/RichMedia          : 0
/EmbeddedFile       : 0
/Encrypt            : 2

################################################################################

Execution Time: 0.048780 sec
```


# License

MIT