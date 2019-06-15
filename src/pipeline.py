import numpy as np
from get_features import GetFeatures
from get_model import get_model

gf = GetFeatures()


img = 'leo_r.jpg'
a = gf.get_features(img)


filename = 'finalized_model.sav'

# load the model from disk
loaded_model = get_model(filename)
result = loaded_model.predict(np.array(a).reshape(1, -1))
print(result)