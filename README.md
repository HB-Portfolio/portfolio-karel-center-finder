# Find The Centre Karel

I made this as my final Karel project to showcase what can be done with just a few simple starting functions. This Karel can find the centre of any square. Based on my theory, although not efficient, it could find the centre of a square with an area approaching infinity.

**Author:** Hendrich Buhrer  
**Certification:** [Stanford Code in Place Certificate](https://codeinplace.stanford.edu/cip4/certificate/e80xil)  
**Deployed Project:** [Karel Centre Finder](https://codeinplace.stanford.edu/cip4/share/4AdpjabHDMmMKVeGyPxE)

## Project Details

This project was developed as part of the **Code in Place** program by Stanford University. You can view the deployed project on the [Stanford Code in Place Website](https://codeinplace.stanford.edu/cip4/share/4AdpjabHDMmMKVeGyPxE).

I earned a certification for completing this course, which you can view [here](https://codeinplace.stanford.edu/cip4/certificate/e80xil).

## Karel and StanfordKarel Library

Karel the Robot is a programming language and learning environment developed by Richard E. Pattis. It is used to introduce students to programming concepts and logical thinking. The StanfordKarel library is a Python implementation that is part of Stanford's CS106 program, designed to make it easier for students to create Karel programs using Python.

### Key Features

- **Custom Python Library:** Utilizes the `stanfordkarel` library, which provides functions to control Karel and interact with the environment.
- **Centre Finding Algorithm:** Karel can find the centre of any square grid by placing beepers and moving systematically to determine the midpoint.

## Code Quality and Structure

All the files are uploaded to the repository. I encourage you to look at the code to see the quality and structure. The main logic includes:

- **Finding the Centre:** The main algorithm involves functions to find the row and column midpoints.
- **Column Midpoint:** Functions to check the height, fill and clear columns, and find the column midpoint.
- **Row Midpoint:** Functions to check the width, fill and clear rows, and find the row midpoint.

## How It Works

- **find_the_centre:** Calls the functions to find the row and column midpoints.
- **find_row_midpoint and find_column_midpoint:** Check the dimensions, fill the row/column with beepers, clear unnecessary beepers, and identify the midpoint.
- **Helper Functions:** Includes functions like `fill_row`, `fill_column`, `clear_row`, `clear_column`, and utility functions like `turn_right` and `turn_around`.
