import yaml
import streamlit as st


class handle_yaml():

    def __init__(self) -> None:
        pass

    def add_data(self, yamlPath, key, val):
        file = open(yamlPath, "a")

        yaml.dump({key: val}, file, default_flow_style=False, allow_unicode=True, encoding=None)

        file.close()

    def read_data(self, yamlPath):
        with open(yamlPath, "r") as f:
            z = yaml.safe_load(f)
            st.json(z)

            return z



