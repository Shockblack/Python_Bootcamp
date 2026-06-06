# Cornell Astronomy Python Bootcamp
##### By: Aiden Zelakiewicz (asz39@cornell.edu)


Welcome to the Python Bootcamp for Cornell University's Department of Astronomy. This bootcamp is primarily designed for the 2024 Research Experience for Undergraduates (REU) program, but is openly available to the wider Cornell Astronomy community. This bootcamp is heavily inspired by the [2022 Cornell REU](https://github.com/CUAstro-REU-Python-Workshop/2022-workshop) bootcamp, Ohio State Astronomy's [Python Bootcamp](https://github.com/giganano/PythonBootcamp) by James Johnson, and the OSU Astronomy 1221 and 3350 courses by Prof. Donald Terndrup.

What you are seeing currently are files in a GitHub repository, a great tool for version control and storage of code. The bootcamp focuses on using Jupyter Notebooks, which are an interactive way to run Python. Ideally, before the bootcamp, you will have Python installed on your local computer along with Jupyter. 

## Before the Bootcamp

Before we begin the bootcamp, I would like you to figure out how you will be using Python and Jupyter. We strongly recommend to run Python locally within an Integrated Developement Environment (IDE) such as Microsoft's [Visual Studio Code](https://code.visualstudio.com/) (VSCode). This is personally where I (Aiden) do ALL of my coding and is the most community supported IDE available today. Once you learn VSCode, you will never go back as it is such a boon to coding in multiple languages at once with many customizable quality of life features, such as AI autocomplete, autobracketing, colorized indents, and so much more.

Things to do before the bootcamp begins are as follows:
1. Get Access To Python (details below)
2. Download/Clone the Repository (details below)
3. Install the required Python packages using the `environment.yml` file (details below)
4. Go through [BeforeBootcamp.ipynb](code/BeforeBootcamp/BeforeBootcamp.ipynb) as a primer

### 1. Getting Access to Python

One of the best ways to get access to Python is through the [Anaconda Distribution](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html). These are free, open-source distributions of Python that come with a package manager called `conda` which makes it easy to install and manage Python packages. Anaconda comes with a lot of pre-installed packages, while Miniconda is a minimal installer that allows you to install only the packages you need. We *strongly* recommend using Anaconda or Miniconda to manage your Python environment, and installing it through the command line interface (CLI) rather than the graphical user interface (GUI) for better control and understanding of your Python environment. The Anaconda GUI will more or less become a crutch that you will have to get past eventually.

Links to download Anaconda and Miniconda:
- [Anaconda](https://www.anaconda.com/docs/getting-started/anaconda/install/overview)
- [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install/overview)

Here are some basic quickstart commands to get you started with Anaconda/Miniconda:
```bash
# Create a new conda environment named "my_environment" with Python 3.12
$ conda create -n my_environment python=3.12

# Create an environment using the environment.yml
$ conda env create -f environment.yml

# Activate the environment
$ conda activate my_environment

# Deactivate the environment
$ conda deactivate

# Install a package (e.g., numpy) in the current environment (using pip)
$ pip install numpy
```


### 2. Cloning the Repository

To download this git repository (called "cloning") locally, you can either click the <mark style="background-color: #32CD32"><>Code</mark> dropdown menu and download the zip file. Alternatively, you can type this line into the terminal in a directory you want the files downloaded to (**RECOMMENDED**):
```
$ git clone https://github.com/Shockblack/Python_Bootcamp.git
```
or
```
$ git clone git@github.com:Shockblack/Python_Bootcamp.git
```

### 3. Installing Required Python Packages

The `environment.yml` file in the root of this repository contains a list of all the Python packages required for the bootcamp. To install these packages, you can use the following command in your terminal:
```bash
$ conda env create -f environment.yml
```
This will create a new conda environment with all the required packages installed. You can then activate this environment using:
```bash
$ conda activate astro-bootcamp
```

### 4. Going Through the Primer

You are ready to begin! Head on over to the notebook located at [`code/BeforeBootcamp/BeforeBootcamp.ipynb`](code/BeforeBootcamp/BeforeBootcamp.ipynb) and go through the primer. This notebook covers the Python fundamentals you need before Day 1 of the bootcamp. It is not meant to be an exhaustive introduction to Python, but rather a quick refresher on the basics.

Happy coding!