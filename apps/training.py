import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.preprocessing.image import img_to_array
from keras.utils import np_utils
from lenet.nn.conv import LeNet  # local file
from imutils import paths
import imutils
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2
import os

from contextlib import redirect_stdout
import io

# Page 1: Training the model
# - show the training data
# - show the testing data
# - show the model performance

# lenet: convolutional neural network
# https://pyimagesearch.com/2016/08/01/lenet-convolutional-neural-network-in-python/
# spinner, progress, balloons

def app():
    st.title('Training the Model')
    if st.button('Train Model'):
        with st.spinner('This could take about 5 minutes'):
            training_model()
        st.balloons()


def training_model():
    args = {}
    args['dataset'] = './SMILEs'
    args['model'] = './model3.h5'

    # initialize the list of data and labels
    data = []
    labels = []

    # loop over the input images
    for imagePath in sorted(list(paths.list_images(args['dataset']))):
        # load the image, pre-process it, and store in the data list
        image = cv2.imread(imagePath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = imutils.resize(image, width=28) # 28 x 28 x 1
        image = img_to_array(image)
        data.append(image)

        # extract the class label from the image path and update the labels list
        label = imagePath.split(os.path.sep)[-3]
        label = 'smiling' if label == 'positives' else 'not_smiling'
        labels.append(label)

    # scale the raw pixel intensities to the range [0, 1]
    data = np.array(data, dtype='float') / 255.0 # 0 to 255
    labels = np.array(labels)

    # convert the labels from integers to vectors
    le = LabelEncoder().fit(labels)
    labels = np_utils.to_categorical(le.transform(labels), 2)

    # account for skew in the labeled data
    classTotals = labels.sum(axis=0)
    classWeight = dict()

    for i in range(0, len(classTotals)):
        classWeight[i] = classTotals.max() / classTotals[i]

    # partition the data into training and testing sploits using 80% of
    # the data for training and the remaining 20% for testing
    (trainX, testX, trainY, testY) = train_test_split(data, labels,
                                                      test_size=0.20,
                                                      stratify=labels,
                                                      random_state=42)

    # initialize the model
    print('[INFO] compiling model...')
    model = LeNet.build(width=28, height=28, depth=1, classes=2)
    model.compile(loss=['binary_crossentropy'], optimizer='adam', metrics=['accuracy'])

    # train the network
    print('[INFO] training network...')
    H = model.fit(trainX, trainY, validation_data=(testX, testY),
                  class_weight=classWeight, batch_size=64, epochs=15, verbose=1)

    # evaluate the network
    print('[INFO] evaluating network...')
    predictions = model.predict(testX, batch_size=64)
    print(classification_report(testY.argmax(axis=1),
                                predictions.argmax(axis=1),
                                target_names=le.classes_))

    # save the model to disk
    print('[INFO] serializing network')
    model.save(args['model'])

    fig, ax = plt.subplots()
    
    ax.plot(np.arange(0, 15), H.history['loss'], label='train_loss')
    ax.plot(np.arange(0, 15), H.history['val_loss'], label='val_loss')
    ax.plot(np.arange(0, 15), H.history['accuracy'], label='accuracy')
    ax.plot(np.arange(0, 15), H.history['val_accuracy'], label='val_accuracy')
    ax.set_title('Training Loss and Accuracy')
    ax.set_xlabel('Epoch #')
    ax.set_ylabel('Loss/Accuracy')
    ax.legend()
    st.write(fig)
