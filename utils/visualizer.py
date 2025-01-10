import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix
    

def logger(epochs, train_losses, train_accuracies):
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Loss', color='tab:red')
    ax1.plot(epochs, train_losses, color='tab:red')
    ax1.tick_params(axis='y', labelcolor='tab:red')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Accuracy', color='tab:blue')
    ax2.plot(epochs, train_accuracies, color='tab:blue')
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    plt.title('Loss and Accuracy')
    plt.savefig("./workspace/training_log/loss_and_accuray.png")


def mk_confusion_matrix(class_names, all_labels, all_preds):

    cm = confusion_matrix(all_labels, all_preds)

    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('MNIST')
    plt.savefig("./workspace/eval/mnist_confusion_matrix.png")
    plt.show()
