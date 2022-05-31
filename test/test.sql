SELECT json_object(
   'user' VALUE a.username,
   'sqltext' VALUE replace(b.sql_fulltext, chr(10), ' ')
)
FROM v$session a, v$sql b
WHERE a.sql_id = b.sql_id AND a.status = 'ACTIVE' AND a.username is not null;

quit;
/