# Loan-Qualifier-CLI
This program uses a command line interface to ask the user for their loan application information and the path to a data set of available loans. It filters those loans according to the information provided and offers to save the results to a CSV file. The command line interface is intended to increase usability for the user.

---

## Technologies

This python 3.7 program uses the sys, fire, questionary, and pathlib libraries as they are current on 9/27/2021. It was tested in a git bash environment in Windows 10 and also works on python 3.8.8. 

It uses calculator functions written to calculate debt to income and loan to value ratios, and filter functions for a list of loans available by the max loan size, credit score, debt to income ratio, and loan to value ratio compared to the user entered amounts.

It uses functions to load and save CSV files.

---

## Installation Guide

This program requires installation of Python, gitbash for windows users, and questionary. It was tested on Python 3.7 and 3.8.8.

See:
- [Python install files](https://www.python.org/downloads/)
- [Git install files](https://git-scm.com/downloads) (In mac you can use the terminal)

For questionary to work, you must type in git bash or mac terminal:
```pip install pip```


## Usage

This section should include screenshots, code blocks, or animations explaining how to use your project.

This program requires as input a CSV file that is structured as rows of comma separated lists, in the following format:

![screenshot of CSV input file opened in notepad]()

The git bash / terminal input to run this function is:

``` $ python app.py

Some usage examples:

![](https://github.com/phodsman/Loan-Qualifier-CLI/blob/main/Screenshot%202021-09-27%20112931.png?raw=true)

![](https://github.com/phodsman/Loan-Qualifier-CLI/blob/main/Screenshot%202021-09-27%20120216.png?raw=true)

![](https://github.com/phodsman/Loan-Qualifier-CLI/blob/main/Screenshot%202021-09-27%20120257.png?raw=true)

![](https://github.com/phodsman/Loan-Qualifier-CLI/blob/main/Screenshot%202021-09-27%20120351.png?raw=true)

![](https://github.com/phodsman/Loan-Qualifier-CLI/blob/main/Screenshot%202021-09-27%20120618.png?raw=true)

![](https://github.com/phodsman/Loan-Qualifier-CLI/blob/main/Screenshot%202021-09-27%20120704.png?raw=true)

![](https://github.com/phodsman/Loan-Qualifier-CLI/blob/main/Screenshot%202021-09-27%20124518.png?raw=true)

---

## Contributors

In this section, list all the people who contribute to this project. You might want recruiters or potential collaborators to reach you, so include your contact email and, optionally, your LinkedIn or Twitter profile.

---

## License

When you share a project on a repository, especially a public one, it's important to choose the right license to specify what others can and can't with your source code and files. Use this section to include the license you want to use.