SELECT students.group_id, avg(assignments_grades.grade) as avg_grade_in_group, count(assignments_grades.assisgnment_id) as total_assignments_in_group, count(assignments_grades.student_id) as total_students_received_grades_for_assignments_in_group,  count(students.student_id) as total_students_in_group from assignments_grades
INNER JOIN students ON students.student_id = assignments_grades.student_id
INNER JOIN students_groups ON students_groups.group_id = students.group_id
GROUP BY students.group_id;