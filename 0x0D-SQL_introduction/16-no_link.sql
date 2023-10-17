-- a script that delete the database hbtn_0c_0 in your MySQL server 
-- because Batch 3 is the best!
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;