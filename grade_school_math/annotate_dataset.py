# Simple script to add steps to json files
import json

path = 'grade_school_math/data/'

files = ["train.jsonl", "train_socratic.jsonl", "test.jsonl", "test_socratic.jsonl"]

for filename in files:
    newfile = 'a_' + filename

    with open(path + filename) as fh:
        all_obj = [json.loads(line) for line in fh.readlines() if line]
        for obj in all_obj:
            obj['steps'] = str(obj['answer'].count('\n'))
    
        with open(path + newfile, 'w') as fw:
            for obj in all_obj:
                json.dump(obj, fw)
                fw.write('\n')