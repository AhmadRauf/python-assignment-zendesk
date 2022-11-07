import json


class Tickets:
    ticketsData = []
    filePath = ''

    def __init__(self, path):
        self.filePath = path

    def loadJsonFileData(self):
        f = open(self.filePath)
        self.ticketsData = json.load(f)

    def searchData(self, searchCriteria, field='_id'):
        found = False
        for record in self.ticketsData:
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
        record = self.ticketsData[0]
        for fields in record.keys():
            print(fields)

    def searchableFieldsCheck(self, searchField):
        record = self.ticketsData[0]
        for field in record.keys():
            if field == searchField:
                return True
        return False
