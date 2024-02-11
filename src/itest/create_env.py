import os
from pathlib import Path


class __noops():
    # '''

    #     Inspired by React
    #     This app can be used to build an end to end Data Science and Machine Learning App
    #     Provides an easy access to create the end to end application
    #     Helps to focus more on the Data Science and Machine Learning

    # '''

    def __init__(self, url: str, project_name: str, author_name: str, email_id: str, requirements: list = [],
                 conda=False, ):

        # '''

        #     Getting the Git Hub Url as string and Conda as boolean amd

        # '''

        self.conda = conda
        self.url = url
        self.project_name = project_name
        self.requirements = requirements
        self.author_name = author_name
        self.email_id = email_id

    def clone_github(self):

        # '''

        #     Cloning Git Hub Here
        #     And Initializing the documents

        # '''

        os.system("git clone " + self.url)
        os.chdir(self.project_name)

    def create_folders(self):  # File Creation

        list_of_files = [

            f"src/{self.project_name}/__init__.py",

            f"src/{self.project_name}/components/data_ingestion.py",
            f"src/{self.project_name}/components/data_transformation.py",
            f"src/{self.project_name}/components/model_trainer.py",
            f"src/{self.project_name}/components/model_evaluator.py",
            f"src/{self.project_name}/components/model_predictor.py",
            f"src/{self.project_name}/components/__init__.py",

            f"src/{self.project_name}/utils/__init__.py",

            f"src/{self.project_name}/config/__init__.py",

            f"src/{self.project_name}/pipeline/__init__.py",
            f"src/{self.project_name}/pipeline/data_ingestion.py",
            f"src/{self.project_name}/pipeline/data_transformation.py",
            f"src/{self.project_name}/pipeline/model_trainer.py",
            f"src/{self.project_name}/pipeline/model_evaluator.py",
            f"src/{self.project_name}/pipeline/model_predictor.py",

            f"src/{self.project_name}/app/app.py",

            f"src/{self.project_name}/entity/__init__.py",

            f"src/{self.project_name}/constants/__init__.py",

            "test.py",

            "resource/resource.txt",

            f"requirements.txt",
            f"src/{self.project_name}/config/dataingestion.yaml",
            f"src/{self.project_name}/config/datatransformation.yaml",
            f"src/{self.project_name}/config/modelbuild.yaml",
            f"src/{self.project_name}/config/pipeline.yaml",
            f"src/{self.project_name}/config/modelprediction.yaml",
            f"src/{self.project_name}/config/modelevaluation.yaml",

            f"proto/proto.ipynb",
            f"templates/html/index.html",
            f"templates/html/result.html",
            f"templates/css/index.css",
            f"templates/css/result.css",
            f"log/logs.log",

            f"src/{self.project_name}/utils/",
            "setup.txt",

        ]

        try:

            for filepath in list_of_files:
                filepath = Path(filepath)
                filedir, filename = os.path.split(filepath)

                if filedir != "":
                    os.makedirs(filedir, exist_ok=True)

                if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
                    with open(filepath, 'w') as f:
                        pass  # creating an empty file only

                else:
                    pass
        except Exception as e:
            pass
            # st.warning(str(e))

    def write_files(self):  # Write Files

        setup_code = ['import setuptools',
                      '\n',
                      '\n',
                      '__version__ = "0.0.0"',
                      '\n',
                      f'REPO_NAME = "{self.project_name}"',
                      '\n',
                      f'AUTHOR_USER_NAME = "{self.author_name}"',
                      '\n',

                      f'SRC_REPO = "{self.project_name}"',
                      '\n',
                      f'AUTHOR_EMAIL = "{self.email_id}"',
                      '\n', '\n',
                      'setuptools.setup(',
                      '\n',
                      f'    name="{self.project_name}",',
                      '\n',
                      '    version=__version__,',
                      '\n',
                      f'    author="{self.author_name}",',
                      '\n',
                      f'    author_email="{self.email_id}",',
                      '\n',
                      '    description="nops performed",',
                      '\n',
                      f'    url="{self.url}",',
                      '\n',
                      '    project_urls={',
                      '\n',
                      f'        "Bug Tracker": "{self.url}" + "/issues",',
                      '\n', '    },',
                      '\n',
                      '    package_dir={"": "src"},',
                      '\n',
                      '    packages=setuptools.find_packages(where="src")',
                      '\n',
                      ')',
                      '\n']

        data_ingestion_code = ['from noops.utils.logger import get_logger', '\n',
                               'from noops.utils.yaml import handle_yaml', '\n',
                               'from dataclasses import dataclass', '\n',
                               'import os', '\n', "\n", "\n",

                               'logger=get_logger()', '\n',
                               'yaml_handler=handle_yaml()', '\n', "\n", "\n",

                               '@dataclass', '\n',
                               'class DataIngestionConfig():', '\n', "\n"

                                                                     '    config=yaml_handler.read_data(', '\n',
                               '        os.path.join(', '\n',
                               '            os.getcwd(),', '\n',
                               f'            "src","{self.project_name}",', '\n',
                               '            "config","dataingestion.yaml"', '\n',
                               '            )', '\n',
                               '        )', '\n', "\n", "\n",

                               'class DataIngestion():', '\n', "\n",

                               '    def __init__(self) -> None:', '\n',
                               '        self.config=DataIngestionConfig().config', '\n']

        data_transformation_code = ['from noops.utils.logger import get_logger', '\n',
                                    'from noops.utils.yaml import handle_yaml', '\n',
                                    'from dataclasses import dataclass', '\n',
                                    'import os', '\n', "\n", "\n",

                                    'logger=get_logger()', '\n',
                                    'yaml_handler=handle_yaml()', '\n', "\n", "\n",

                                    '@dataclass', '\n',
                                    'class DataTransformationConfig():', '\n', "\n",

                                    '    config=yaml_handler.read_data(', '\n',
                                    '        os.path.join(', '\n',
                                    '            os.getcwd(),', '\n',
                                    f'            "src","{self.project_name}",', '\n',
                                    '            "config","datatransformation.yaml"', '\n',
                                    '            )', '\n',
                                    '        )', '\n', "\n", "\n",

                                    'class DataTranformation():', '\n', "\n",

                                    '    def __init__(self) -> None:', '\n',
                                    '        self.config=DataTransformationConfig().config', '\n']

        model_evaluator_code = ['from noops.utils.logger import get_logger', '\n',
                                'from noops.utils.yaml import handle_yaml', '\n',
                                'from dataclasses import dataclass', '\n',
                                'import os', '\n', "\n", "\n",

                                'logger=get_logger()', '\n',
                                'yaml_handler=handle_yaml()', '\n', "\n", "\n",

                                '@dataclass', '\n',
                                'class ModelEvaluatorConfig():', '\n', "\n",

                                '    config=yaml_handler.read_data(', '\n',
                                '        os.path.join(', '\n',
                                '            os.getcwd(),', '\n',
                                f'            "src","{self.project_name}",', '\n',
                                '            "config","modelevaluation.yaml"', '\n',
                                '            )', '\n',
                                '        )', '\n', "\n", "\n",

                                'class ModelEvaluator():', '\n', "\n",

                                '    def __init__(self) -> None:', '\n',
                                '        self.config=ModelEvaluatorConfig().config', '\n']

        model_predictor_code = ['from noops.utils.logger import get_logger', '\n',
                                'from noops.utils.yaml import handle_yaml', '\n',
                                'from dataclasses import dataclass', '\n',
                                'import os', '\n', "\n", "\n",

                                'logger=get_logger()', '\n',
                                'yaml_handler=handle_yaml()', '\n', "\n",

                                '@dataclass', '\n',
                                'class ModelPredictorConfig():', '\n', "\n",

                                '    config=yaml_handler.read_data(', '\n',
                                '        os.path.join(', '\n',
                                '            os.getcwd(),', '\n',
                                f'            "src","{self.project_name}",', '\n',
                                '            "config","modelprediction.yaml"', '\n',
                                '            )', '\n',
                                '        )', '\n', "\n",

                                'class ModelPredictor():', '\n', "\n",

                                '    def __init__(self) -> None:', '\n',
                                '        self.config=ModelPredictorConfig().config', '\n']

        model_trainer_code = ['from noops.utils.logger import get_logger', '\n',
                              'from noops.utils.yaml import handle_yaml', '\n',
                              'from dataclasses import dataclass', '\n',
                              'import os', '\n', "\n", "\n",

                              'logger=get_logger()', '\n',
                              'yaml_handler=handle_yaml()', '\n', "\n", "\n",

                              '@dataclass', '\n',
                              'class ModelTrainerConfig():', '\n', "\n",

                              '    config=yaml_handler.read_data(', '\n',
                              '        os.path.join(', '\n',
                              '            os.getcwd(),', '\n',
                              f'            "src","{self.project_name}",', '\n',
                              '            "config","modelbuild.yaml"', '\n',
                              '            )', '\n',
                              '        )', '\n', "\n", "\n",

                              'class ModelTrainer():', '\n', "\n",

                              '    def __init__(self) -> None:', '\n',
                              '        self.config=ModelTrainerConfig().config', '\n']

        require = []
        self.requirements = self.requirements

        for i in self.requirements:
            require.append(i)
            require.append('\n')
        require.append('-e .')

        with open("requirements.txt", "w") as f:
            f.writelines(require)

        with open("setup.txt", "w") as f:
            f.writelines(setup_code)

        with open(f"src/{self.project_name}/components/data_ingestion.py", "w") as f:
            f.writelines(data_ingestion_code)

        with open(f"src/{self.project_name}/components/data_transformation.py", "w") as f:
            f.writelines(data_transformation_code)

        with open(f"src/{self.project_name}/components/model_trainer.py", "w") as f:
            f.writelines(model_trainer_code)

        with open(f"src/{self.project_name}/components/model_evaluator.py", "w") as f:
            f.writelines(model_evaluator_code)

        with open(f"src/{self.project_name}/components/model_predictor.py", "w") as f:
            f.writelines(model_predictor_code)

        try:

            os.rename("setup.txt", "setup.py")

        except Exception as e:
            pass
            # st.warning(str(e))

    def conda_env(self):

        if self.conda == True:

            try:
                os.system("conda create -p environment -y")

            except Exception as e:
                pass
                # st.warning(str(e))


def create_app(url, requirements, project_name, conda, author_name, email_id):  # Create App

    obj = __noops(url=url, project_name=project_name,
                  requirements=requirements, conda=conda, author_name=author_name, email_id=email_id)

    obj.clone_github()
    obj.conda_env()
    obj.create_folders()
    obj.write_files()


create_app(
    "https://github.com/Musician9dx/musician",
    "scikit-learn tensorflow",
    "musician",
    True,
    "musician",
    "ragha@gmail.com"
)















