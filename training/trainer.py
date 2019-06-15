import dlib

import pandas as pd
from src.preproc import *
from src.get_features import GetFeatures

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# img_io = resize(io.imread(file), 700)

# img_copy = img_io.copy()

gf = GetFeatures()


def get_list_of_cords(file):
    img = cv2.imread(file)
    img = resize(img, 700)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # etect faces
    dets = detector(gray, 1)
    if len(dets) == 0:
        return
    # find face box bounding points
    for d in dets:
        x = d.left()
        y = d.top()
        w = d.right()
        h = d.bottom()

    dlib_rect = dlib.rectangle(x, y, w, h)
    ##############   Find facial landmarks   ##############
    detected_landmarks = predictor(gray, dlib_rect).parts()
    landmarks = np.array([[p.x, p.y] for p in detected_landmarks])
    return landmarks


def get_features_list(landmarks):
    features = gf.gex_X(landmarks)
    return features


def parse_all_data():
    #all_cords = []
    #all_features = []
    with_lbls = []

    for i in range(1, 500):
        new = []
        ac = get_list_of_cords('../all_data/img_no_{}.jpg'.format(i))
        if ac is None:
            continue
        #all_cords.append(ac)
        new = get_features_list(ac)
        new.append((i - 1) // 100)
        with_lbls.append(new)
        if (i % 10 == 0):
            print(i)
    return with_lbls


def build_dict(all_d):
    with_lbls = []


    for i in range(0, 9):
        value = all_d[i]
        value.append((i - 1) // 100)
        with_lbls.append(value)
    return with_lbls

with_labels = parse_all_data()

# for_df = build_dict(with_labels)

df = pd.DataFrame(with_labels)
df.to_csv('./features_from_al.csv')
