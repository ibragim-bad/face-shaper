from math import sqrt
from math import atan
import face_alignment
from skimage import io
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


class GetFeatures():

    def __init__(self):
        self.fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, flip_input=False, device='cpu')

    def norm(a):
        return (sqrt(a[0] * a[0] + a[1] * a[1]))

    def f_i(self, preds, i):
        if (i == 1):
            return (self.norm(preds[0][8] - (preds[0][20] + preds[0][21]) / 2) / self.norm(preds[0][0] - preds[0][16]))
        elif (i == 2):
            return (self.norm(preds[0][4] - preds[0][12]) / self.norm(preds[0][0] - preds[0][16]))
        elif (i == 3):
            return (self.norm(preds[0][8] - preds[0][18]) / self.norm(preds[0][4] - preds[0][12]))
        elif (4 <= i <= 11):
            return (atan(abs(preds[0][i - 3 - 1][1] - preds[0][8][1]) / abs(preds[0][i - 3 - 1][0] - preds[0][8][0])))
        elif (12 <= i <= 19):
            return (atan(abs(preds[0][i - 2 - 1][1] - preds[0][8][1]) / abs(preds[0][i - 2 - 1][0] - preds[0][8][0])))

    def gex_X(self, preds):
        res = []
        for i in range(1, 20):
            res.append(self.f_i(preds, i))
        return (res)

    def get_features(self, image):
        inp = io.imread(image)
        preds = self.fa.get_landmarks(inp)
        features = self.gex_X(preds)
        return features










