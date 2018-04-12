import fasttext
import tempfile
import sys

args = sys.argv

def execute(self, input):

    # Verify that mandatory parameters were given
    if "-t" not in args:
        return "ERROR: No input test file was given"
    if "-m" not in args:
        return "ERROR: No model was given"

    # Extract names of files
    test_file = args[args.index("-t")+1]
    model_file = args[args.index("-m")+1]
    
    # Load model
    classifier = fasttext.load_model(model_file)
    
    # Test the given file using the loaded classifier
    result = classifier.test(test_file)
    return vars(result)

execute()