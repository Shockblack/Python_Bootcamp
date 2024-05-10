# Cornell Astronomy Python Bootcamp
##### By: Aiden Zelakiewicz (asz39@cornell.edu)


Welcome to the Python Bootcamp for Cornell University's Department of Astronomy. This bootcamp is primarily designed for the 2024 Research Experience for Undergraduates (REU) program, but is openly available to the wider Cornell Astronomy community. This bootcamp is heavily inspired by the [2022 Cornell REU](https://github.com/CUAstro-REU-Python-Workshop/2022-workshop) bootcamp and Ohio State Astronomy's [Python Bootcamp](https://github.com/giganano/PythonBootcamp) by James Johnson.

What you are seeing currently are files in a GitHub repository, a great tool for version control and storage of code. The bootcamp focuses on using Jupyter Notebooks, which are an interactive way to run Python. Ideally, before the bootcamp, you will have Python installed on your local computer along with Jupyter. Otherwise, we will also introduce the free service [SciServer](https://apps.sciserver.org/) from which both Python scripts and Jupyter notebooks can be used. Everything you will do in this bootcamp can be done from SciServer, and maybe even most of the research you will do, but eventually getting Python installed locally will give you much greater flexibility.

## Before the Bootcamp

### Getting Started with SciServer

SciServer is a tool hosted out of Johns Hopkins University and is a very easy and convenient way to begin coding with an emphasis on astronomy. Many astronomy databases, pipelines, and other useful tools come prebuilt into SciServer. Creating a SciServer account is free for everyone, so go ahead and make an account with a username you will remember and a secure password.

Once logged into SciServer, you will be greeted with a launch page that will look similar to the image below. You will want to click on the "Compute" button to begin (not "Compute Jobs").
![SciServer homepage.](img/sciserver_home.png)

From here you will see any containers you have created, which essentially your coding environments. Click on the "Create Container" button to make a new container. Name it whatever you would like, such as "Cornell REU" or "my silly codespace" if you are so inclined.
![SciServer container creation page.](img/sciserver_container.png)
There will be choices for the "Compute Image" that will alter what kind of programs you have access to and how the Graphical User Interface (GUI) will appear. "SciServer Essentials 2.0" will give the classic SciServer layout that I personally learned Python on, while "SciServer Essentials 3.0" and "Astronomy" will give a Jupyter Lab like view. Once you have created a name and selected your image, scroll to the bottom and click "Create" while leaving everything else at the default.
![SciServer container creation page.](img/sciserver_create.png)



### Installing the Repository

To download this entire repository locally, you can either click the <mark style="background-color: #32CD32"><>Code</mark> dropdown menu and download the zip file. Alternatively, you can type this into the terminal in a directory you want to files downloaded to:
```
$ git clone https://github.com/Shockblack/Python_Bootcamp.git
```
If you are on SciServer, on the left hand side of the Jupyter Lab