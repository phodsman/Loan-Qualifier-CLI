# Loan-Qualifier-CLI
This program uses a command line interface to ask the user for their loan application information and the path to a comma separated value (CSV) data set of available loans. It filters those loans according to the information provided and offers to save the results to a CSV file. The command line interface is intended to increase usability for the user.

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

This program requires as input a CSV file that is structured as rows of comma separated lists, in the following format:

![Screenshot of CSV file for input in notepad](https://github.com/phodsman/Loan-Qualifier-CLI/blob/main/Screenshot%202021-09-27%20124518.png?raw=true)

The git bash / terminal input to run this function is:

``` $ python app.py```

Some usage examples:

Found loans, saved in new folder:  
![](https://github.com/phodsman/Loan-Qualifier-CLI/blob/main/Screenshot%202021-09-27%20112931.png?raw=true)  

![](https://github.com/phodsman/Loan-Qualifier-CLI/blob/main/Screenshot%202021-09-27%20120216.png?raw=true)

Use the tab key to show available files and folders instead of manually typing the path:  
![](https://github.com/phodsman/Loan-Qualifier-CLI/blob/main/Screenshot%202021-09-27%20120257.png?raw=true)

No qualifying loans found:  
![](https://github.com/phodsman/Loan-Qualifier-CLI/blob/main/Screenshot%202021-09-27%20120351.png?raw=true)

Deciding not to create a new folder:  
![](https://github.com/phodsman/Loan-Qualifier-CLI/blob/main/Screenshot%202021-09-27%20120618.png?raw=true)

Deciding not to save the output to file:
![](https://github.com/phodsman/Loan-Qualifier-CLI/blob/main/Screenshot%202021-09-27%20120704.png?raw=true)

---

## Contributors

This code was adapted from the Loan Qualifier code © 2020 - 2021 Trilogy Education Services, a 2U, Inc. brand.
Additional coding for usability was added by Preston Hodsman, phodsman@yahoo.com

---

## License

MIT License

Copyright (c) 2021 Preston Hodsman

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.