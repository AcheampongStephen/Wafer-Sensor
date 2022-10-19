# WAFER


### PROBLEM STATEMENT
 <p>The inputs of various sensors for different wafers have been provided. In electronics, a wafer (also called a slice or substrate) is a thin slice of semiconductor used for the fabrication of integrated circuits.</p>

<p>The goal is to build a machine learning model which predicts whether a wafer needs to be replaced or not(i.e., whether it is working or not) based on the inputs from various sensors. There are two classes: +1 and -1.</p>
<br>

### PROJECT STRUCTURE
<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

```
1. Create a virtual environment : conda create -n wafer3 python=3.7 -y  Activate: conda activate wafer3
```

```
2. pip install cookiecutter
```

```
3. cookiecutter https://github.com/drivendata/cookiecutter-data-science
```





### PROJECT ORGAINIZATION
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
<br>

##### <b>INITIALIZE GIT IN CURRENT WORKING DIRECTORY</b>
```
git init
```
##### <b>INITIALIZE DVC</b>
```
1. pip install dvc
```
```
2. dvc init
```
##### <b>COMMIT AND PUSH TO THE REMOTE REPOSITORY</b>
```
1. git add . && git commit -m "first commit"
2. git branch -M main
3. git remote add origin https://github.com/AcheampongStephen/Wafer.git
4. git push -u origin main
```
##### <b>CREATE AND CHECKOUT A DEVELOPMENT BRANCH</b>
```
git checkout -b dev
```
##### <b>ADDING DATA TO DVC FOR TRACKING</b>
```
dvc add Training_Batch_Files/*.csv Prediction_Batch_files/*.csv
```
##### <b>INSTALL DVC FOR GDRIVE</b>
```
pip install dvc[gdrive]
```
##### <b>ADD REMOTE STORAGE</b>
```
dvc remote add -d storage gdrive://<DRIVE ID>

git add .dvc/config && git commit -m "Configure remote storage"
```
##### <b>PUSH THE DATA TO REMOTE</b>
```
dvc push
```
##### <b>ADD GDRIVE CREDENTIAL TO REPO SECRET</b>
##### <b>INSTALL PACKAGES IN REQUIREMENTS.TXT</b>
```
pip install -r requirements.txt
```
##### <b>CREATE A PIPELINE PATH FOR DATA PREPARATION IN SRC DIRECTORY AND IMPORT LIBRARIES</b>
```
touch src/pipeline_o1_data_preparation.py
```
##### <b>CREATE CONFIG DIRECTORY</b>
```
1. mkdir config
2. In config directory, create params.yaml file.
3. Create config/schema_training.json in config directory.
4. Create config/schema_prediction.json in config directory. 
```