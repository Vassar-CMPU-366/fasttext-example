# FastText Solutions Journalism Example
This is a quick example of building a model from the [Solutions Journalism](https://www.solutionsjournalism.org) data using the FastText module.
This was originally made as a REST-like service using Flask. 

The data we have so far is your starting point (until we get the additional data promised). The fasttext implementation is for reference--you can use it as a basis to build on or use whatever approach you want. Note it is not necessary to create a web service, but it would be nice to do so since the Solutions Journalism people ultimately want that.

## Converter
The converter will take JSON input from a positive (-p) and negative file (-n), as well as a comma-separated list of labels (-l) representing the field names in the JSON file.
```
Example command: python3 fasttext-converter-neg-pos.py -p data/positive.json -n data/negative.json -l 'title,full_text'
```

## Trainer
The trainer will take the output file from the Converter as input (-i), and the name of the model (-m) to be used in the training as mandatory parameters.

Options for the model are: supervised, skipgram, and cbow.

Optional parameters also include '--epoch,--ngrams,--label'

[Visit the FastText page for more information on parameters.](https://pypi.python.org/pypi/fasttext)
```
Example command: python3 fasttext-trainer.py -i tmp/tmp123 -t supervised
```

## Tester
The tester will take the output file from the the Trainer as a model (-m), and a test file as input (-t), and will print basic results output by the FastText classifier.
```
Example command: python3 fasttext-trainer.py -m tmp/tmp456 -t testfile
```
