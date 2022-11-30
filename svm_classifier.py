import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

def configure_axes(ax, x0, x1, title, **params):
    ax.scatter(x0, x1, **params)
    # ax.set_ylabel('y label here')
    # ax.set_xlabel('x label here')
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title(title)
    # ax.legend()

def run_svm(x, y, title):
  model = SVC(kernel='linear')
  clf = model.fit(x, y)

  fig, ax = plt.subplots()
  # Set-up grid for plotting.
  X0, X1 = x[:, 0], x[:, 1]
  xx, yy = make_meshgrid(X0, X1)

  plot_contours(ax, clf, xx, yy, cmap=plt.cm.coolwarm, alpha=0.8)
  configure_axes(ax, X0, X1, title, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
  plt.show()