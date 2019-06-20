import string
from os import listdir
from os.path import isfile, join
from nltk.translate.bleu_score import corpus_bleu
from nltk.translate.nist_score import corpus_nist

reference_directory = 'reference/'

data_directories = [
    'aws/',
    'azure/',
    'google/'
]

references = []
ref_files = [f for f in listdir(reference_directory) if isfile(join(reference_directory, f))]
for file in ref_files:
    with open(reference_directory + file, 'r', encoding="utf8") as f:
        fileTokens = []
        for line in f:
            text = line.translate(str.maketrans('', '', string.punctuation)).lower()
            token = text.split()
            fileTokens.extend(token)        
        references.append([fileTokens])

for directory in data_directories:    
    candidates = []
    only_files = [f for f in listdir(directory) if isfile(join(directory, f))]    
    for file in only_files:        
        fileTokens = []
        with open(directory + file, 'r', encoding="utf8") as f:                        
            for line in f:
                text = line.translate(str.maketrans('', '', string.punctuation)).lower()
                token = text.split()
                fileTokens.extend(token)            
            candidates.append(fileTokens)
    bleu_score = corpus_bleu(references, candidates)
    nist_score = corpus_nist(references, candidates)
    print(directory)
    print("bleu {}".format(bleu_score))
    print("mist {}".format(nist_score))
