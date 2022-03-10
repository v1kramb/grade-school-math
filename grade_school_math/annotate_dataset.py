# Simple script to add steps to json files
import json
import jsonlines
import os

path = 'grade_school_math/data/'

files = ["train.jsonl", "train_socratic.jsonl", "test.jsonl", "test_socratic.jsonl"]

for filename in files:
    newfile = 'a_' + filename
    with jsonlines.open(path + newfile, mode='w') as writer:
        with jsonlines.open(path + filename) as reader:
            for obj in reader:
                obj['steps'] = obj['answer'].count('\n')
                writer.write(obj)        
