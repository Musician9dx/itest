from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Regression Metrics
from sklearn.metrics import explained_variance_score
from sklearn.metrics import max_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_poisson_deviance
from sklearn.metrics import mean_gamma_deviance
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.metrics import d2_absolute_error_score
from sklearn.metrics import d2_pinball_score
from sklearn.metrics import d2_tweedie_score

import pandas as pd
import numpy as np

# Classifier Metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import log_loss
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score

from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier


class TestModel():

    def __init__(self) -> None:

        self.DataFrame = False
        self.models = []

    def regression(self, models, x, y):

        df = pd.read_csv("D:/INeuron/nvech/noops/test.csv")

        x = df["x"]
        y = df["y"]

        x = np.reshape(x, (-1, 1))
        y = np.reshape(y, (-1, 1))

        models = {

            "linear": LinearRegression(),
            "random": RandomForestRegressor(),
        }

        for model in models.keys():
            dataFrame = []
            ml = models[model]

            ml.fit(x, y)

            ypred = ml.predict(x)

            metrics = {}

            metrics["Model"] = model

            metrics.update({

                "explained_variance_score": [explained_variance_score(y, ypred)],
                "max_error": [max_error(y, ypred)],
                "mean_absolute_error": [mean_absolute_error(y, ypred)],
                "mean_squared_error": [mean_squared_error(y, ypred)],
                "r2_score": [r2_score(y, ypred)],
                "median_absolute_error": [median_absolute_error(y, ypred)],

                "mean_absolute_percentage_error": [mean_absolute_percentage_error(y, ypred)],

            })

            df = pd.DataFrame.from_dict(metrics)

            self.models.append(ml)

            print(df)

    def classification(self, models):

        df = pd.read_csv("D:/INeuron/nvech/noops/train.csv")

        y = df["price_range"]

        df.drop("price_range", inplace=True, axis=1)

        x = df

        y = y.values.tolist()

        y = np.reshape(y, (-1, 1))

        for model in models.keys():
            dataFrame = []
            ml = models[model]

            ml.fit(x, y)

            ypred = ml.predict(x)

            metrics = {}

            metrics["Model"] = model

            metrics.update({

                "accuracy_score": [accuracy_score(y, ypred)],
                "f1_score": [f1_score(y, ypred, average="macro")],
                "r2_score": [r2_score(y, ypred)],
                "precision_score": [precision_score(y, ypred, average="macro")],
                "recall_score": [recall_score(y, ypred, average="macro")],

            })

            df = pd.DataFrame.from_dict(metrics)

            self.models.append(ml)

            print(df)


tester = TestModel()

models = {

    "linear": LinearRegression(),
    "random": RandomForestRegressor(),
}

models2 = {

    "Ada": AdaBoostClassifier(),
    "Random": RandomForestClassifier(),

}

tester.classification(models2)



