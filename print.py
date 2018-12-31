from pathlib import Path
from pick import pick
from os.path import isfile, join
from os import listdir
import re
import json

storiesPath = "./stories/"

def retFileListByExtension(extension, path):
    return [f for f in listdir(path) if isfile(
        join(path, f)) and f.endswith(extension)]

storyFiles = retFileListByExtension(".txt", storiesPath)

title = 'Choose story: '
option, index = pick(storyFiles, title)
storyPath = storiesPath + option

storyFile = Path(storyPath).read_text()

storyVariables = set(re.findall(r'\{(.*?)\}', storyFile))
storyCharacter = {}
for v in storyVariables:
    storyCharacter[v] = input(v + ": ")

with open(storyPath, 'r') as myfile:
    data = myfile.read()
    for k, v in storyCharacter.items():
        # print(k)
        data = data.replace('{'+k+'}', v)

    print(data)