from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='template')

app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = 'db_project'
app.config["MYSQL_HOST"] = 'localhost'


db = MySQL(app)
@app.route("/")
def index():
    print("Hi")
    return render_template('home_page.html')

@app.route("/ShowAllPrograms")
def ShowPrograms():
    try:
        mycursor = db.connection.cursor()
        query = "SELECT * FROM PROGRAMS;"
        mycursor.execute(query)
        col_names = [i[0] for i in mycursor.description]
        prog = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(prog)
        return render_template("ShowPrograms.html", programs = prog)
    except:
        return render_template("home_page.html")

@app.route("/ShowAllExecutives")
def ShowExecutives_1():
    try:
        mycursor = db.connection.cursor()
        query = "SELECT * FROM executives;"
        mycursor.execute(query)
        col_names = [i[0] for i in mycursor.description]
        exec = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(exec)
        return render_template("ShowExecutives.html", executives= exec)
    except:
        return render_template("home_page.html")


@app.route("/ShowAllOrganizations")
def ShowOrganizations():
    try:
        mycursor = db.connection.cursor()
        query = "SELECT * FROM ORGANIZATIONS;"
        mycursor.execute(query)
        col_names = [i[0] for i in mycursor.description]
        org = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(org)
        return render_template("ShowOrganizations.html", organizations= org)
    except:
        return render_template("home_page.html")

@app.route("/ShowAllFields")
def Show_Sci_Fields():
    try:
        mycursor = db.connection.cursor()
        query = "SELECT * FROM SCIENTIFIC_FIELDS;"
        mycursor.execute(query)
        col_names = [i[0] for i in mycursor.description]
        field = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(field)
        return render_template("ShowFields.html", fields= field)
    except:
        return render_template("home_page.html")

@app.route("/ShowAllResearchers")
def ShowResearchers():
    try:
        mycursor = db.connection.cursor()
        query = "SELECT * FROM RESEARCHERS;"
        mycursor.execute(query)
        col_names = [i[0] for i in mycursor.description]
        res = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(res)
        return render_template("ShowResearchers.html", researchers = res)
    except:
        return render_template("home_page.html")


@app.route("/ShowAllProjects")
def ShowProjects():
    try:
        mycursor = db.connection.cursor()
        query = "SELECT * FROM PROJECTS;"
        mycursor.execute(query)
        col_names = [i[0] for i in mycursor.description]
        proj = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(proj)
        return render_template("ShowProjects.html", projects = proj)
    except:
        return render_template("home_page.html")


@app.route("/First_Question")
def First_Question():
    return render_template('first_question.html')

@app.route("/First_Question/Programs")
def First_Question_Programs():
    mycursor = db.connection.cursor()
    query = "SELECT * FROM PROGRAMS;"
    mycursor.execute(query)
    col_names = [i[0] for i in mycursor.description]
    prog = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
    print(prog)
    return render_template('first_question_programs.html', programs = prog)

@app.route("/First_Question/Executives")
def ShowExecutives():
    try:
        mycursor = db.connection.cursor()
        query = "SELECT * FROM EXECUTIVES;"
        mycursor.execute(query)
        col_names = [i[0] for i in mycursor.description]
        exec = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(exec)
        return render_template("first_question_showExecutives.html", executives = exec)
    except:
        print("Error_exec")
        return render_template("home_page.html")

@app.route("/First_Question/Executives/Exec-Proj", methods = ['POST'])
def Show_Exec_proj():
    try:
        sel_exec = request.form['selected_executive']
        mycursor = db.connection.cursor()
        print(sel_exec)
        tuple_1= (sel_exec,)
        query = """SELECT project_id, title FROM PROJECTS WHERE executive_id = %s ORDER BY project_id ;"""
        mycursor.execute(query, tuple_1)
        col_names = [i[0] for i in mycursor.description]
        proj = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(proj)
        return render_template("first_question_showProjects.html",projects = proj)
    except:
        print("error_1")
        return render_template("home_page.html")

@app.route("/First_Question", methods=['POST'])
def pass_value():
    try:
        inp_date = request.form['user_date']
        if len(inp_date) != 0:
            print(inp_date)
            print(type(inp_date))
            mycursor = db.connection.cursor()
            query_1 = """SELECT project_id,title FROM PROJECTS WHERE (start_date < %s AND due_date > %s);"""
            tuple_1 = (inp_date,inp_date)
            mycursor.execute(query_1,tuple_1)
            col_names = [i[0] for i in mycursor.description]
            proj = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
            print(proj)
            return render_template('first_question_date.html', projects = proj, DATE = inp_date)

        inp_duration = request.form['duration']
        print(inp_duration)
        if(inp_duration=="one_year"):
            mycursor = db.connection.cursor()
            mycursor.callproc('31_duration', [2])
            col_names = [i[0] for i in mycursor.description]
            proj = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
            print(proj)
            return render_template('first_question_duration.html', projects=proj, DURATION=1)
        if (inp_duration == "two_year"):
            mycursor = db.connection.cursor()
            mycursor.callproc('31_duration', [3])
            col_names = [i[0] for i in mycursor.description]
            proj = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
            print(proj)
            return render_template('first_question_duration.html', projects=proj, DURATION=2)
        if (inp_duration == "three_year"):
            mycursor = db.connection.cursor()
            mycursor.callproc('31_duration', [4])
            col_names = [i[0] for i in mycursor.description]
            proj = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
            print(proj)
            return render_template('first_question_duration.html', projects=proj, DURATION=3)

    except :
        print("Error")
        return render_template('home_page.html')

@app.route("/First_Question/Researchers", methods=['POST'])
def Show_Researchers():
    try:
        sel_project = request.form['selected_project']
        print(sel_project)
        mycursor = db.connection.cursor()
        tuple_1=(sel_project,sel_project)
        query = """SELECT P.researcher_id, R.first_name,R.last_name FROM PROJECTS P INNER JOIN RESEARCHERS R WHERE (%s=P.project_id AND R.researcher_id=P.researcher_id) UNION SELECT R.researcher_id, R.first_name, R.last_name FROM RESEARCHERS R INNER JOIN WORKS_ON W ON (%s=W.project_id AND W.researcher_id=R.researcher_id) ;"""
        mycursor.execute(query, tuple_1)
        col_names = [i[0] for i in mycursor.description]
        res = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        return render_template("first_question_showResearchers.html", RESEARCHERS= res)
    except:
        print("Error")
        return render_template("home_page.html")


@app.route("/Second_Question/MENU")
def Choose_View():
    try:
        return render_template("second_question_menu.html")
    except :
        return render_template("home_page.html")


@app.route("/Second_Question/MENU/Proj_per_Res")
def First_View():
    try:
        mycursor = db.connection.cursor()
        mycursor.callproc('32_proj_research')
        col_names = [i[0] for i in mycursor.description]
        view_1 = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(view_1)
        return render_template("second_question_firstView.html", views = view_1)
    except:
        return render_template("home_page.html")


@app.route("/Second_Question/MENU/Proj_per_Org")
def Second_View():
    try :
        mycursor = db.connection.cursor()
        mycursor.callproc('32_proj_org')
        col_names = [i[0] for i in mycursor.description]
        view_2 = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(view_2)
        return render_template("second_question_secondView.html", views = view_2)
    except:
        print("Error rendering ! ")
        return render_template("home_page.html")


@app.route("/Third_Question")
def showScientific_Fields():
    try:
        mycursor = db.connection.cursor()
        query = "SELECT * FROM SCIENTIFIC_FIELDS ;"
        mycursor.execute(query)
        col_names = [i[0] for i in mycursor.description]
        fields = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(fields)
        return render_template("third_question_showFields.html", FIELDS = fields)
    except:
        print("Error executing third query")
        return render_template("home_page.html")


@app.route("/Third_Question/MENU", methods =['POST'])
def ShowMenu():
    try:
        sel_field = request.form['selected_field']
        return render_template('third_question_menu.html', FIELD = sel_field)
    except:
        return render_template("home_page.html")


@app.route("/Third_Question/MENU/ShowProjects", methods =['POST'])
def ShowProjects_Field():
    try:
        sel_field = request.form['selected_field']
        print(sel_field)
        mycursor = db.connection.cursor()
        query = """SELECT P.project_id, P.title FROM PROJECTS P INNER JOIN DESCRIBES D ON (P.project_id=D.project_id AND D.field_id=%s) WHERE (P.start_date<CURRENT_DATE() AND P.due_date>CURRENT_DATE()) ORDER BY p.project_id;"""
        tuple_1 = (sel_field,)
        mycursor.execute(query,tuple_1)
        col_names = [i[0] for i in mycursor.description]
        proj = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(proj)
        return render_template("third_question_showProjects.html", FIELD=sel_field, projects = proj)
    except:
        print("error_2")
        return render_template("home_page.html")


@app.route("/Third_Question/MENU/ShowResearchers", methods = ['POST'])
def showResearchers_Field():
    try:
        sel_field = request.form['selected_field']
        print(sel_field)
        mycursor = db.connection.cursor()
        query = """SELECT P.project_id, R.researcher_id, R.first_name, R.last_name FROM PROJECTS P INNER JOIN DESCRIBES D  ON (P.project_id=D.project_id AND D.field_id=%s) INNER JOIN RESEARCHERS R  ON P.researcher_id = R.researcher_id WHERE (P.start_date<CURRENT_DATE() AND P.due_date>CURRENT_DATE()) UNION SELECT P.project_id, R.researcher_id, R.first_name, R.last_name FROM PROJECTS P INNER JOIN DESCRIBES D  ON (P.project_id=D.project_id AND D.field_id=%s) INNER JOIN WORKS_ON W ON P.project_id=W.project_id INNER JOIN RESEARCHERS R  ON W.researcher_id=R.researcher_id WHERE (P.start_date<CURRENT_DATE() AND P.due_date>CURRENT_DATE()) Order by project_id;"""
        tuple_1 = (sel_field,sel_field)
        mycursor.execute(query,tuple_1)
        col_names = [i[0] for i in mycursor.description]
        res = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(res)
        return render_template("third_question_showResearchers.html", researchers = res, FIELD = sel_field)
    except:
        return render_template("home_page.html")

@app.route("/Fourth_Question")
def Choose_Number_of_Programs():
    try:
        return render_template("fourth_question_menu.html")
    except:
        return render_template("home_page.html")

@app.route("/Fourth_Question", methods = ['POST'])
def ShowFourthQuestion():
    try:
        inp_number_of_projects = request.form['user_number']
        print(inp_number_of_projects)
        mycursor = db.connection.cursor()
        mycursor.callproc('34_question', [inp_number_of_projects])
        col_names = [i[0] for i in mycursor.description]
        result = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(result)
        return render_template("fourth_question.html", results = result)
    except: return render_template("home_page.html")


@app.route("/Fifth_Question")
def Pairs_Scientific_fields():
    try:
        mycursor = db.connection.cursor()
        query = "select S.field_name as FieldA, F.field_name as FieldB, cust.counter from ( SELECT A.field_id as newField_A, B.field_id as newField_B ,B.project_id, count(*) as counter FROM DESCRIBES A INNER JOIN DESCRIBES B  ON (A.project_id = B.project_id AND  A.field_id<B.field_id AND A.description_id <> B.description_id) GROUP BY A.field_id, B.field_id ORDER BY counter DESC limit 3) cust inner join scientific_fields S on S.field_id= cust.newField_A inner join scientific_fields F on F.field_id=cust.newField_B #GROUP BY S.field_id, F.field_id  order by cust.counter DESC;"
        mycursor.execute(query)
        col_names = [i[0] for i in mycursor.description]
        result = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(result)
        return render_template("fifth_question.html", results = result)
    except:
        print("Error executing 5th query")
        return render_template("home_page.html")


@app.route("/Sixth_Question")
def Young_Researchers():
    try:
        mycursor = db.connection.cursor()
        query = "SELECT R.researcher_id, R.first_name, R.last_name, W.project_id, count(*) as project_count FROM RESEARCHERS R INNER JOIN WORKS_ON W ON (R.researcher_id = W.researcher_id AND DATE_SUB(R.date_of_birth,INTERVAL -40 YEAR)> CURRENT_DATE()) INNER JOIN PROJECTS P ON P.project_id=W.project_id and P.start_date<CURRENT_DATE() AND P.due_date>CURRENT_DATE() GROUP BY R.researcher_id UNION SELECT R.researcher_id, R.first_name, R.last_name , P.project_id, count(*) project_count FROM RESEARCHERS R INNER JOIN PROJECTS P ON R.researcher_id = P.researcher_id AND DATE_SUB(R.date_of_birth,INTERVAL -40 YEAR)> CURRENT_DATE() AND P.start_date<CURRENT_DATE() AND P.due_date>CURRENT_DATE() GROUP BY R.researcher_id ORDER BY project_count DESC , researcher_id ;"
        query_1 ="select cust.r_id, cust.r_fn, cust.r_ln, cust.r_pr, sum(cust.project_count) as s_pr from (SELECT R.researcher_id as r_id, R.first_name as r_fn, R.last_name as r_ln, W.project_id as r_pr, count(*) as project_count FROM RESEARCHERS R INNER JOIN WORKS_ON W ON (R.researcher_id = W.researcher_id AND  DATE_SUB(R.date_of_birth,INTERVAL -40 YEAR)> CURRENT_DATE()) INNER JOIN PROJECTS P ON P.project_id=W.project_id and P.start_date<CURRENT_DATE() AND P.due_date>CURRENT_DATE()  GROUP BY R.researcher_id  UNION SELECT R.researcher_id as r_id, R.first_name as r_fn, R.last_name as r_ln, P.project_id as r_pr, count(*) project_count FROM RESEARCHERS R INNER JOIN PROJECTS P ON R.researcher_id = P.researcher_id AND  DATE_SUB(R.date_of_birth,INTERVAL -40 YEAR)> CURRENT_DATE() AND P.start_date<CURRENT_DATE() AND P.due_date>CURRENT_DATE()  GROUP BY R.researcher_id ) as cust group by (cust.r_id) order BY s_pr DESC, r_id ;"
        mycursor.execute(query_1)
        col_names = [i[0] for i in mycursor.description]
        result = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(result)
        return render_template("sixth_question.html", results = result)
    except:
        print("Error executing 6th query")
        return render_template("home_page.html")

@app.route("/Seventh_Question")
def Top5Executives():
    try:
        mycursor = db.connection.cursor()
        query = "SELECT E.executive_id, E.executive_first_name, E.executive_last_name, O.org_name, SUM(P.funding) Total_funds FROM EXECUTIVES E INNER JOIN PROJECTS P ON E.executive_id = P.executive_id INNER JOIN ORGANIZATIONS O ON P.organization_id = O.organization_id INNER JOIN COMPANIES C ON C.organization_id=O.organization_id GROUP BY E.executive_id ORDER BY Total_funds DESC limit 5;"
        mycursor.execute(query)
        col_names = [i[0] for i in mycursor.description]
        exec = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(exec)
        return render_template("seventh_question.html", executives = exec)
    except:
        print("Error executing 7th query")
        return render_template("home_page.html")

@app.route("/Eighth_Question")
def Show_Researchers_deliverables():
    try:
        mycursor = db.connection.cursor()
        mycursor.callproc('38_question',[5])
        col_names = [i[0] for i in mycursor.description]
        res = [dict(zip(col_names, entry)) for entry in mycursor.fetchall()]
        print(res)
        return render_template("eighth_question.html", researchers = res)

    except:
        print("Error executing 8th query")
        return render_template("eighth_question.html")

@app.route("/Projects")
def Projects_Menu():
    try:
        return render_template("Projects_menu.html")
    except:
        return render_template("home_page.html")

@app.route("/Projects/Insert/Stage_1")
def Get_Deliverables_form():
    try:
        return render_template("ProjectsGetDeliverables.html")
    except :
        return render_template("home_page.html")

@app.route("/Projects/Insert/Stage_1", methods = ['POST'])
def Get_Deliverables():
    try:
        inp_del_number = request.form['user_del_number']
        global user_Deliverables
        user_Deliverables = inp_del_number
        print(inp_del_number)
        del_number = int(inp_del_number)
        a = [dict(zip("1","1")) for i in range (0,del_number)]
        print(a)
        return render_template("Project_Form.html", deliverables = a)
    except:
        return render_template("home_page.html")

@app.route("/Insert/Deliverables")
def Insert_Deliverables():
    try:
        return render_template("Deliverable_Form.html")
    except:
        return render_template("home_page.html")


Deliverables_queries=[]
number_of_Deliverables = 0
user_Deliverables =0

@app.route("/Insert/Deliverables", methods=['POST'])
def Insert_deliverables():
    try:
        inp_del_title=request.form['user_del_title']
        inp_del_summary = request.form['user_del_summary']
        inp_del_date = request.form['user_del_date']
        global Deliverables_queries, number_of_Deliverables, user_Deliverables
        Deliverables_queries.append(inp_del_title)
        Deliverables_queries.append(inp_del_summary)
        Deliverables_queries.append(inp_del_date)
        number_of_Deliverables = number_of_Deliverables + 1
        print(Deliverables_queries[number_of_Deliverables-1], number_of_Deliverables, int(user_Deliverables))
        a = [dict(zip("1", "1")) for i in range(number_of_Deliverables, int(user_Deliverables))]
        print(a)
        return render_template("Project_Form.html", deliverables = a)
    except:
        return render_template("home_page.html")


@app.route("/Projects/Insert", methods =['POST'])
def Retrieve_Data():
    try:
        global Deliverables_queries, number_of_Deliverables, user_Deliverables
        inp_title = request.form['user_title']
        print("Input title : "+ inp_title)
        inp_summary = request.form['user_summary']
        print("Input summary : " + inp_summary)
        inp_funding = request.form['user_funding']
        print("Input funding : " + inp_funding)
        inp_start_date = request.form['user_start_date']
        print("Input start date : " + inp_start_date)
        inp_due_date = request.form['user_due_date']
        print("Input due date : " + inp_due_date)
        inp_program_id = request.form['user_program_id']
        print("Input program_id : " + inp_program_id)
        inp_executive_id = request.form['user_executive_id']
        print("Input executive_id : " + inp_executive_id)
        inp_organization_id = request.form['user_organization_id']
        print("Input organization_id : " + inp_organization_id)
        inp_field_id = request.form['user_field_id']
        print("Input field_id : " + inp_field_id)
        inp_researcher_id = request.form['user_researcher_id']
        print("Input researcher_id : " + inp_researcher_id)
        inp_advisor_id = request.form['user_advisor_id']
        print("Input researcher_id of advisor : " + inp_advisor_id)
        inp_evaluator_id = request.form['user_evaluator_id']
        print("Input evaluator_id of evaluator : " + inp_evaluator_id)
        inp_eval_grade = request.form['user_eval_grade']
        print("Input evaluation grade : " + inp_eval_grade)
        inp_eval_date = request.form['user_eval_date']
        print("Input evaluation date : " + inp_eval_date)
        tuple_of_deliverables = request.form['number_of_del']
        print(tuple_of_deliverables)
        sequence_of_deliverables = len(tuple_of_deliverables)
        Number_of_deliverables = sequence_of_deliverables/12
        print(int(Number_of_deliverables))

        tuple(inp_researcher_id)
        tuple(inp_field_id)
        print(type(inp_eval_date), type(int(inp_eval_grade)))
        query = "SET FOREIGN_KEY_CHECKS = 0;"
        query_1 = """INSERT INTO evaluations VALUES((SELECT `AUTO_INCREMENT` FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND TABLE_NAME  = 'evaluates'),%s,%s);"""
        tuple_1 = (int(inp_eval_grade),inp_eval_date)
        mycursor = db.connection.cursor()
        mycursor.execute(query)
        mycursor.execute(query_1,tuple_1)
        query_2 = """INSERT INTO evaluates VALUES ((SELECT `AUTO_INCREMENT` FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'evaluates'),(SELECT `AUTO_INCREMENT` FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'projects'),%s);"""
        tuple_2 = (inp_evaluator_id,)
        mycursor.execute(query_2, tuple_2)
        print("Selected fields are :" + inp_field_id)
        tup_field_id = inp_field_id.split(",")
        tuple_field_id = tuple(tup_field_id)
        print(tuple_field_id)
        print(tuple_field_id[0])
        query_3 = """INSERT INTO describes (field_id,project_id) VALUES (%s,(SELECT `AUTO_INCREMENT` FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'projects'));"""
        for i in range(0,len(tuple_field_id)):
            #print(i)
            tuple_3 = (tuple_field_id[i],)
            mycursor.execute(query_3, tuple_3)
        tup_researcher_id = inp_researcher_id.split(",")
        tuple_researcher_id = tuple(tup_researcher_id)
        query_4 = """INSERT INTO works_on (project_id,researcher_id) VALUES ((SELECT `AUTO_INCREMENT` FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'projects'), %s);"""
        for i in range(0,len(tuple_researcher_id)):
            #print(i)
            tuple_4 = (tuple_researcher_id[i],)
            mycursor.execute(query_4, tuple_4)
        query_5 = """INSERT INTO deliverables VALUES (( select (case when not EXISTS  (select * from deliverables D where D.project_id=(SELECT `AUTO_INCREMENT`-1 FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'projects')) then 1 else (select count(*)+1 from deliverables D where D.project_id=(SELECT `AUTO_INCREMENT`-1 FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'projects')) end)),(SELECT `AUTO_INCREMENT`-1 FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'projects'),%s,%s,%s);"""
        #print("Size of list : " + str(len(Deliverables_queries)))
        #for i in range(0,len(Deliverables_queries),3):
        #    tuple_5 = (Deliverables_queries[i],Deliverables_queries[i+1],Deliverables_queries[i+2])
        #    print(tuple_5)
        #    mycursor.execute(query_5, tuple_5)

        #Deliverables_queries = []
        #number_of_Deliverables = 0
        #user_Deliverables = 0

        query_6 = """INSERT INTO projects VALUES ((SELECT `AUTO_INCREMENT` FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'projects'), %s, %s, %s, %s, %s, %s, %s, %s,(SELECT `AUTO_INCREMENT`-1 FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'describes'),(SELECT `AUTO_INCREMENT`-1 FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'works_on'), %s, (SELECT `AUTO_INCREMENT`-1 FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'evaluates'));"""
        tuple_6 =(inp_title,inp_summary,inp_funding,inp_start_date,inp_due_date,inp_program_id,inp_executive_id,inp_organization_id,inp_advisor_id)
        mycursor.execute(query_6,tuple_6)

        print("Size of list : " + str(len(Deliverables_queries)))
        for i in range(0, len(Deliverables_queries), 3):
            tuple_5 = (Deliverables_queries[i], Deliverables_queries[i + 1], Deliverables_queries[i + 2])
            print(tuple_5)
            mycursor.execute(query_5, tuple_5)

        Deliverables_queries = []
        number_of_Deliverables = 0
        user_Deliverables = 0

        db.connection.commit()

        print("Successfully inserted into Projects ")

        return render_template('SUCCESS.html')
    except Exception as e:
        print(e)
        Deliverables_queries = []
        number_of_Deliverables = 0
        user_Deliverables = 0
        print("User input for deliverables after failure " + str(user_Deliverables))
        print("Error inserting....")
        return render_template('FAILURE.html')


@app.route("/Projects/Update")
def Update_Project_menu():
    try:
        return render_template("Projects_Update_Form.html")
    except:
        return render_template("home_page.html")

@app.route("/Projects/Update/Alter_Dates")
def Alter_dates():
    try:
        return render_template("Project_Alter_Dates.html")
    except:
        return render_template("home_page.html")

@app.route("/Projects/Update/Alter_Dates", methods = ['POST'])
def Query_Alter_Dates():
    try:
        inp_project_id = request.form['user_project_id']
        inp_start_date = request.form['user_start_date']
        inp_due_date = request.form['user_due_date']
        query_1 = """UPDATE PROJECTS SET start_date = %s, due_date =%s WHERE project_id = %s;"""
        tuple_1 = (inp_start_date,inp_due_date,inp_project_id)
        mycursor = db.connection.cursor()
        mycursor.execute(query_1,tuple_1)
        db.connection.commit()
        return render_template("SUCCESS.html")
    except Exception as e:
        print(e)
        return render_template("FAILURE.html")

@app.route("/Projects/Update/Executive")
def Update_Project_Executive():
    try:
        return render_template("Project_Alter_Executive.html")
    except:
        return render_template("home_page.html")

@app.route("/Projects/Update/Executive", methods = ['POST'])
def Update_Executive():
    try:
        inp_project_id = request.form['user_project_id']
        inp_executive_id = request.form['user_executive_id']
        query_1 = """UPDATE PROJECTS SET executive_id = %s WHERE project_id = %s;"""
        tuple_1 = (inp_executive_id,inp_project_id)
        mycursor = db.connection.cursor()
        mycursor.execute(query_1, tuple_1)
        db.connection.commit()
        return render_template("SUCCESS.html")
    except Exception as e:
        return render_template("home_page.html")

@app.route("/Projects/Delete")
def Delete_Project_Form():
    try:
        return render_template("Project_Delete.html")
    except:
        return render_template("home_page.html")

@app.route("/Projects/Delete", methods = ['POST'])
def Delete_Project():
    try:
        inp_project_id = request.form['user_project_id']
        mycursor = db.connection.cursor()
        query = "SET FOREIGN_KEY_CHECKS = 0;"
        mycursor.execute(query)
        query_1 = """DELETE FROM WORKS_ON WHERE project_id = %s;"""
        tuple_1 = (inp_project_id,)
        mycursor.execute(query_1, tuple_1)
        query_2 = """DELETE FROM DESCRIBES WHERE project_id = %s;"""
        mycursor.execute(query_2, tuple_1)
        query_3 = """DELETE FROM EVALUATIONS WHERE evaluation_id = (SELECT evaluation_id FROM EVALUATES where project_id =%s);"""
        mycursor.execute(query_3, tuple_1)
        query_4 = """DELETE FROM EVALUATES WHERE project_id = %s;"""
        mycursor.execute(query_4, tuple_1)
        query_5 = """DELETE FROM DELIVERABLES WHERE project_id = %s;"""
        mycursor.execute(query_5, tuple_1)
        query_6 = """DELETE FROM PROJECTS WHERE project_id = %s;"""
        mycursor.execute(query_6, tuple_1)
        db.connection.commit()
        print("Successfully deleted project with id = "+ inp_project_id)
        return render_template("home_page.html")
    except Exception as e:
        print(e)
        return render_template("home_page.html")

@app.route("/Researchers")
def Researchers_Menu():
    try:
        return render_template("Researchers_menu.html")
    except:
        return render_template("home_page.html")

@app.route("/Researchers/Insert")
def Researchers_Form():
    try:
        return render_template("Researcher_Form.html")
    except:
        return render_template("home_page.html")

@app.route("/Researchers/Insert", methods = ['POST'])
def Retreive_Data():
    try:
        inp_first_name = request.form['user_first_name']
        inp_last_name = request.form['user_last_name']
        inp_sex = request.form['user_sex']
        inp_date_of_birth = request.form['user_date_of_birth']
        inp_org_id = request.form['user_organization_id']
        inp_date_of_recruitment = request.form['user_date_of_recruitment']
        print(inp_first_name,inp_last_name,inp_sex,inp_date_of_birth,inp_org_id,inp_date_of_recruitment)

        mycursor = db.connection.cursor()
        query_1 = """INSERT INTO RESEARCHERS VALUES ((SELECT AUTO_INCREMENT FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'researchers'),%s,%s,%s,%s,%s,%s);"""
        tuple_1 = (inp_first_name,inp_last_name,inp_sex,inp_date_of_birth,inp_org_id,inp_date_of_recruitment)
        mycursor.execute(query_1,tuple_1)
        db.connection.commit()
        print("Successful at inserting Researcher")

        return render_template("SUCCESS.html")
    except Exception as e :
        print(e)
        return render_template("FAILURE.html")

@app.route("/Researchers/Update")
def Researcher_Update_Menu():
    try:
        return render_template("Researchers_Update_menu.html")
    except:
        return render_template("home_page.html")

@app.route("/Researchers/Update/Project")
def Researcher_Project():
    try:
        return render_template("Researcher_Project_Form.html")
    except:
        return render_template("home_page.html")

@app.route("/Researchers/Update/Project", methods = ['POST'])
def Add_Relationship():
    try:
        inp_researcher_id = request.form['user_researcher_id']
        inp_project_id = request.form['user_project_id']
        query_1 = """INSERT INTO WORKS_ON VALUES ((SELECT AUTO_INCREMENT FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'works_on'),%s,%s);"""
        tuple_1 = (inp_project_id,inp_researcher_id)
        mycursor = db.connection.cursor()
        mycursor.execute(query_1,tuple_1)
        db.connection.commit()
        return render_template("SUCCESS.html")
    except Exception as e:
        print(e)
        return render_template("FAILURE.html")

@app.route("/Researchers/Update/Name")
def Update_Name():
    try:
        return render_template("Researchers_Update_name.html")
    except:
        return render_template("home_page.html")

@app.route("/Researchers/Update/Name", methods = ['POST'])
def Alter_name():
    try:
        inp_researcher_id = request.form['user_researcher_id']
        inp_new_Fname = request.form['user_first_name']
        inp_new_Lname = request.form['user_last_name']
        print(inp_new_Fname,inp_new_Lname,inp_researcher_id)
        query_1 = """UPDATE RESEARCHERS SET first_name = %s, last_name = %s WHERE researcher_id = %s;"""
        tuple_1 = (inp_new_Fname,inp_new_Lname,inp_researcher_id)
        mycursor = db.connection.cursor()
        mycursor.execute(query_1, tuple_1)
        db.connection.commit()
        return render_template("SUCCESS.html")
    except Exception as e:
        print(e)
        return render_template("FAILURE.html")


@app.route("/Researchers/Delete")
def Delete_Researcher():
    try:
        return render_template("Researcher_Delete_Form.html")
    except:
        return render_template("home_page.html")

@app.route("/Researchers/Delete", methods =['POST'])
def Script_Delete_Researcher():
    try:
        inp_researcher_id = request.form['user_researcher_id']
        query_1 = """DELETE FROM RESEARCHERS WHERE researcher_id = %s;"""
        tuple_1 = (inp_researcher_id,)
        mycursor = db.connection.cursor()
        query = "SET FOREIGN_KEY_CHECKS = 0;"
        mycursor.execute(query)
        mycursor.execute(query_1, tuple_1)
        query_2 = """DELETE FROM WORKS_ON WHERE researcher_id = %s """
        mycursor.execute(query_2,tuple_1)
        db.connection.commit()
        print("Deleted researcher")
        return render_template("home_page.html")
    except Exception as e:
        print(e)
        return render_template("home_page.html")

@app.route("/Executives")
def Executives_Menu():
    try:
        return render_template("Executives_menu.html")
    except:
        return render_template("home_page.html")


@app.route("/Executives/Insert")
def Executives_Form():
    try:
        return render_template("Executive_Form.html")
    except:
        return render_template("home_page.html")

@app.route("/Executives/Insert",methods = ['POST'])
def Insert_Executive():
    try:
        inp_first_name = request.form['user_first_name']
        inp_last_name = request.form['user_last_name']
        print(inp_first_name,inp_last_name)
        mycursor = db.connection.cursor()
        query_1 = """INSERT INTO EXECUTIVES VALUES ((SELECT AUTO_INCREMENT FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'executives'),%s,%s)"""
        tuple_1 = (inp_first_name,inp_last_name)
        mycursor.execute(query_1,tuple_1)
        db.connection.commit()
        return render_template("SUCCESS.html")
    except Exception as e:
        print(e)
        return render_template("FAILURE.html")

@app.route("/Programs")
def Programs_Menu():
    try:
        return render_template("Programs_menu.html")
    except:
        return render_template("home_page.html")

@app.route("/Programs/Insert")
def Programs_Form():
    try:
        return render_template("Program_Form.html")
    except:
        return render_template("home_page.html")

@app.route("/Programs/Insert", methods = ['POST'])
def Programs_Insert():
    try:
        inp_name = request.form['user_name']
        inp_dept_name = request.form['user_dept_name']
        print(inp_name,inp_dept_name)
        mycursor = db.connection.cursor()
        query_1 = """INSERT INTO PROGRAMS VALUES ((SELECT AUTO_INCREMENT FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'programs'),%s,%s)"""
        tuple_1 = (inp_name,inp_dept_name)
        mycursor.execute(query_1,tuple_1)
        db.connection.commit()
        return render_template("SUCCESS.html")
    except Exception as e:
        print(e)
        return render_template("FAILURE.html")


@app.route("/Fields")
def Fields_Menu():
    try:
        return render_template("Fields_menu.html")
    except:
        return render_template("home_page.html")

@app.route("/Fields/Insert")
def Fields_Form():
    try:
        return render_template("Field_Form.html")
    except:
        return render_template("home_page.html")

@app.route("/Fields/Insert", methods = ['POST'])
def Fied_Insert():
    try:
        inp_field_name = request.form['user_name']
        query_1 = """INSERT INTO SCIENTIFIC_FIELDS VALUES ((SELECT AUTO_INCREMENT FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'scientific_fields'),%s);"""
        tuple_1 = (inp_field_name,)
        mycursor = db.connection.cursor()
        mycursor.execute(query_1, tuple_1)
        print(inp_field_name)
        db.connection.commit()
        return render_template("SUCCESS.html")
    except Exception as e:
        print(e)
        return render_template("FAILURE.html")


@app.route("/Organizations")
def Organization_menu():
    try:
        return render_template("Organizations_menu.html")
    except:
        return render_template("home_page.html")

@app.route("/Organizations/Insert/SelectType")
def Choose_Type():
    try:
        return render_template("Organizations_choose_type.html")
    except:
        return render_template("home_page.html")


organization_type = ""

@app.route("/Organizations/Insert/SelectType", methods = ['POST'])
def Choose_Type_2():
    try:
        inp_org_type = request.form['Org_type']
        print(inp_org_type)
        global organization_type
        organization_type = inp_org_type
        if(organization_type =="University"):
            a = [dict(zip("1", "1")) for i in range(0, 1)]
        if(organization_type == "Research_Centre"):
            a = [dict(zip("1", "1")) for i in range(0, 2)]
        if(organization_type == "Company"):
            a = [dict(zip("1", "1")) for i in range(0, 3)]
        print(a)
        return render_template("Organization_Form.html", check_type=a)
    except Exception as e:
        print(e)
        return render_template("home_page.html")

@app.route("/Organizations/Insert",methods = ['POST'])
def Insert_Organizations():
    try:
        inp_name = request.form['user_name']
        inp_city = request.form['user_city']
        inp_street_name = request.form['user_street_name']
        inp_street_number = request.form['user_street_number']
        inp_zip_code = request.form['user_zip_code']
        inp_abbreviation = request.form['user_abbreviation']
        inp_phone_number = request.form['user_phone_number']
        mycursor = db.connection.cursor()
        mycursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        global organization_type
        if(organization_type =="University"):
            query_1 = """INSERT INTO UNIVERSITIES VALUES ((SELECT AUTO_INCREMENT FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'organizations'),%s)"""
            inp_uni_fund = request.form['user_uni_fund']
            tuple_1 = (inp_uni_fund,)
        if (organization_type == "Research_Centre"):
            query_1 = """INSERT INTO RESEARCH_CENTRES VALUES ((SELECT AUTO_INCREMENT FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'organizations'),%s,%s)"""
            inp_ministry_fund = request.form['user_ministry_fund']
            inp_private_fund = request.form['user_private_fund']
            tuple_1 = (inp_ministry_fund,inp_private_fund)
        if (organization_type == "Company"):
            query_1 = """INSERT INTO COMPANIES VALUES ((SELECT AUTO_INCREMENT FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'organizations'),%s)"""
            inp_own_funds = request.form['user_own_fund']
            tuple_1 = (inp_own_funds,)

        organization_type = ""
        mycursor.execute(query_1, tuple_1)
        tup_phone_number = inp_phone_number.split(",")
        tuple_phone_number = tuple(tup_phone_number)
        for i in range(0,len(tuple_phone_number)):
            print(i)
            query_2 = """INSERT INTO INST_PHONE VALUES ((SELECT AUTO_INCREMENT FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'organizations'),%s);"""
            tuple_2 = (tuple_phone_number[i],)
            print(tuple_phone_number[i])
            mycursor.execute(query_2,tuple_2)
        query_3 = """INSERT INTO ORGANIZATIONS VALUES ((SELECT AUTO_INCREMENT FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'db_project' AND  TABLE_NAME  = 'organizations'),%s,%s,%s,%s,%s,%s);"""
        tuple_3 = (inp_name,inp_city,inp_street_name,inp_street_number,inp_zip_code,inp_abbreviation)
        mycursor = db.connection.cursor()
        mycursor.execute(query_3, tuple_3)
        db.connection.commit()
        return render_template("SUCCESS.html")
    except Exception as e:
        print(e)
        return render_template("FAILURE.html")


@app.route("/Organizations/Update")
def Org_Update_Menu():
    try:
        return render_template("Organizations_Update_Menu.html")
    except:
        return render_template("home_page.html")

@app.route("/Organizations/Update/Name")
def Alter_Org_name():
    try:
        return render_template("Organization_Alter_Name.html")
    except:
        return render_template("home_page.html")

@app.route("/Organizations/Update/Name", methods= ['POST'])
def Script_alter_name():
    try:
        inp_org_id = request.form['user_org_id']
        inp_org_name = request.form['user_name']
        query_1 = """UPDATE ORGANIZATIONS SET org_name = %s WHERE organization_id = %s;"""
        tuple_1 = (inp_org_name,inp_org_id)
        mycursor = db.connection.cursor()
        mycursor.execute(query_1, tuple_1)
        db.connection.commit()
        return render_template("SUCCESS.html")
    except Exception as e:
        print(e)
        return render_template("home_page.html")

@app.route("/Organizations/Update/Location")
def Alter_Organization_Location():
    try:
        return render_template("Organizations_Alter_Location.html")
    except :
        return render_template("home_page.html")

@app.route("/Organizations/Update/Location", methods = ['POST'])
def Alter_location_script():
    try:
        inp_org_id = request.form['user_org_id']
        inp_city = request.form['user_city']
        inp_street_name = request.form['user_street_name']
        inp_street_number = request.form['user_street_number']
        inp_zip_code = request.form['user_zip_code']
        query_1 = """UPDATE ORGANIZATIONS SET city = %s, street_name = %s, street_number = %s, zip_code = %s WHERE organization_id = %s; """
        tuple_1 =(inp_city,inp_street_name,inp_street_number,inp_zip_code,inp_org_id)
        mycursor = db.connection.cursor()
        mycursor.execute(query_1, tuple_1)
        db.connection.commit()
        return render_template("SUCCESS.html")
    except Exception as e:
        print(e)
        return render_template("home_page.html")

if __name__ == '__main__':
    app.run(debug=True, host = "localhost", port = 3000)
