import os
import pprint

pp = pprint.PrettyPrinter(indent=4)

import pandas as pd
from ydata_profiling import ProfileReport

"""


df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)

"""


class __MLFlowSummarizer():

    def __init__(self):

        self.cwd = os.path.join(os.getcwd(), "mlruns", "0")

        self.mllogs = {}

    def list_all_mlversions(self):

        directory = os.listdir(self.cwd)

        self.versions = directory.copy()
        self.versions.pop(-1)

        for file in range(len(directory)):
            directory[file] = os.path.join(self.cwd, directory[file])

        directory.pop(-1)

        self.directory = directory

        return self.versions

    def branch(self):

        self.metrics_dir = self.directory.copy()
        self.params_dir = self.directory.copy()

        for file in range(len(self.metrics_dir)):
            self.metrics_dir[file] = os.path.join(self.cwd, self.metrics_dir[file], "metrics")

        for file in range(len(self.params_dir)):
            self.params_dir[file] = os.path.join(self.cwd, self.params_dir[file], "params")

    def read_params(self):

        param_summary = {}

        cnt = 0

        for i in self.params_dir:

            param_dir = os.listdir(i)

            li = {}
            for j in param_dir:
                file_name = os.path.join(i, j)

                file = open(file_name, "r")
                k = file.read()

                li[j] = int(k)

            param_summary[self.versions[cnt]] = li
            cnt = cnt + 1

            params = {"Parameters": param_summary}

        return params

    def read_metrics(self):

        metric_summary = {}

        cnt = 0

        for i in self.metrics_dir:

            param_dir = os.listdir(i)

            li = {}
            for j in param_dir:
                file_name = os.path.join(i, j)

                file = open(file_name, "r")
                k = file.read()

                li[j] = int(k)

            metric_summary[self.versions[cnt]] = li
            cnt = cnt + 1

            metrics = {"Metrics": metric_summary}

        return metrics

    def create_profile(self, metrics, params):

        summary = []

        for key in params["Parameters"].keys():
            metricDict = metrics["Metrics"][key]
            paramDict = params["Parameters"][key]
            metricDict.update(paramDict)

            metricDict["Model ID"] = key

            summary.append(metricDict)

        DataFrame = pd.DataFrame.from_dict(summary)

        profileReport = ProfileReport(DataFrame)

        return (profileReport,DataFrame)


def Summarize_MLFlow():
    obj = __MLFlowSummarizer()

    versions = obj.list_all_mlversions()

    obj.branch()

    params = obj.read_params()

    metrics = obj.read_metrics()

    profile,DataFrame = obj.create_profile(metrics, params)

    return (
        versions,
        params,
        metrics,
        profile,
        DataFrame
    )


Summarize_MLFlow()






