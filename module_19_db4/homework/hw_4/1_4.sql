SELECT max(assisgnment), min(assisgnment), avg(assisgnment), groups FROM (
SELECT count(assignments.assisgnment_id) as assisgnment, assignments.group_id as groups FROM assignments
GROUP BY groups)
GROUP BY groups;