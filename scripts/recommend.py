import psycopg2

from config import db


def get_category_by_role(role_uuid, connection):
    cursor = connection.cursor()
    cursor.execute(
    f"""
    select category_uuid from (select category_uuid, COUNT(role_uuid) as cnt 
    from project join lineup on lineup.project_uuid = project.uuid 
where role_uuid = '{role_uuid}' group by category_uuid order by cnt desc  ) as foo
    """)

    project_list = cursor.fetchall()
    if (len(project_list) == 0):
        cursor.execute(
        f"""select uuid from category;""")

        project_list = cursor.fetchall()

    print(project_list)
    return project_list

def get_role_by_project_uuid(project_uuid, connection):
    cursor = connection.cursor()
    cursor.execute(
    f"""select distinct * from (select lineup.role_uuid from project join
        (select category_uuid
        from project  
        where project.uuid = '{project_uuid}') as ctg 
        on
        project.category_uuid = ctg.category_uuid 
        join lineup on project.uuid = lineup.project_uuid
        where project.uuid <> '{project_uuid}'
        ) as foo""")

    project_list = cursor.fetchall()
    if (len(project_list) == 0):
        cursor.execute(
        f"""select uuid from public.role;""")

        project_list = cursor.fetchall()

    print(project_list)
    return project_list


def get_role_by_project_uuid(project_uuid, connection):
    cursor = connection.cursor()
    cursor.execute(
    f"""select distinct * from (select lineup.role_uuid from project join
        (select category_uuid
        from project  
        where project.uuid = '{project_uuid}') as ctg 
        on
        project.category_uuid = ctg.category_uuid 
        join lineup on project.uuid = lineup.project_uuid
        where project.uuid <> '{project_uuid}'
        ) as foo""")

    project_list = cursor.fetchall()
    if (len(project_list) == 0):
        cursor.execute(
        f"""select uuid from public.role;""")

        project_list = cursor.fetchall()

    print(project_list)
    return project_list

def get_projects_by_user_uuid(user_uuid, connection ):
    cursor = connection.cursor()
    cursor.execute(
    f"""select project_uuid from profile join public.role on profile.specialization_uuid = public.role.specialization_uuid join
    (SELECT project.uuid as project_uuid, role_uuid 
     from project join lineup on lineup.project_uuid = project.uuid 
     where profile_uuid IS NULL) as lineup_needs on public.role.uuid = lineup_needs.role_uuid where user_uuid = '{user_uuid}';""")

    project_list = cursor.fetchall()
    if (len(project_list) == 0):
        cursor.execute(
        f"""SELECT project.uuid as project_uuid 
                 from project join lineup on lineup.project_uuid = project.uuid 
                 where profile_uuid IS NULL;""")

        project_list = cursor.fetchall()

    print(project_list)
    return project_list


def get_user_uuid_by_project_uuid(project_uuid, connection ):
    cursor = connection.cursor()
    cursor.execute(
    f"""select user_uuid from 
        (select user_uuid, public.role.uuid as role_uuid from profile join public.role ON profile.specialization_uuid = public.role.specialization_uuid) as tb1
        join
        (select project_uuid, role_uuid from project join lineup on project.uuid = lineup.project_uuid where public.lineup.profile_uuid is NULL) as tb2
        on
        tb1.role_uuid = tb2.role_uuid
        where
        project_uuid = '{project_uuid}';""")

    project_list = cursor.fetchall()

    if (len(project_list) == 0):
        cursor.execute(
            f"""select user_uuid from profile;""")

        project_list = cursor.fetchall()


    print(project_list)
    return project_list