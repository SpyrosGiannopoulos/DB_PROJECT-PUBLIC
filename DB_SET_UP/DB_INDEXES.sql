USE DB_PROJECT;

CREATE INDEX idx_start_date ON PROJECTS(start_date);
CREATE INDEX idx_due_date ON PROJECTS(due_date);
CREATE INDEX idx_title ON PROJECTS(title);
CREATE INDEX idx_first_name ON RESEARCHERS(first_name);
CREATE INDEX idx_last_name ON RESEARCHERS(last_name);

#SHOW INDEX FROM PROJECTS;
