import sys
import copy
import random

from courseassignment import *


class AssignmentCreator():
    def __init__(self, courseassignment):
        """Creates Domains Assigning each Faculty to Courses and Available Course Load in there Preferences."""
        self.courseassignment = courseassignment
        self.domains = {
            faculty: {
                course : 1
                for course in faculty.preferences.copy()
            }
            for faculty in self.courseassignment.faculty_list
        }

    def save(self, assignment, filename):
        """Outputs the Assignment onto a Text File."""
        with open(filename, "a") as file:  # Use "a" for append mode
            for faculty in assignment:
                file.write(f"Faculty {faculty.faculty_id} {faculty.max_load}: ")
                for course_dict in assignment[faculty]:
                    course, load = list(course_dict.keys())[0], list(course_dict.values())[0]
                    file.write(f"{faculty.preferences[course]}, {course} -> {load}, ")
                file.write("\n")
            file.write("\n")

    def solve(self):
        return self.backtrack(dict(), self.domains)

    def available_load(self, faculty, assignment):
        """Returns the Current Available Course Load for Every Faculty."""
        load_available = faculty.max_load
        for course in assignment[faculty]:
            load_available -= sum(list(course.values()))

        return load_available

    def enforce_node_consistency(self, faculty, course, assignment, domains):
        """Removes the Recently Assigned Course from the Faculty."""
        #possible addition: remove faculty from the copy domains if available_load == 0
        if course in list(self.domains[faculty].keys()):
            del self.domains[faculty][course]

    def enforce_arc_consistency(self, faculty, course, assignment, domains):
        """Removes or Reduces Course Load from Neighboring Faculties."""
        #could change neighbors where only those neighbors are found which have the given course in common
        courses_to_remove = []
        course_load = 0
        for assigned_courses in assignment[faculty]:
            for course_check, course_load_check in assigned_courses.items():
                if course_check == course:
                    course_load = course_load_check
        for neighbor in self.courseassignment.neighbors(faculty):
            if course in list(self.domains[neighbor].keys()):
                self.domains[neighbor][course] -= course_load
                if (self.domains[neighbor][course] == 0):
                    courses_to_remove.append((neighbor, course))

        for neighbor, course in courses_to_remove:
            del self.domains[neighbor][course]
    
    def select_unassigned_faculty(self, assignment):
        """Returns Faculty that are Unassigned or not Fully Assigned."""
        unassigned_faculty = None
        #needs to be changed so that only a random faculty is choosed
        for faculty in random.sample(list(self.domains), len(self.domains)):
            if faculty not in assignment:
                if unassigned_faculty is None:
                    unassigned_faculty = faculty
                    break
                else:
                    if len(self.courseassignment.neighbors(faculty)) > len(self.courseassignment.neighbors(unassigned_faculty)):
                        unassigned_faculty = faculty
                        break
            else:
                load_available = self.available_load(faculty, assignment)
                if load_available >= 0.5:
                    if unassigned_faculty is None:
                        unassigned_faculty = faculty
                        break
                    else:
                        if len(self.courseassignment.neighbors(faculty)) > len(self.courseassignment.neighbors(unassigned_faculty)):
                            unassigned_faculty = faculty
                            break

        return unassigned_faculty

    def backtrack(self, assignment, domains):
        """Recursively Checks and Assigns possible Courses to Faculties."""
        all_faculties_assigned = all(
            faculty in assignment and abs(self.available_load(faculty, assignment)) < 1e-10
            for faculty in self.domains
        )
        if all_faculties_assigned:
            return assignment

        faculty = self.select_unassigned_faculty(assignment)
        if faculty is not None:
            for course, course_load_available in self.domains[faculty].items():
                if course_load_available > 0:
                    new_assignment = assignment.copy()
                    new_domains = domains.copy()

                    if faculty not in new_assignment:
                        new_assignment[faculty] = []

                    if self.available_load(faculty, new_assignment) != 0:
                        if course_load_available == 0.5:
                            new_assignment[faculty].append({course: 0.5})
                        else:
                            new_assignment[faculty].append({course: min(1, self.available_load(faculty, new_assignment))})
                    else:
                        break

                    self.enforce_node_consistency(faculty, course, new_assignment, new_domains)
                    self.enforce_arc_consistency(faculty, course, new_assignment, new_domains)
                    result = self.backtrack(new_assignment, new_domains)
                    if result is not None:
                        return result

        return None
                    

def main():

    if len(sys.argv) != 3:
        sys.exit("Usage: python3 generate.py preferences [output]")

    preferences_file = sys.argv[1]
    output = sys.argv[2]

    courseassignment = Courseassignment(preferences_file)
    assignmentcreator = AssignmentCreator(courseassignment)
    assignment = assignmentcreator.solve()

    if assignment is None:
        print("No Possible Assignment.")
    else:
        assignmentcreator.save(assignment, output)


if __name__ == "__main__":
    main()