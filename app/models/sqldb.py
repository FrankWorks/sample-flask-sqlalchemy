import sys
# sys.path.append('./app/models')
import pyodbc
import users
import json
class UserList():

        
    connection_sring = ("Driver={SQL Server Native Client 11.0};"
                "Server=;"
                "Database=;"
                "Trusted_Connection=yes;")
    conn = pyodbc.connect(connection_sring)

    cursor = conn.cursor()
    # To retrieve the data from DB
    cursor.execute('select LogonName, FirstName, LastName, UpdatedBy, DateUpdated from tblEndUsers teu' )
    people = []
    for row in cursor:
        # From the retrieved data to Object List
        object = users.user(row.LogonName,row.FirstName,row.LastName,row.UpdatedBy, row.DateUpdated)
        # Object List to Dictionary
        people.append(object.dump())
    conn.close()
        # To Generate List to JSON
    def listUser(self):
        return json.dumps(UserList.people)
