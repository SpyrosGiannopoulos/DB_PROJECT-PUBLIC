USE DB_PROJECT;


CREATE TABLE PROJECTS
(
	project_id int UNSIGNED NOT NULL AUTO_INCREMENT,
    title varchar(50)  NOT NULL,
    summary varchar(100) NOT NULL,
    funding DECIMAL(9,2) NOT NULL,
    start_date DATE NOT NULL,
    due_date DATE NOT NULL,
    PRIMARY KEY  (project_id)
);

CREATE TABLE RESEARCHERS
(
	researcher_id int UNSIGNED NOT NULL AUTO_INCREMENT,
    first_name varchar(45) NOT NULL,
    last_name varchar(45) NOT NULL,
    sex varchar(6) NOT NULL,
    date_of_birth DATE NOT NULL,
    PRIMARY KEY (researcher_id)
);

CREATE TABLE ORGANIZATIONS 
(
	organization_id int UNSIGNED NOT NULL AUTO_INCREMENT,
    org_name varchar(45) NOT NULL,
    city varchar(45) NOT NULL,
    street_name varchar(45) NOT NULL,
    street_number int unsigned NOT NULL,
    zip_code int(5) NOT NULL,
    abbreviation varchar(10) NOT NULL,
    PRIMARY KEY (organization_id)
);

CREATE TABLE PROGRAMS 
(
	program_id int UNSIGNED NOT NULL AUTO_INCREMENT,
    program_name varchar(45) NOT NULL,
    dept_name varchar(60) NOT NULL,
    PRIMARY KEY (program_id)
);

CREATE TABLE SCIENTIFIC_FIELDS 
(
	field_id int unsigned not null auto_increment,
    field_name varchar(45) NOT NULL,
    PRIMARY KEY(field_id)
);

CREATE TABLE EXECUTIVES 
(
	executive_id int UNSIGNED NOT NULL AUTO_INCREMENT,
    executive_first_name varchar(45) NOT NULL,
    executive_last_name varchar(45) NOT NULL,
    PRIMARY KEY (executive_id)
);

CREATE TABLE EVALUATIONS
(
	evaluation_id int UNSIGNED NOT NULL AUTO_INCREMENT,
    grade int(3) unsigned NOT NULL,
    evaluation_date DATE NOT NULL,
    PRIMARY KEY (evaluation_id)
);

ALTER TABLE PROJECTS
ADD program_id int UNSIGNED NOT NULL;

ALTER TABLE PROJECTS
ADD CONSTRAINT fk_PROJECTS_PROGRAMS FOREIGN KEY (program_id)
REFERENCES PROGRAMS (program_id) ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE PROJECTS
ADD executive_id int unsigned not null,
ADD CONSTRAINT fk_PROJECTS_EXECUTIVES FOREIGN KEY (executive_id)
REFERENCES EXECUTIVES(executive_id) ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE PROJECTS
ADD organization_id int unsigned not null,
ADD CONSTRAINT fk_PROJECTS_ORGANIZATIONS FOREIGN KEY (organization_id)
REFERENCES ORGANIZATIONS(organization_id) ON DELETE RESTRICT ON UPDATE CASCADE;

CREATE TABLE DELIVERABLES
(
	deliverable_id int unsigned not null,
    project_id int unsigned not null,
    title varchar(50) not null,
	summary varchar(100) not null,
    delivery_date date not null,
    PRIMARY KEY(deliverable_id,project_id)
);

ALTER TABLE DELIVERABLES
ADD CONSTRAINT fk_DELIVERABLES_PROJECTS FOREIGN KEY (project_id)
REFERENCES PROJECTS(project_id) ON DELETE RESTRICT ON UPDATE CASCADE;

CREATE TABLE UNIVERSITIES
(
	organization_id int unsigned not null,
    ministry_of_education DECIMAL(11,2) NOT NULL,
    PRIMARY KEY(organization_id)
);

ALTER TABLE UNIVERSITIES
ADD CONSTRAINT fk_UNIVERSITIES_ORGANIZATIONS FOREIGN KEY (organization_id)
REFERENCES ORGANIZATIONS(organization_id) ON DELETE RESTRICT ON UPDATE CASCADE;

CREATE TABLE COMPANIES
(
	organization_id int unsigned not null,
    own_funds DECIMAL(11,2) NOT NULL,
    PRIMARY KEY(organization_id)
);

ALTER TABLE COMPANIES
ADD CONSTRAINT fk_COMPANIES_ORGANIZATIONS FOREIGN KEY (organization_id)
REFERENCES ORGANIZATIONS(organization_id) ON DELETE RESTRICT ON UPDATE CASCADE;

CREATE TABLE RESEARCH_CENTRES
(
	organization_id int unsigned not null,
    ministry_of_education DECIMAL(11,2) NOT NULL,
    private_activities DECIMAL(11,2) NOT NULL,
    PRIMARY KEY(organization_id)
);

ALTER TABLE RESEARCH_CENTRES
ADD CONSTRAINT fk_RESEARCH_CENTRES_ORGANIZATIONS FOREIGN KEY (organization_id)
REFERENCES ORGANIZATIONS(organization_id) ON DELETE RESTRICT ON UPDATE CASCADE;

CREATE TABLE INST_PHONE 
(
	organization_id int unsigned not null,
    phone_number BIGINT unsigned not null,
    PRIMARY KEY(organization_id,phone_number)
);

ALTER TABLE INST_PHONE
ADD CONSTRAINT fk_INST_PHONE_ORGANIZATIONS FOREIGN KEY (organization_id)
REFERENCES ORGANIZATIONS(organization_id) ON DELETE RESTRICT ON UPDATE CASCADE;

CREATE TABLE DESCRIBES 
(
	description_id int unsigned not null auto_increment,
	field_id int unsigned not null,
    project_id int unsigned not null,
    PRIMARY KEY(description_id,field_id,project_id)
);

ALTER TABLE PROJECTS
ADD description_id int unsigned not null,
ADD CONSTRAINT fk_PROJECTS_DESCRIBES FOREIGN KEY (description_id)
REFERENCES DESCRIBES(description_id) ON DELETE RESTRICT ON UPDATE CASCADE;


ALTER TABLE DESCRIBES
ADD CONSTRAINT fk_DESCRIBES_PROJECTS FOREIGN KEY (project_id)
REFERENCES PROJECTS(project_id) ON DELETE RESTRICT ON UPDATE CASCADE;



ALTER TABLE DESCRIBES
ADD CONSTRAINT fk_DESCRIBES_SCIENTIFIC_FIELDS FOREIGN KEY (field_id)
REFERENCES scientific_fields(field_id) ON DELETE RESTRICT ON UPDATE CASCADE;



CREATE TABLE WORKS_ON
(
	worksON_id int unsigned not null auto_increment,
    project_id int unsigned not null,
    researcher_id int unsigned not null,
    PRIMARY KEY(worksON_id,project_id,researcher_id)
);

ALTER TABLE PROJECTS
ADD worksON_id int unsigned not null,
ADD CONSTRAINT fk_PROJECTS_WORKS_ON FOREIGN KEY (worksON_id)
REFERENCES WORKS_ON(worksON_id) ON DELETE RESTRICT ON UPDATE CASCADE;


ALTER TABLE WORKS_ON
ADD CONSTRAINT fk_WORKS_ON_REASEARCHERS FOREIGN KEY(researcher_id)
REFERENCES RESEARCHERS(researcher_id) ON DELETE RESTRICT ON UPDATE CASCADE,
ADD CONSTRAINT fk_WORKS_ON_PROJECTS FOREIGN KEY(project_id)
REFERENCES PROJECTS(project_id) ON DELETE RESTRICT ON UPDATE CASCADE;


ALTER TABLE RESEARCHERS
ADD organization_id int unsigned not null,
ADD date_of_recruitment date not null,
ADD CONSTRAINT fk_RESEARCHERS_ORGANIZATIONS FOREIGN KEY (organization_id)
REFERENCES ORGANIZATIONS(organization_id) ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE PROJECTS
ADD researcher_id int unsigned not null,
ADD CONSTRAINT fk_PROJECTS_RESEARCHERS FOREIGN KEY (researcher_id)
REFERENCES RESEARCHERS(researcher_id) ON DELETE RESTRICT ON UPDATE CASCADE,
ADD evaluation_id int unsigned not null,
ADD CONSTRAINT fk_PROJECTS_EVALUATIONS FOREIGN KEY (evaluation_id)
REFERENCES EVALUATIONS(evaluation_id) ON DELETE RESTRICT ON UPDATE CASCADE;

CREATE TABLE EVALUATES 
(
	evaluation_id int unsigned not null auto_increment,
    project_id int unsigned not null,
    researcher_id int unsigned not null,
    PRIMARY KEY(evaluation_id,project_id,researcher_id)
);


ALTER TABLE EVALUATES 
ADD CONSTRAINT fk_EVALUATES_EVALUATIONS FOREIGN KEY(evaluation_id)
REFERENCES EVALUATIONS(evaluation_id) ON DELETE RESTRICT ON UPDATE CASCADE,
ADD CONSTRAINT fk_EVALUATES_PROJECTS FOREIGN KEY(project_id)
REFERENCES PROJECTS(project_id) ON DELETE RESTRICT ON UPDATE CASCADE,
ADD CONSTRAINT fk_EVALUATES_RESEARCHERS FOREIGN KEY(researcher_id)
REFERENCES RESEARCHERS(researcher_id) ON DELETE RESTRICT ON UPDATE CASCADE


