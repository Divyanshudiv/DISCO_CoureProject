# DISCO_CourseProject
An Application of Graph Optimization-Course Project
The research problem at hand revolves around the optimization of the University Course Assignment System. Within a department, there are "n" faculty members categorised into three distinct groups: "x1," "x2," and "x3." Faculty in each category are assigned different course loads, with "x1" handling 0.5 courses per semester, "x2" taking 1 course per semester, and "x3" managing 1.5 courses per semester.

In this system, faculty members have the flexibility to take multiple courses in a given semester, and conversely, a single course can be assigned to multiple faculty members. When a course is shared between two professors, each professor's load is considered to be 0.5 courses. Moreover, each faculty member maintains a preference list of courses, ordered by their personal preferences, with the most preferred courses appearing at the top. Importantly, there is no prioritisation among faculty members within the same category.

The primary objective of this research problem is to develop an assignment scheme that maximises the number of courses assigned to faculty while aligning with their preferences and the category-based constraints ("x1," "x2," "x3"). The challenge lies in ensuring that a course can only be assigned to a faculty member if it is present in their preference list.

This problem is unique due to the flexibility it offers regarding the number of courses faculty members can take, distinct from typical Assignment problems. Potential modifications may include adjusting the maximum number of courses "y" for each category of professors, instead of requiring exact adherence, or extending the number of professor categories beyond the existing three to devise a more generalised solution.

---------------------------------------------------------------------------------------------------------------------------------------------
The aim is to achieve a good degree of optimization on this constraint satisfaction problem through enforcing node consistency, arc consistency and utilizing techniques like backtracking.

Currently the program is able to optimally assign upto 50 faculties(we didn't test for higher number of faculties).

Generating the Dataset:
We created a program in Python to generate input test-cases to test the implementation of our programs. We got hands on a list of courses offered at our college from the BITS timetable document. We used excel to get 
the courses in a csv file. Then, we categorised the courses obtained into FD.csv containing First Degree courses and HD.csv containing Higher Degree courses. After this, we created a dictionary with keys "FDCDC", 
"FDELE", "HDCDC" and "HDELE". We assigned random values from the FD.csv file to FDCDC and FDELE keys and from HD.csv to HDCDC and HDELE keys of the dictionary. We also created another python script to generate 
faculty and randomly put them in categories, i.e. x1, x2 and x3 according to the number of faculties given as an argument. Using the count of x1, x2 and x3, we calculated the number of courses that would be required 
to assign the data to the faculties. The subjects needed was calculated as : 0.5*count("x1") + 1*count("x2") + 1.5*count("x3"). According to the subjects needed, we extracted the desired amount of subjects from the 
FD.csv and HD.csv. We then randomly assigned every faculty member 12 preferences; 4 FDCDCs, 4 FDELEs, 2 HDCDCs and 2 HDELEs. We then push this data to a csv file and use this csv file in our main program as the 
Faculty_data.csv.

---------------------------------------------------------------------------------------------------------------------------------------------
#To create a new dataset, first set the dataset variable in the Subjects_Generator.py as the number of faculty for which you want to generate the data. Then use python3 preference_assignment.py. This will create Faculty_data.csv.
#To run the assignment program use python3 generateV2.py input.csv output.txt


