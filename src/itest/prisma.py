import pandas as pd
import os
import streamlit


class __LogV():

    def __init__(self, repo):
        self.repo = repo

    def read_data(self):
        logs = os.path.join(os.getcwd(), "log", "logs.log")
        file = open(logs, "r")

        document = []
        for i in file.readlines():
            i = i[:-2]
            i = i[1:]
            document.append(i)

        self.document = document

    def create_dataframe(self):

        timestamp = []

        for line in range(len(self.document)):
            timestamp.append(self.document[line][1:24])
            self.document[line] = self.document[line][26:]
            continue

        doc = []
        for i in self.document:
            doc.append(i.strip().split(":"))

        self.df = pd.concat(objs=[pd.DataFrame(timestamp, columns=["Time Stamp"]),
                                  pd.DataFrame(doc, columns=["Level", "Module", "Message"])], axis=1)

    def create_streamlit(self):

        streamlit.dataframe(self.df, height=500, width=1000)


def read_logs(repo):
    obj = __LogV(repo)
    obj.read_data()
    obj.create_dataframe()
    obj.create_streamlit()

