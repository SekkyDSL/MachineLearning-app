from sklearn import svm
from sklearn import datasets
import pickle


def main():
    # classifier
    clf = svm.SVC()
    # data(iris)
    iris = datasets.load_iris()
    # Split train_x, train_y
    X, y = iris.data, iris.target
    # train
    clf.fit(X, y)
    # save model
    with open('recruit-back/trained-model/model.pkl', 'wb') as f:
        pickle.dump(clf, f)


if __name__ == '__main__':
    main()
