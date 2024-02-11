import streamlit as st
from streamlit_pandas_profiling import st_profile_report
import os

from itest.create_env import create_app
from itest.prisma import read_logs
from itest.handlers import handle_yaml
from itest.mlflow import Summarize_MLFlow
import time

yamlhandler = handle_yaml()

st.title("Retro & Mylo")
st.caption("Itest")
# Intro


app, logs, git, mllogs, yaml, timc, ret = st.tabs(
    ["Creat App", "Read Logs", "Update Git", "Read ML Logs", "YAML Configuration", "Calculate Time", "Return"])

with app:
    st.subheader("Create a Retro")

    col1, col2, col3 = st.columns(3)

    with st.container():
        requirements = list(map(str, str((st.text_input("Enter your Requirements"))).split()))

    with st.container():
        with col1:

            url = str(st.text_input("URL"))

            repo = str(st.text_input("Enter Repo Name"))
            conda = str(st.selectbox("Need Conda?", ["YES", "NO"]))

            if conda == "YES":
                conda = True
            else:
                conda = False
    with st.container():
        with col2:
            author_name = str(st.text_input("Author Name"))

            email_id = str(st.text_input("Email ID"))

            st.subheader("A 9DX PROJEXT")

    if st.button("Create App"):
        create_app(url=url, project_name=repo, conda=conda, author_name=author_name, email_id=email_id,
                   requirements=requirements)
        os.system("cd " + os.path.join(os.getcwd(), repo))

        st.balloons()  # Initialize App

with logs:
    st.caption("Logs")  # Log Reader

    if st.button("Update Logs:"):
        read_logs(repo)

with git:
    st.subheader("Git Update")  # Git Update

    log = st.text_input("Commit")
    if st.button("Update Git"):

        try:
            os.system("git add .")
            os.system("git commit -m " + log)
            os.system("git push")
        except Exception as e:
            st.warning(str(e))

with mllogs:
    st.subheader("Summarize ML Logs")

    if st.button("Read Logs:"):  # Summarize ML Models

        Versions, Parameters, Metrics, Profile,DataFrame = Summarize_MLFlow()

        Ver, Par, Met, Prof = st.tabs(["Model Versions", "Model Parameters", "Model Metrics", "Profile Report"])

        with Ver:
            st.caption("Model Versions")
            st.write(Versions)

        with Par:
            st.caption("Model Parameters")
            st.json(Parameters)

        with Met:
            st.caption("Model Metrics")
            st.json(Metrics)

        with Prof:

            st_profile_report(Profile)

with yaml:
    dataingestion, datatransformation, modelbuild, modelpredict, modelevaluate, pipleine = st.tabs(
        ["Data Ingestion", "Data Transformation", "Model Build", "Model Predict", "Model Evaluate", "Pipeline"])

    with dataingestion:

        DataIngestionYaml = os.path.join(os.getcwd(), "src", f"{repo}", "config",
                                         "dataingestion.yaml")  # Configuraion File Handlers

        # Data Ingestion YAML

        st.header("Append Configuration")
        key1 = st.text_input("Enter Key for Data Ingestiontion")
        val1 = st.text_input("Enter Value for Data Ingestion")

        if st.button("Add to Data Ingestion YAML"):
            yamlhandler.add_data(DataIngestionYaml, key=key1, val=val1)

        st.header("Read Configuration")
        if st.button("Read from Data Ingestiontion YAML"):
            yamlhandler.read_data(DataIngestionYaml)

    with datatransformation:
        # Data Transformation YAML
        DataTransformationYaml = os.path.join(os.getcwd(), "src", f"{repo}", "config", "datatransformation.yaml")

        st.header("Append Configuration")
        key2 = st.text_input("Enter Key for Data Transformation")
        val2 = st.text_input("Enter Value for Data Transformation")

        if st.button("Add to Data Transformation YAML"):
            yamlhandler.add_data(DataTransformationYaml, key=key2, val=val2)

        st.header("Read Configuration")
        if st.button("Read from Data Transformation YAML"):
            yamlhandler.read_data(DataTransformationYaml)

    with modelbuild:

        # Model Building YAML
        ModelBuildYaml = os.path.join(os.getcwd(), "src", f"{repo}", "config", "modelbuild.yaml")

        st.header("Append Configuration")
        key2 = st.text_input("Enter Key for Model Builder")
        val2 = st.text_input("Enter Value for Model Builder")

        if st.button("Add to Model Builder YAML"):
            yamlhandler.add_data(ModelBuildYaml, key=key2, val=val2)

        st.header("Read Configuration")
        if st.button("Read from Model Build YAML"):
            yamlhandler.read_data(ModelBuildYaml)

    with modelevaluate:

        # Model Evaluation
        ModelEvaluationYaml = os.path.join(os.getcwd(), "src", f"{repo}", "config", "modelevaluation.yaml")

        st.header("Append Model Evaluation Configuration")
        key2 = st.text_input("Enter Key for Model Evaluator")
        val2 = st.text_input("Enter Value for Model Evaluator")

        if st.button("Add to Model Evaluation YAML"):
            yamlhandler.add_data(ModelEvaluationYaml, key=key2, val=val2)

        st.header("Read Model Evaluation Configuration")
        if st.button("Read from Model Evaluation YAML"):
            yamlhandler.read_data(ModelEvaluationYaml)

    with modelpredict:
        # Model Prediction
        ModelPredictionYaml = os.path.join(os.getcwd(), "src", f"{repo}", "config", "modelprediction.yaml")

        st.header("Append Model Model Prediction Configuration")
        key2 = st.text_input("Enter Key for Model Predictor")
        val2 = st.text_input("Enter Value for Model Predictor")

        if st.button("Add to Model Prediction YAML"):
            yamlhandler.add_data(ModelPredictionYaml, key=key2, val=val2)

        st.header("Read Model Prediction Configuration")
        if st.button("Read from Model Prediction YAML"):
            yamlhandler.read_data(ModelPredictionYaml)

    with pipleine:
        # Pipeline
        PipelineYaml = os.path.join(os.getcwd(), "src", f"{repo}", "config", "pipeline.yaml")

        st.header("Append Pipeline Configuration")
        key2 = st.text_input("Enter Key for Pipeline")
        val2 = st.text_input("Enter Value for Pipeline")

        if st.button("Add to Pipeline YAML"):
            yamlhandler.add_data(PipelineYaml, key=key2, val=val2)

        st.header("Read Pipeline Configuration")
        if st.button("Read from Pipeline YAML"):
            yamlhandler.read_data(PipelineYaml)

with timc:
    dataingestion, datatransformation, modelbuild, modelpredict, modelevaluate, pipeline = st.tabs(
        ["Data Ingestion", "Data Transformation", "Model Build", "Model Predict", "Model Evaluate", "Pipeline"])

    with dataingestion:

        if st.button("Calculate Data Ingestion Time"):
            start = time.time()
            #
            os.system("python " + os.path.join(os.getcwd(), "src", repo, "pipeline", "data_ingestion.py"))

            end = time.time()

            st.subheader(end - start)

    with datatransformation:

        if st.button("Calculate Data Transformation Time"):
            start = time.time()
            #
            os.system("python " + os.path.join(os.getcwd(), "src", repo, "pipeline", "data_transformation.py"))

            end = time.time()

            st.subheader(end - start)

    with modelevaluate:

        if st.button("Calculate Data Evaluation Time"):
            start = time.time()
            #
            os.system("python " + os.path.join(os.getcwd(), "src", repo, "pipeline", "model_evaluator.py"))

            end = time.time()

            st.subheader(end - start)

    with modelbuild:

        if st.button("Calculate Model Build Time"):
            start = time.time()
            #
            os.system("python " + os.path.join(os.getcwd(), "src", repo, "pipeline", "model_trainer.py"))

            end = time.time()

            st.subheader(end - start)

    with modelpredict:

        if st.button("Calculate Model Predict Time"):
            start = time.time()
            #
            os.system("python " + os.path.join(os.getcwd(), "src", repo, "pipeline", "model_predictor.py"))

            end = time.time()

            st.subheader(end - start)

    with pipeline:

        if st.button("Calculate The Pipeline Time"):
            start = time.time()
            os.system("python " + os.path.join(os.getcwd(), "src", repo, "pipeline", "data_ingestion.py"))
            os.system("python " + os.path.join(os.getcwd(), "src", repo, "pipeline", "data_transformation.py"))
            os.system("python " + os.path.join(os.getcwd(), "src", repo, "pipeline", "model_evaluator.py"))
            os.system("python " + os.path.join(os.getcwd(), "src", repo, "pipeline", "model_trainer.py"))
            os.system("python " + os.path.join(os.getcwd(), "src", repo, "pipeline", "model_predictor.py"))

            end = time.time()

            st.subheader(end - start)

with ret:
    path = st.text_input("Return Path")

    if st.button("Return"):
        os.chdir(f"{str(path)} ")

        st.warning(path)

        st.warning(os.getcwd())







