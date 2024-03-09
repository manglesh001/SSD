CREATE DATABASE ABC;
USE ABC;
CREATE TABLE ABC.Employee(
	emp_no INT PRIMARY KEY,
    emp_name VARCHAR(50),
    emp_joining_date VARCHAR(20),
    emp_salary INT 
);
select * from ABC.Employee;
CREATE TABLE ABC.Courses(
course_id VARCHAR(10) PRIMARY KEY,
course_name VARCHAR(50)
);

CREATE TABLE ABC.Certifications(
cert_id VARCHAR(10) PRIMARY KEY,
cert_name VARCHAR(50)
);

CREATE TABLE ABC.CourseCompletions(
course_id VARCHAR(10),
emp_no INT,
date_completed VARCHAR(20),
FOREIGN KEY (emp_no) REFERENCES ABC.Employee(emp_no),
FOREIGN KEY (course_id) REFERENCES ABC.Courses(course_id)
);

CREATE TABLE ABC.CertificateCompletions(
cert_id VARCHAR(10),
emp_no INT,
date_completed VARCHAR(20),
FOREIGN KEY (emp_no) REFERENCES ABC.Employee(emp_no),
FOREIGN KEY (cert_id) REFERENCES ABC.Certifications(cert_id)
);

select * from ABC.Employee;
select * from ABC.Courses;
select * from ABC.CourseCompletions;
select * from ABC.Certifications;
select * from ABC.CertificateCompletions;

UPDATE ABC.Employee
SET emp_joining_date=date_format(STR_TO_DATE(emp_joining_date,'%d-%m-%Y'),'%Y-%m-%d');

ALTER TABLE ABC.Employee
MODIFY COLUMN emp_joining_date date; 

UPDATE ABC.CourseCompletions
SET date_completed=date_format(STR_TO_DATE(date_completed,'%d-%m-%Y'),'%Y-%m-%d');

ALTER TABLE ABC.CourseCompletions
MODIFY COLUMN date_completed date; 

UPDATE ABC.CertificateCompletions
SET date_completed=date_format(STR_TO_DATE(date_completed,'%d-%m-%Y'),'%Y-%m-%d');

ALTER TABLE ABC.CertificateCompletions
MODIFY COLUMN date_completed date; 

DELIMITER $$
CREATE PROCEDURE UpdateEmpSkill()
BEGIN
DECLARE empid INT;
DECLARE salary INT;
DECLARE flag INT DEFAULT 0;
DECLARE CertificateNo INT;
DECLARE joinDate DATE;
DECLARE skillLevel VARCHAR(40);
DECLARE CourseNo INT;
DECLARE newSalary INT;
DECLARE increment INT;

DECLARE My_Cursor CURSOR FOR
SELECT E.emp_no,COALESCE(CP.no_of_Courses,0)AS no_of_Courses,
COALESCE(CC.no_of_Certifications,0)AS no_of_Certifications,
E.emp_joining_date,E.emp_salary
FROM ABC.Employee AS E
INNER JOIN(SELECT emp_no,COUNT(course_id)AS no_of_Courses 
FROM ABC.CourseCompletions
GROUP BY emp_no)AS CP 
ON E.emp_no=CP.emp_no
INNER JOIN(
SELECT emp_no,COUNT(cert_id) AS no_of_Certifications
FROM ABC.CertificateCompletions
GROUP BY emp_no)AS CC 
ON E.emp_no=CC.emp_no;

DECLARE CONTINUE HANDLER FOR NOT FOUND SET flag= 1;
CREATE TABLE IF NOT EXISTS UpdatedEmpSkills(
emp_no INT,
curr_salary INT,
increment INT,
new_salary INT,
skill_level VARCHAR(30)
);

OPEN My_Cursor;
FETCH_ROW:
LOOP
FETCH My_Cursor INTO empid,CourseNo,CertificateNo,joinDate,salary;
IF flag THEN
LEAVE FETCH_ROW;
END IF;

IF joinDate<='2022-07-31' THEN
IF CourseNo>=10 AND CertificateNo>=8 THEN
SET skillLevel='Expert';
SET increment=salary*0.25;
SET newSalary=increment+salary;
INSERT INTO UpdatedEmpSkills
VALUES (empid,salary,increment,newSalary,skillLevel);
ELSEIF CourseNo>=6 AND CertificateNo>=6 THEN
SET skillLevel='Advanced';
SET increment=salary*0.2;
SET newSalary=increment+salary;
INSERT INTO UpdatedEmpSkills
VALUES (empid,salary,increment,newSalary,skillLevel);
ELSEIF CourseNo >= 4 AND CertificateNo>=4 THEN
SET skillLevel='Intermediate';
SET increment=salary*0.15;
SET newSalary=increment+salary;
INSERT INTO UpdatedEmpSkills
VALUES (empid,salary,increment,newSalary,skillLevel);
ELSEIF CourseNo>=2 AND CertificateNo>=2 THEN
SET skillLevel='Beginner';
SET increment=salary*0.1;
SET newSalary=increment+salary;
INSERT INTO UpdatedEmpSkills
VALUES (empid,salary,increment,newSalary,skillLevel);
ELSE
SET skillLevel=NULL;
SET increment=0;
END IF;

END IF;
END LOOP;

CLOSE My_Cursor;
END $$
DELIMITER ;

SELECT * FROM UpdatedEmpSkills;


CALL UpdateEmpSkill();

