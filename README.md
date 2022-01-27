# Carbon-Capture Membrane

> A program to simulate a gas seperation membrane, tested for carbon capture.

## Table of Contents

-   [General Info](#general-information)
-   [Technologies Used](#technologies-used)
-   [Features](#features)
-   [Screenshots](#screenshots)
-   [Setup](#setup)
-   [Usage](#usage)
-   [Project Status](#project-status)
-   [Room for Improvement](#room-for-improvement)
-   [Acknowledgements](#acknowledgements)
-   [Contact](#contact)
<!-- * [License](#license) -->

## General Information

This project was initially part of my MEng disseration, however the focus was on the chemical engineering aspects at that time.
Since then the project has been re-written as a practical learning exercise to aid my understanding of:

-   Object Oriented Design (OOD)
-   Test driven development (TDD)
-   Implementing proper documentation

<!-- You don't have to answer all the questions - just the ones relevant to your project. -->

## Technologies Used

-   pytest - 6.2.5
-   Sphinx - 4.3.2

## Features

-   Comprehensive unit testing.
-   Full documentation - with Sphinx generated web page.
-   Makes use of python features such as:
    -   Descriptors
    -   Fixtures

<!-- ## Screenshots

![Example screenshot](./img/screenshot.png) -->

<!-- If you have screenshots you'd like to share, include them here. -->

## Setup

1. Navigate to directory that will host the project
2. Clone the repo:
   `git clone https://github.com/Josh-Human/membrane.git`
3. Navigate into directory
   `cd membrane`
4. Create a virtual env
   `python3 -m venv .venv`
5. Activate enviroment
   `.venv/Scripts/activate`
6. Install required packages
   `pip install -r requirements.txt`

## Usage

All tests may be run using
`pytest`

Specific tests may be run using
`pytest <file_path>`

## Project Status

Project is: in progress. Changes will be made to improve existing code and expand upon work as time allows.

## Room for Improvement

Room for improvement:

-   Better understanding of when to use 'private' and public attributes.
-   Understanding of what makes a good test.
    -   e.g had a series of tests for simple getter/setter functions
-   Understanding of project architecture.

To do:

-   Refactor JSON/consturctor classes to have keys with value null rather than adding on instance.
-   Improve formatting of Sphinx web page.
-   Host documentation online.
-   Create additonal models for more complex simulations.

## Acknowledgements

Many thanks to my academic supervisors Professor Ferrari & Professor Baschetti.

## Contact

Created by [@Josh](https://www.linkedin.com/in/joshua-human/) - feel free to contact me!

<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
