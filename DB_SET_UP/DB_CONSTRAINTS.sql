USE DB_PROJECT;
 
 #Έλεχος στο projects
ALTER TABLE PROJECTS
ADD CONSTRAINT check_funding_min CHECK (100000.00<=funding),
ADD CONSTRAINT check_funding_max CHECK(funding<=1000000.00),
ADD CONSTRAINT valid_date CHECK (start_date<due_date),
ADD CONSTRAINT valid_duration CHECK (due_date>DATE_SUB(start_date,INTERVAL -1 YEAR)),
ADD CONSTRAINT valid_runtime CHECK (due_date<DATE_SUB(start_date,INTERVAL -4 YEAR));

#Δεν επιτρέπεται η εισαγωγή έργων που δεν έχουν πάρει έγκριση δηλαδή με βαθμό<50

ALTER TABLE EVALUATIONS 
ADD CONSTRAINT check_grade CHECK (grade>=50);

#Έλεγχος η τιμή για το φύλο του ερευνητή να εισάγεται ως (M ή F)
#Ο ερευνητής να είναι 18 ετών την ημέρα πρόσληψής του στον οργανισμό
ALTER TABLE RESEARCHERS 
ADD CONSTRAINT check_sex CHECK ((sex='M') XOR (sex='F')),
ADD CONSTRAINT check_date_of_birth CHECK (DATE_SUB(date_of_birth,INTERVAL -18 YEAR)<date_of_recruitment);

#Έλεγχος η ημέρα πρόσληψης ενός ερευνητή να μην είναι μεγαλύτερη της τρέχουσας ημερομηνίας

DELIMITER $$

CREATE TRIGGER check_date_of_recruitment
BEFORE INSERT ON RESEARCHERS
FOR EACH ROW
BEGIN
IF 
(NEW.date_of_recruitment > CURRENT_DATE()) THEN
SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Warning: Recruitment date cant be greater than current date!';
END IF;
END$$
    DELIMITER ;

#Η ημερομηνία της αξιολόγησης πρέπει να είναι μικρότερη της ημερομηνίας έναρξης του έργου

DELIMITER $$

CREATE TRIGGER check_evaluation_date
BEFORE INSERT ON PROJECTS
FOR EACH ROW
BEGIN
SET @eval_date=(SELECT evaluation_date FROM EVALUATIONS WHERE evaluation_id=NEW.evaluation_id);
IF (@eval_date > NEW.start_date) THEN
SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Warning: Evaluation date should be prior start date of project!';
END IF;
END$$
	DELIMITER ;


#Η ημερομηνία παράδοσης του κάθε παραδοτέου πρέπει να είναι μεταξύ ημερομηνίας έναρξης του έργου και ημερομηνία λήξης
DELIMITER $$
	
CREATE TRIGGER check_delivery_date
BEFORE INSERT ON DELIVERABLES
FOR EACH ROW
BEGIN
SET @start_date = (SELECT start_date FROM PROJECTS WHERE project_id=NEW.project_id);
SET @due_date = (SELECT due_date FROM PROJECTS WHERE project_id=NEW.project_id);
IF(@start_date>NEW.delivery_date) OR (@due_date<NEW.delivery_date) THEN
SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Warning: Delivery date should be between start date of project and due date ';
END IF;
END$$
	DELIMITER ;

#Οι προϋπολογισμοί να είναι θετικοί κάθε οργανισμού
ALTER TABLE RESEARCH_CENTRES
ADD CONSTRAINT check_1 CHECK(ministry_of_education>0),
ADD CONSTRAINT check_2 CHECK(private_activities>0);

ALTER TABLE UNIVERSITIES
ADD CONSTRAINT check_3 CHECK(ministry_of_education>0);

ALTER TABLE COMPANIES
ADD CONSTRAINT check_4 CHECK(own_funds>0);

#Κάθε project να έχει μόνο μια αξιολόγηση

DELIMITER $$
CREATE TRIGGER check_for_unique_evaluation
BEFORE INSERT ON EVALUATES
FOR EACH ROW
BEGIN
IF (EXISTS(SELECT * FROM EVALUATES WHERE project_id = NEW.project_id)) THEN
SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Warning : Only one evaluation per project';
END IF;
END $$
DELIMITER ;


#Ο αξιολογητής δεν μπορεί να αξιολογεί πρότζεκτ του οργανισμού του

DELIMITER $$
CREATE TRIGGER check_for_evaluator_and_organization
BEFORE INSERT ON PROJECTS
FOR EACH ROW
BEGIN
SET @org_of_evaluator = (SELECT R.organization_id FROM RESEARCHERS R JOIN EVALUATES E WHERE (E.project_id=new.project_id and R.researcher_id = E.researcher_id));
IF(NEW.organization_id = @org_of_evaluator) THEN
SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Warning : Researcher cant evaluate project of his/hers organization';
END IF;
END $$


#Ο επιστημονικός υπεύθυνος πρέπει να δουλεύει σε πρότζεκτ του οργανισμού του

DELIMITER $$
CREATE TRIGGER check_advisor_organization
BEFORE INSERT ON PROJECTS
FOR EACH ROW
BEGIN
SET @org_id = (SELECT organization_id FROM RESEARCHERS WHERE researcher_id = NEW.researcher_id);
IF(NEW.organization_id<>@org_id) THEN
SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Warning : Scientific advisor has to work at project of their organization !';
END IF;
END$$
DELIMITER ;;

# Ο επιστημονικός υπεύθυνος να μην τοποθετείται και στον πίνακα works_on
DELIMITER $$
CREATE TRIGGER check_for_advisor_and_worker
BEFORE INSERT ON PROJECTS
FOR EACH ROW
BEGIN 
IF(EXISTS(SELECT * FROM WORKS_ON WHERE (NEW.researcher_id=researcher_id and project_id = new.project_id))) then
SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Warning : Scientific advisor cant also work on the project !';
END IF;
END $$
DELIMITER ; 

#Ένας ερευνητής μπορεί να δουλεύει μόνο σε πρότζεκτ του οργανισμού του
DELIMITER $$
CREATE TRIGGER check_worker_organization
BEFORE INSERT ON PROJECTS
FOR EACH ROW
BEGIN
IF(EXISTS(SELECT * FROM WORKS_ON W JOIN RESEARCHERS R WHERE (R.researcher_id=W.researcher_id and W.project_id = new.project_id and R.organization_id <> new.organization_id))) THEN
SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Warning : Worker has to work on project of his organization !';
END IF;
END $$
DELIMITER ;;

#Το νεό start date δε θα πρέπει να είναι μεγαλύτερο του delivery date και το νέο due date να μην είανι μεγαλύτερο 

DELIMITER $$
CREATE TRIGGER check_alter_dates_projects
BEFORE UPDATE ON PROJECTS
FOR EACH ROW
BEGIN
IF(EXISTS(SELECT * FROM DELIVERABLES WHERE (project_id = new.project_id AND (new.start_date>delivery_date or new.due_date<delivery_date)))) THEN
SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Warning : Cant update start date or due date due to deliverable date';
END IF;
END $$
DELIMITER ;;

#Έλεγχος στο worκs_on ώστε ένας ερευνητής να δουλεύει μόνο σε project του οργανισμού του
DELIMITER $$
CREATE TRIGGER check_insert_new_working_relationship
BEFORE INSERT ON WORKS_ON
FOR EACH ROW
BEGIN
SET @org_id = (SELECT organization_id FROM RESEARCHERS WHERE new.researcher_id = researcher_id);
IF(EXISTS(SELECT * FROM PROJECTS WHERE (project_id = new.project_id AND organization_id <> @org_id))) THEN 
SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Warning : Researcher cant work on a project not of his organization';
END IF;
END $$
DELIMITER ;;

#Έλεγχος προϋποθέσεων ώστε να διαγραφεί ένας ερευνητής

DELIMITER $$
CREATE TRIGGER check_delete_researcher
BEFORE DELETE ON RESEARCHERS
FOR EACH ROW
BEGIN
SET @org_id = (SELECT organization_id FROM RESEARCHERS WHERE researcher_id = OLD.researcher_id);
IF(EXISTS(SELECT * FROM EVALUATES WHERE researcher_id = OLD.researcher_id) OR EXISTS(SELECT * FROM PROJECTS P WHERE(P.organization_id=@org_id AND P.researcher_id=OLD.researcher_id)) 
OR EXISTS (SELECT count(A.r_id) as C FROM
(SELECT W.project_id as p_id, W.researcher_id as r_id from WORKS_ON W ) AS A
INNER JOIN 
(SELECT project_id as p_id FROM WORKS_ON WHERE researcher_id = OLD.researcher_id) AS B
ON A.p_id = B.p_id GROUP BY A.p_id HAVING C = 1))
THEN 
SIGNAL SQLSTATE '02000' SET MESSAGE_TEXT = 'Warning : Researcher is evaluator or scientific advisor or a single worker';
END IF;
END $$
DELIMITER ;;