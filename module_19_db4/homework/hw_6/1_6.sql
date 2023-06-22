SELECT avg(assignments_grades.grade) as avg_grade from assignments_grades
INNER JOIN assignments ON assignments.assisgnment_id = assignments_grades.assisgnment_id
WHERE assignments.assignment_text LIKE 'прочитать%' OR assignments.assignment_text LIKE 'выучить%';