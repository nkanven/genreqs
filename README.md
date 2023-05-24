# GenReqs : Generate Requirements file for python
> Genreqs is a straighforward python package which allow deveoper to automate
> the creation of the requirements.txt file for their project.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- Unlike other alternatives available, GenReqs aims to be more precised and 
- specific about selecting the most relevant package and not just all packages
- and their unnecessary dependancies listed through pip list.
- Many python developers use to copy and paste the required packages for a certain
- project from the pip list which can be very fastidious and time consuming for
- large projects with alot of packages.
- GenReqs is here to save you time and allow you to focus on building your project.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- GenReqs need only Python 3 to function

## Features
With GenReqs, you can generated :
- Generate requirements.txt from global Python environment
- Generate requirements.txt from any other Python environment


## Setup
Make sure you have pip install.

For Linux users
`sudo apt install python3-pip`

clone this repo in your computer, preferrably on your project root dir.
Package can be executed globally if add to System environment path.
Launch the module with


`python PATH_TO_PACKAGE_DIR genreqs -h`

for help.



## Usage
How does one go about using it?

- You can just generate the requirements.txt of you python environment every easily by typing :

`python PATH_TO_PACKAGE_DIR genreqs`

- This will generate the requirements.txt of the python environment you are in.
- If you need the requirements.txt of a particular project on a precised environment
- you are not in. Give the absolute path of the python folder by typing:

`python PATH_TO_PACKAGE_DIR genreqs -p PATH_TO_PYTHON_FOLDER`


## Project Status
Project is: _in progress_ I am continously adding features and updating the package

## Room for Improvement

Room for improvement:
- Upload the package to Pypi
- Make it run in pycharm environment without error


## Contact
Created by [@nkanven](https://www.linkedin.com/in/nkondog) - feel free to contact me!


## License
This project is open source and available under the MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
