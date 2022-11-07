import json


class Users:
    userData = []
    filePath = ''

    def __init__(self, path):
        self.filePath = path

    def loadJsonFileData(self):
        f = open(self.filePath)
        self.userData = json.load(f)

    def searchData(self, searchCriteria, field='_id'):
        found = False
        for record in self.userData:
            if type(record[field]) == int:
                searchCriteria = int(searchCriteria)
            if record[field] == searchCriteria:
                found = True
                for label, data in record.items():
                    print(str(label) + ':        ' + str(data))
                break
        if not found:
            print('No Results Found')

    def searchableFields(self):
        record = self.userData[0]
        for field in record.keys():
            print(field)

    def searchableFieldsCheck(self, searchField):
        record = self.userData[0]
        for field in record.keys():
            if field == searchField:
                return True
        return False

