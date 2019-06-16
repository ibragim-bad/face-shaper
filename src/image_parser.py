from PIL import Image
from scipy import ndimage
from skimage import io
import dlib
from src.get_features import GetFeatures
from src.get_model import get_model
from src.preproc import *
import sys
import os
import glob

PATH = './sunglasses'

def get_img_list(gname):
    if (gname == 'heart'):
        return (os.path.join(PATH, 'w_deal.png'))
    if (gname == 'oblong'):
        return (os.path.join(PATH, 'w_deal.png'))
    if (gname == 'oval'):
        return (os.path.join(PATH, 'deal.png'))
    if (gname == 'round'):
        return (os.path.join(PATH, 'w_deal.png'))
    if (gname == 'square'):
        return (os.path.join(PATH, 'w_deal.png'))


# def get_img_list(gname):
#     if (gname == 'heart'):
#         return (os.path.join(PATH, 'wayfarer.png'))
#     if (gname == 'oblong'):
#         return (os.path.join(PATH, 'clubmaster.png'))
#     if (gname == 'oval'):
#         return (os.path.join(PATH, 'round.png'))
#     if (gname == 'round'):
#         return (os.path.join(PATH, 'wayfarer.png'))
#     if (gname == 'square'):
#         return (os.path.join(PATH, 'aviator.png'))



PATH_DIR_GLASS = './'

class ImageDealer():
    def __init__(self):
        self.gf = GetFeatures()
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("../models/shape_predictor_68_face_landmarks.dat")
        self.model_path = '../models/finalized_model.sav'
        self.svc = get_model(self.model_path)

    def parse_image(self, file):

        img_leo = cv2.imread(file)
        img = resize(img_leo, 700)
        img_io = resize(io.imread(file), 700)

        img_copy = img_io.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # etect faces
        dets = self.detector(gray, 1)
        if len(dets) == 0:
            sys.exit('doesn`t find face((')
        # find face box bounding points
        for d in dets:
            x = d.left()
            y = d.top()
            w = d.right()
            h = d.bottom()

        dlib_rect = dlib.rectangle(x, y, w, h)

        detected_landmarks = self.predictor(gray, dlib_rect).parts()

        landmarks = np.array([[p.x, p.y] for p in detected_landmarks])

        for idx, point in enumerate(landmarks):
            pos = (point[0], point[1])
            if idx == 0:
                eye_left = pos
            elif idx == 16:
                eye_right = pos

            try:
                # cv2.line(img_copy, eye_left, eye_right, color=(0, 255, 255))
                degree = np.rad2deg(np.arctan2(eye_left[0] - eye_right[0], eye_left[1] - eye_right[1]))

            except:
                pass

        landmarks = np.array([[p.x, p.y] for p in detected_landmarks])

        features = np.array(self.gf.gex_X(landmarks))

        result = self.svc.predict(features.reshape(1, -1))[0]

        eye_center = (eye_left[1] + eye_right[1]) / 2

        # Sunglasses translation
        glass_trans = int(.2 * (eye_center - y))

        # Funny tanslation
        # glass_trans = int(-.3 * (eye_center - y ))

        # Mask translation
        # glass_trans = int(-.8 * (eye_center - y))

        # resize glasses to width of face and blend images
        face_width = w - x
        shapes = ['heart', 'oblong', 'oval', 'round', 'square']
        # glasses_files = [['deal.png'],['deal.png'],['deal.png'],
        #                  ['deal.png'],['deal.png']]
        # glasses_dict = dict(zip(shapes, glasses_files))
        # resize_glasses


        shape_result = shapes[result]
        glass_files = get_img_list(shape_result)
        path_dir = PATH_DIR_GLASS
        #path = os.path.join(path_dir, glasses_dict[shape_result][0])
        glasses = cv2.imread(glass_files, -1)
        glasses_resize = resize(glasses, face_width)

        # Rotate glasses based on angle between eyes
        yG, xG, cG = glasses_resize.shape
        glasses_resize_rotated = ndimage.rotate(glasses_resize, (degree + 90))
        glass_rec_rotated = ndimage.rotate(img[y + glass_trans:y + yG + glass_trans, x:w], (degree + 90))

        # blending with rotation
        h5, w5, s5 = glass_rec_rotated.shape
        rec_resize = img_copy[y + glass_trans:y + h5 + glass_trans, x:x + w5]
        blend_glass3 = blend_transparent(rec_resize, glasses_resize_rotated)
        img_copy[y + glass_trans:y + h5 + glass_trans, x:x + w5] = blend_glass3

        ioi = Image.fromarray(img_copy, 'RGB')
        ioi.save('result-{}'.format(file))
        return shape_result
