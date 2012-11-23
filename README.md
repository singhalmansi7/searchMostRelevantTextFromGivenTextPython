searchMostRelevantTextFromGivenTextPython
=========================================

Given a text, a person can search most relevant lines out of it.

Steps to perform:

1) Install virtual env
2) Activate virtual env using commands:
    $ mkdir virtualEnvDirectory
    $ cd virtualEnvDirectory
    $ virtualenv venv
    $ source venv/bin/activate

3) Now run: pip install -r searchMostRelevantTextFromGivenTextPython/requirements.pip
4) cd sentimentAnalysisInPython/
5) Run nltkSetUpScript to install nltk in virtualEnv: ./nltkSetup.sh

6) Run the project:
    --> python src/mostRelevantTextSearcher.py 8081
    --> On the browser, type: localhost:8081/Ok
