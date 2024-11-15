import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score


def extract_features(file_path):
    audio, _ = librosa.load(file_path, sr=None)

    zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(audio))
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=audio))
    spectral_rolloff = np.mean(librosa.feature.spectral_rolloff(y=audio))
    mfccs = np.mean(librosa.feature.mfcc(y=audio, n_mfcc=13))
    rms = np.mean(librosa.feature.rms(y=audio))
    #spectral_contrast = np.mean(librosa.feature.spectral_contrast(y=audio))
    energy = np.mean(librosa.feature.rms(y=audio)**2)  

    
    return [zero_crossing_rate, spectral_centroid, spectral_rolloff, mfccs, rms,energy]

class1_train_dir = "C:/Users/praba/OneDrive/Desktop/Autum 2023/Audio Processing/Data/Training data/Tram"  # Class 1 training data 
class1_test_dir = "C:/Users/praba/OneDrive/Desktop/Autum 2023/Audio Processing/Data/Tesing Data/Tram"     # Class 1 testing data 

class2_train_dir = "C:/Users/praba/OneDrive/Desktop/Autum 2023/Audio Processing/Data/Training data/Bus"   # Class 2 training data 
class2_test_dir = "C:/Users/praba/OneDrive/Desktop/Autum 2023/Audio Processing/Data/Tesing Data/Bus"      # Class 2 testing data 

def process_class_data(train_dir, test_dir, label):
    features = []
    labels = []

    # Extract features for training
    for filename in os.listdir(train_dir):
        if filename.endswith(".wav"):
            file_path = os.path.join(train_dir, filename)
            feature_vector = extract_features(file_path)
            features.append(feature_vector)
            labels.append(label)

    # Extract features for testing
    for filename in os.listdir(test_dir):
        if filename.endswith(".wav"):
            file_path = os.path.join(test_dir, filename)
            feature_vector = extract_features(file_path)
            features.append(feature_vector)
            labels.append(label)

    return features, labels

class1_train_features, class1_train_labels = process_class_data(class1_train_dir, class1_test_dir, 0)
class2_train_features, class2_train_labels = process_class_data(class2_train_dir, class2_test_dir, 1)

# Combine features and labels for training
features = class1_train_features + class2_train_features
labels = class1_train_labels + class2_train_labels

# Split the data into training and validation
X_train, X_temp, y_train, y_temp = train_test_split(features, labels, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.3, random_state=42)

# Standardize the feature vectors
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# Train the SVM model
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)

# Train the Logistic Regression model
lr_model = LogisticRegression(random_state=42)
lr_model.fit(X_train, y_train)

class1_features, _ = process_class_data(class1_train_dir, class1_test_dir, 0)
class2_features, _ = process_class_data(class2_train_dir, class2_test_dir, 1)

class1_features = np.array(class1_features)
class2_features = np.array(class2_features)

# Predict on the validation set
svm_val_predictions = svm_model.predict(X_val)
lr_val_predictions = lr_model.predict(X_val)

# Evaluate the models on the validation set
svm_val_accuracy = accuracy_score(y_val, svm_val_predictions)
svm_val_precision = precision_score(y_val, svm_val_predictions)
svm_val_recall = recall_score(y_val, svm_val_predictions)

lr_val_accuracy = accuracy_score(y_val, lr_val_predictions)
lr_val_precision = precision_score(y_val, lr_val_predictions)
lr_val_recall = recall_score(y_val, lr_val_predictions)

# Print validation results
print("SVM Model Validation Accuracy:", svm_val_accuracy)
print("SVM Model Validation Precision:", svm_val_precision)
print("SVM Model Validation Recall:", svm_val_recall)

print("Logistic Regression Model Validation Accuracy:", lr_val_accuracy)
print("Logistic Regression Model Validation Precision:", lr_val_precision)
print("Logistic Regression Model Validation Recall:", lr_val_recall)

# Predict on the test set
svm_test_predictions = svm_model.predict(X_test)
lr_test_predictions = lr_model.predict(X_test)

# Evaluate the models on the test set
svm_test_accuracy = accuracy_score(y_test, svm_test_predictions)
svm_test_precision = precision_score(y_test, svm_test_predictions)
svm_test_recall = recall_score(y_test, svm_test_predictions)

lr_test_accuracy = accuracy_score(y_test, lr_test_predictions)
lr_test_precision = precision_score(y_test, lr_test_predictions)
lr_test_recall = recall_score(y_test, lr_test_predictions)

# Print test results
print("SVM Model Test Accuracy:", svm_test_accuracy)
print("SVM Model Test Precision:", svm_test_precision)
print("SVM Model Test Recall:", svm_test_recall)

print("Logistic Regression Model Test Accuracy:", lr_test_accuracy)
print("Logistic Regression Model Test Precision:", lr_test_precision)
print("Logistic Regression Model Test Recall:", lr_test_recall)


feature_names = ['Zero Crossing Rate', 'Spectral Centroid', 'Spectral Rolloff', 'MFCCs', 'RMS', 'Energy']

for i in range(class1_features.shape[1]):
    plt.figure(figsize=(10, 5))
    plt.hist(class1_features[:, i], bins=50, alpha=0.5, label='Class 1', color='blue')
    plt.hist(class2_features[:, i], bins=50, alpha=0.5, label='Class 2', color='orange')
    plt.title(f'Histogram of {feature_names[i]}')
    plt.xlabel(feature_names[i])
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()