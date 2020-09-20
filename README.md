# bigram-model

Представленная модель генерирует продолжение предложения с помощью биграммной языковой модели (при нулевом префиксе начальное слово выбирается случайно) длины, случайно выбираемой из отрезка [7,15]

- файл с обучением модели: 
python fit.py -a [text file location] -b [model save location('pickle_text_gen.pkl' as default)]

- файл с генерацией предложения: 
python generate.py -a [model location]
