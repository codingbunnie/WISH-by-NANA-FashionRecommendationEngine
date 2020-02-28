from sklearn.neighbors import NearestNeighbors
import cv2
import pickle
import tensorflow as tf

extractModel = tf.keras.models.load_model('static/extractModel.h5')

def get_neighbors(category, imagePath):

    with open('static/feature-vector/{}FV.pkl'.format(category),'rb') as f:
        featureVector = pickle.load(f)

    # with open('static/knn/{}KNN.pkl'.format(category),'rb') as f:
    #     neigh = pickle.load(f)

    X = featureVector.reshape((len(featureVector),-1)) 

    neigh = NearestNeighbors(n_neighbors = len(featureVector))

    neigh.fit(X)

    image = cv2.imread('static/' + imagePath)
    image = tf.image.resize(image, [299, 299])
    image = image.numpy().reshape((1,299,299,3))
    image = image/255.0

    return neigh.kneighbors(extractModel.predict(image))
