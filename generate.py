from model import TextGenerator
import pickle
import argparse

parser = argparse.ArgumentParser(description='generate text')

parser.add_argument('-a', action="store", dest="file")

args = parser.parse_args()

try:
    with open(args.file, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    print('model not found!')

while(True):
    pref = input('enter prefix: ')
    print(model.generate(pref))
