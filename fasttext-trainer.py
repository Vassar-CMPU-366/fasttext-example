import fasttext
import tempfile
import sys

args = sys.argv

def get_optional_param(param, default):
    if param not in args:
        return default

    else:
        return args[args.index(param)+1]


def execute():
    # Verify that mandatory arguments are present
    if "-i" not in args:
        return "ERROR: No input file was given"

    if "-t" not in args:
        return "ERROR: No model type was given"

    # Extract arguments
    train_file = args[args.index("-i")+1]
    model_type = args[args.index("-t")+1]

    # Extract optional arguments
    epoch = get_optional_param('--epoch',5)
    ngrams = get_optional_param('--ngrams',1)
    label_prefix = get_optional_param('--label','__label__')

    # Create temporary file
    tmp, modelname = tempfile.mkstemp()

    # Use specified classifier with parameters and output model to the name of the temporary file
    if model_type == "supervised":
        classifier = fasttext.supervised(train_file, modelname, epoch=epoch, word_ngrams=ngrams, label_prefix=label_prefix)

    elif model_type == "skipgram":
        classifier = fasttext.skipgram(train_file, modelname, epoch=epoch, word_ngrams=ngrams, label_prefix=label_prefix)

    elif model_type == "cbow":
        classifier = fasttext.cbow(train_file, modelname, epoch=epoch, word_ngrams=ngrams, label_prefix=label_prefix)

    # Return the temporary file name
    return modelname

if __name__ == '__main__':
    print(execute())
