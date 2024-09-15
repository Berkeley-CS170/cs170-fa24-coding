<!-- #region -->
# fa24-coding-staff
This repository contains all the staff solutions to the notebooks and code needed to generate notebooks.

## Setup
### If you're using Datahub:
* If uploading files yourself, make sure to upload any additional files such as `requirements.txt` or additional data files
* Run the first cells in the notebook **and restart the kernel if needed**

### If you're running locally:
You'll need to perform some extra setup.
#### First-time setup
* Install Anaconda following the instructions here: https://www.anaconda.com/products/distribution 
* Create a conda environment: `conda create -n cs170 python=3.8`
* Activate the environment: `conda activate cs170`
    * See for more details on creating conda environments https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
* Install pip: `conda install pip`
* Install jupyter: `conda install jupyter`

#### Every time you want to work
* Make sure you've activated the conda environment: `conda activate cs170`
* Launch jupyter: `jupyter notebook` or `jupyter lab` 
* Run any installation cells in the notebook **and restart the kernel if needed**

## Coding Workflow
TA's
1) Refer to past semesters' error backlog (fa23 didn't have one but [sp23 does](https://docs.google.com/spreadsheets/d/13oXZmVfvn_JElcDZcZyi4qZXJ_NrBFSU2tyannBpVXg/edit#gid=0)), find the hw which your notebook corresponds to and first fix the bugs. Make sure the entire notebook can run without issue.
2) Reformat your notebook using Otter. Make sure that 1) there are no errors when you `otter assign` 2) there are no errors when you run each cell in the solution notebook 3) there are no errors when you upload the autograder to gradescope and submit the solution notebook.
3) Ask Debuggers to debug notebooks
4) When releasing the HW (tuesday evening), push notebook to public student facing Repository and use https://jupyterhub.github.io/nbgitpuller/link to generate a link which students can use to pull the notebook into Datahub.

debuggers
1) Complete that week's coding assignment and submit to gradescope.
2) Try giving edge case solutions (returning empty lists/None, malformed solutions, etc)


## Otter
This semester, we are using Otter to autograde solutions. By writing a notebook following their specific format, Otter will generate a student notebook with the solutions omitted, a solutions notebook, and create an autograder which we can then upload to gradescope. 

Otter is very pissy with the configs and formatting, so I'll mention all the important things here. For more comprehensive documentation, refer to https://otter-grader.readthedocs.io/en/latest/otter_assign/v0/python_notebook_format.html 

For the test cells that we use, we are using the exception-based format, since this is likely more familiar to those who've written unit tests in Python. See https://github.com/ucbds-infra/otter-grader/blob/master/examples/data-88e-proj03-exception/proj03.ipynb for details.

Notes:
1) __DO NOT USE TYPE ANNOTATIONS__, otter gives weird errors such as "NameError: name [function name] is not defined" if you use type annotations for some reason. Put everything into docstrings
2) Modularize your code, each cell should be able to be run independently without having to rerun cells above it. For otter, make sure each question is modularized, aside from the dependence of test cells on the student solution cells or import cells at the start. This is good practice in general but especially important so that students don't have cascading errors in their code (failing part a also fails part b). This also makes debugging easier as you don't have to worry about global variables.
3) Don't worry if the test cells end up very verbose for complicated tests. Get a working test first before trying to clean up the code.
4) Use python 3.10, as that's the version Otter will use on Gradescope.
5) Make sure you install the specific version of Otter in `requirements.txt`. Older and newer versions of Otter are **not compatible** with our autograder.

Debugging:
- When you use otter assign with our current setup, the otter assign command should tell you whether or not all the tests run correctly. However, just to be safe, navigate to the solution notebook in the autograder folder and run all the cells. 
- When you rerun otter assign and test the solution notebook, you may need to restart the kernel if you get an error running the first cell with 
```
# Initialize Otter
import otter
grader = otter.Notebook("binary_search.ipynb")
```

## Gradescope

Debugging: 
- If the solution notebook runs without error locally, but gets killed on gradescope, increase the memory limit for the assignment https://gradescope-autograders.readthedocs.io/en/latest/troubleshooting/ 

<!-- #endregion -->
