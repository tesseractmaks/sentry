SELECT name_teacher, min(min_grade) FROM (SELECT teachers.full_name as name_teacher, avg(assignments_grades.grade) as min_grade FROM teachers
INNER JOIN assignments ON assignments.teacher_id = teachers.teacher_id
INNER JOIN assignments_grades ON assignments_grades.assisgnment_id = assignments.assisgnment_id
GROUP BY teachers.full_name);