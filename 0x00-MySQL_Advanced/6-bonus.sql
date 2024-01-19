--  a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

-- Requirements:

-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
-- project_name, a new or already exists projects - if no projects.name found in the table, you should create it
-- score, the score value for the correction

DELIMITER //

CREATE PROCEDURE AddBonus(IN in_user_id INT, IN in_project_name VARCHAR(255), IN in_score INT)
BEGIN
    DECLARE in_project_id INT;

    SELECT id INTO in_project_id
    FROM projects
    WHERE name = in_project_name;

    IF in_project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (in_project_name);
        SET in_project_id = LAST_INSERT_ID();
    END IF;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (in_user_id, in_project_id, in_score);

END;

//

DELIMITER ;
