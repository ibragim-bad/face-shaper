import pickle

def get_model(filename):
    model = pickle.load(open(filename, 'rb'))
    return model