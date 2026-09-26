class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        iterations = len(students)

        while True:
            
            if len(students) < 1:
                return len(students)

            student_first_in_line = students[0]
            sandwich_first_served = sandwiches[0]

            students_remaining = []
            sandwiches_remaining = []

            # "we've cycled through all the students already"
            if iterations == 0:
                return len(students)
            
            if student_first_in_line == sandwich_first_served:
                # pop both students and sandwiches

                students.pop(0)
                sandwiches.pop(0)
                iterations = len(students)
                
            else:
                # wrong here since we follow the stack convention
                # students.append(student_first_in_line)
                # students.pop(0)
                
                # pop then add, much better
                students_that_distaste_sandwiches = students.pop(0)
                students.append(students_that_distaste_sandwiches)
                iterations-=1

                # iterations act as a reverse accumulator