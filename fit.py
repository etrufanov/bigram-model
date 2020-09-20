from model import TextGenerator
import pickle
import argparse

parser = argparse.ArgumentParser(description='fit model')

parser.add_argument('-a', action="store", dest="text_file")
parser.add_argument('-b', action="store", dest="model_file", default='pickle_text_gen.pkl')

args = parser.parse_args()

try:
    model = TextGenerator()
    # обучение модели
    model.fit(args.text_file)
    print('model successfully fitted!')
except FileNotFoundError:
    print('model not found!')


# сохранение модели
with open(args.model_file, 'wb') as file:
    pickle.dump(model, file)