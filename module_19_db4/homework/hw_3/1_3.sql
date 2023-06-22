SELECT students.full_name, id_teacher, max(max_grade) as grade FROM (SELECT teachers.teacher_id as id_teacher, avg(assignments_grades.grade) as max_grade FROM teachers
INNER JOIN assignments ON assignments.teacher_id = teachers.teacher_id
INNER JOIN assignments_grades ON assignments_grades.assisgnment_id = assignments.assisgnment_id
GROUP BY teachers.teacher_id) g
INNER JOIN  students ON students.group_id = (SELECT students_groups.group_id FROM students_groups WHERE teacher_id = g.id_teacher)
GROUP BY students.full_name
HAVING id_teacher = 2;