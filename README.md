# FastText Solutions Journalism Example
This is a quick example of building a model from the Solutions Journalism data using the FastText module.
This was originally made as a REST-like service using Flask.

## Converter
The converter will take JSON input from a positive (-p) and negative file (-n), as well as a comma-separated list of labels (-l) representing the field names in the JSON file.

Example command: python3 fasttext-converter-neg-pos.py -p data/positive.json -n data/negative.json -l 'title,full_text'


## Trainer
The trainer will take the output file from the Converter as input (-i), and the name of the model (-m) to be used in the training as mandatory parameters.
Options for the model are: supervised, skipgram, and cbow.
Optional parameters also include '--epoch,--ngrams,--label'
[Visit the FastText page for more information on parameters.](https://pypi.python.org/pypi/fasttext)

Example command: python3 fasttext-trainer.py -i tmp/tmp123 -m cbow


## Tester
The tester will take the output file from the the Trainer as a model (-m), and a test file as input (-t), and will print basic results output by the FastText classifier.

Example command: python3 fasttext-trainer.py -m tmp/tmp456 -t testfile

