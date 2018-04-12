import tempfile
import json
import sys

args = sys.argv

# Removes None and empty strings from dataset
def filter_blanks(dataset):
    return [val for val in dataset if val is not None and val != '']

# Get the field from the dataset for dictionaries and other datasets
def getfield(dataset, field):
    if isinstance(dataset, dict):
        index = dataset['fields'].index(field)
        return filter_blanks([row[index] for row in dataset['values']])
    else:
        return filter_blanks([row[field] for row in dataset])

def execute():

    # For each mandatory argument, verify that it is specified, and extract data
    if "-p" not in args:
        return "ERROR: No positive examples file was given"

    if "-n" not in args:
        return "ERROR: No negative examples file was given"

    if "-l" not in args:
        return "ERROR: A valid list of labels must be given, in order to create appropriate temporary files for fasttext"

    

    # Extract positive data
    input_pos = args[args.index("-p")+1]
    with open(input_pos, 'r') as f:
        json_pos = json.load(f)

    # Extract negative data
    input_neg = args[args.index("-n")+1]
    with open(input_neg, 'r') as f:
        json_neg = json.load(f)

    # Extract labels
    labels = args[args.index("-l")+1].split(',')
    all_labels = []


    # Labels are made follwing the format for fasttext input
    for each in labels:
        label_data = getfield(json_pos, each)
        all_labels.extend(['__label__pos %s' % ex for ex in label_data])
        label_data = getfield(json_neg, each)
        all_labels.extend(['__label__neg %s' % ex for ex in label_data])

    # Create a temporary file
    tmp, filename = tempfile.mkstemp()

    # Write data to temporary file
    with open(tmp, 'w') as f:
        f.write('\n'.join(all_labels))

    # Return temporary filename
    return filename


if __name__ == '__main__':
    print(execute())
