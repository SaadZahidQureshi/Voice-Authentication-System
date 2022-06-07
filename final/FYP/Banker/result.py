import os
import pickle
import numpy as np
from scipy.io.wavfile import read
from featureextraction import extract_features
# from speakerfeatures import extract_features
import warnings

warnings.filterwarnings("ignore")


# path to training data
source = "SampleData/"

# path where training speakers will be saved
modelpath = "models/"

gmm_files = [os.path.join(modelpath, fname) for fname in
             os.listdir(modelpath) if fname.endswith('.gmm')]

# Load the Gaussian  Models
models = [pickle.load(open(fname, 'rb')) for fname in gmm_files]
speakers = [fname.split("/")[-1].split(".gmm")[0] for fname
            in gmm_files]

error = 0
total_sample = 0.0
acc = 0.0
print("Do you want to Test a Single Audio: Press '1' or The complete Test Audio Sample: Press '0' ?")
take = int(input().strip())
if take == 1:
    print("Enter the File name from Test Audio Sample Collection :")
    path = input().strip()
    user_model = input("Enter user name:")
    print("Testing Audio : ", path)
    sr, audio = read(source + path)
    vector = extract_features(audio, sr)

    log_likelihood = np.zeros(len(models))
    print(log_likelihood)

    i =speakers.index(user_model)
    print(user_model," -> ",i)
    #for i in range(len(models)):
    gmm = models[i]  # checking with each model one by one
    scores = np.array(gmm.score(vector))
    log_likelihood[i] = scores.sum()
    pos_log = log_likelihood*(-1)
    winner = np.argmax(pos_log)
    result=pos_log[winner]

    for x in range(len(models)):
        gmmall = models[x]  # checking with each model one by one
        scores = np.array(gmmall.score(vector))
        log_likelihood[x] = scores.sum()

    r = np.argmax(log_likelihood)
    print("result ",result)
    print("r : ",log_likelihood[r])
    if result <= 30.0 or result==-(log_likelihood[r]) :
        print(result)
        print(winner)
        print("\tdetected as - ", speakers[winner])
    else:
        print(result)
        print("Unknown User")


elif take == 0:
    test_file = "testSamplePath.txt"
    file_paths = open(test_file, 'r')

    # Read the test directory and get the list of test audio files
    for path in file_paths:

        total_sample += 1.0
        path = path.strip()
        print("Testing Audio : ", path)
        sr, audio = read(source + path)
        vector = extract_features(audio, sr)

        log_likelihood = np.zeros(len(models))

        for i in range(len(models)):
            gmm = models[i]  # checking with each model one by one
            scores = np.array(gmm.score(vector))
            log_likelihood[i] = scores.sum()

        winner = np.argmax(log_likelihood)
        print("\tdetected as - ", speakers[winner])

        checker_name = path.split("_")[0]
        if speakers[winner] != checker_name:
            error += 1
