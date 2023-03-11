from numpy import logical_and, sum as t_sum
import numpy as np
import os
import shutil
import urllib
import subprocess
from typing import List


def accuracy(predicted_labels, true_labels):
    """
    Accuracy is correct predictions / all predicitons
    """
    correct_count = 0
    for pred, label in zip(predicted_labels, true_labels):
        correct_count += int(pred == label)

    return correct_count/len(true_labels) if len(true_labels) > 0 else 0.


def precision(predicted_labels, true_labels, which_label=1):
    """
    Precision is True Positives / All Positives Predictions
    """
    pred_which = np.array([pred == which_label for pred in predicted_labels])
    true_which = np.array([lab == which_label for lab in true_labels])
    denominator = t_sum(pred_which)
    if denominator:
        return t_sum(logical_and(pred_which, true_which))/denominator
    else:
        return 0.


def recall(predicted_labels, true_labels, which_label=1):
    """
    Recall is True Positives / All Positive Labels
    """
    pred_which = np.array([pred == which_label for pred in predicted_labels])
    true_which = np.array([lab == which_label for lab in true_labels])
    denominator = t_sum(true_which)
    if denominator:
        return t_sum(logical_and(pred_which, true_which))/denominator
    else:
        return 0.


def f1_score(predicted_labels, true_labels, which_label=1):
    """
    F1 score is the harmonic mean of precision and recall
    """
    P = precision(predicted_labels, true_labels, which_label=which_label)
    R = recall(predicted_labels, true_labels, which_label=which_label)
    if P and R:
        return 2*P*R/(P+R)
    else:
        return 0.


def avg_f1_score(predicted_labels: List[int], true_labels: List[int], classes: List[int]):
    """
    Calculate the f1-score for each class and return the average of it

    :return: float
    """
    result = 0.0
    for i in range(len(classes)):
        result += f1_score(predicted_labels, true_labels, classes[i])
    return result/len(classes)

def download_zip(url: str, dir_path: str):
    import zipfile
    if url.endswith('zip'):
        print('Downloading dataset file')
        path_to_zip_file = 'downloaded_file.zip'
        # Download the dataset zipped file
        urllib.request.urlretrieve(url, path_to_zip_file)
        # Unzip the dataset
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall('./')
        # Delete any existing sem eval folder
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
        # Remove zip file
        if os.path.exists(path_to_zip_file):
            os.remove(path_to_zip_file)
        # Rename sem eval folder name
        if os.path.exists(dir_path + '-master'):
            shutil.move(dir_path + '-master', dir_path)
        elif os.path.exists(dir_path + '-main'):
            shutil.move(dir_path + '-main', dir_path)
    print(f'Downloaded dataset to {dir_path}')


def git(*args):
    return subprocess.check_call(['git'] + list(args))
