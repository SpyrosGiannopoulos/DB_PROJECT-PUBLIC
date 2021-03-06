USE DB_PROJECT;

DROP VIEW IF EXISTS proj_org;
CREATE VIEW proj_org AS
 select p.project_id, o.organization_id, p.title, o.org_name 
 from projects p inner join organizations o on p.organization_id=o.organization_id
 order by o.organization_id;

select  org_name, title from proj_org