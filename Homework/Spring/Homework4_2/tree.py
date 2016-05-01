# -*- coding: utf8 -*-
from scipy.ndimage import imread
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics.classification import accuracy_score


def get_images(dir_name):
    images = []
    for file_name in os.listdir(dir_name):
        x = imread(dir_name + "/" + file_name, flatten=True)
        x.shape = (30625, )
        images.append(x)
    images = np.array(images)
    return images


maple = get_images("maple")
non_maple = get_images("non_maple")
# test = get_images("lol")
np.random.shuffle(maple)
np.random.shuffle(non_maple)
# np.random.shuffle(test)

print(maple.shape)
print(non_maple.shape)

train_m = maple[:135, ]
train_non_m = non_maple[:100, ]

validate_m = maple[135:, ]
validate_non_m = non_maple[100:, ]

train = np.concatenate((train_m, train_non_m))
validate = np.concatenate((validate_m, validate_non_m))

train_y = np.concatenate((np.ones(135), np.zeros(100)))
res = []
for i in (RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier, GradientBoostingClassifier):
    res.append((str(i).split(".")[-1])[:-2])
    print(res)
    for j in (10, 20, 40, 80, 100, 150, 200, 300, 400, 500, 1000):
        random_forest = i(n_estimators=j)
        random_forest = random_forest.fit(train, train_y)

        validate_y = np.concatenate((np.ones(37), np.zeros(35)))
        predicted_y = random_forest.predict(validate)

        res.append(accuracy_score(validate_y, predicted_y))
f_res = open("table.txt", "w")
for i in (res[0:12], res[12:24], res[24:36], res[36:48]):
    f_res.write(str(i))
    f_res.write("\n")
f_res.close()
