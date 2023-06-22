SELECT name_student, avg(student_grade) as avg_grade FROM (SELECT students.full_name as name_student, assignments_grades.grade as student_grade FROM students
INNER JOIN assignments_grades ON assignments_grades.student_id = students.student_id) collect
GROUP BY collect.name_student
ORDER BY avg_grade DESC
LIMIT 10;