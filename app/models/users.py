class user:
    def __init__(self,login,FirstName,LastName,CreatedBy, UpdatedTime ):
        self.login = login
        self.FirstName = FirstName
        self.LastName = LastName
        self.CreatedBy = CreatedBy
        self.UpdatedTime = UpdatedTime
    def dump(self):
        # return {"UserList": {'LoginName': self.login,
        #                        'FirstName': self.FirstName,
        #                        'LastName': self.LastName,
        #                        'UpdatedBy': self.CreatedBy,
        #                        'DateUpdated': str(self.UpdatedTime)}}    
        return {'LoginName':self.login,
                               'FirstName':self.FirstName,
                               'LastName':self.LastName,
                               'UpdatedBy':self.CreatedBy,
                               'DateUpdated':str(self.UpdatedTime)}   