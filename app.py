import organization
import tickets
import users


class Application:

    def __init__(self):
        self.usersObj = users.Users('data/users.json')
        self.ticketsObj = tickets.Tickets('data/tickets.json')
        self.orgsObj = organization.Organizations('data/organizations.json')

    def loadData(self):
        self.usersObj.loadJsonFileData()
        self.ticketsObj.loadJsonFileData()
        self.orgsObj.loadJsonFileData()

    def searchUser(self, criteria):
        self.usersObj.searchData(criteria)


app = Application()
app.loadData()
print('***************     Welcom to Zendesk Search!     ***************')
print('Type "quit" anytime when you want to exit')
userNotQuiting = True
while userNotQuiting:
    print('\n\n\t\tSelect search option:')
    print('\t\tEnter 1 to search zendesk search')
    print('\t\tEnter 2 to view searchable fields')
    print('\t\tType "quit" to exit')
    userOption = input()
    if (not userOption.isdigit()) & (userOption != 'quit'):
        print('Invalid Option, Try Again!')
        continue
    if userOption.isdigit():
        userOption = int(userOption)
    if userOption == 1:
        userWantSearch = True
        while userWantSearch:
            print('Select 1) Users 2) Tickets 3) Organizations 0) Back ')
            userOptionSearch = input()
            if (not userOptionSearch.isdigit()) & (userOptionSearch != 'quit'):
                print('Invalid Option, Try Again!')
                continue
            if userOptionSearch.isdigit():
                userOptionSearch = int(userOptionSearch)
            if userOptionSearch == 1:
                searchMore = True
                while searchMore:
                    print('Enter search term')
                    userOptionSearchField = input()
                    while not app.usersObj.searchableFieldsCheck(userOptionSearchField):
                        print('Wrong option, Type 0 to go back or please try again:')
                        userOptionSearchField = input()
                    if userOptionSearchField == '0':
                        searchMore = False
                        continue
                    print('Enter search value')
                    userOptionSearchValue = input()
                    app.usersObj.searchData(userOptionSearchValue, userOptionSearchField)
                    print('Select 1) Search Again 0) Back')
                    userSearchPostOption = input()
                    if (not userSearchPostOption.isdigit()) & (userSearchPostOption != 'quit'):
                        print('Invalid Option, Try Again!')
                        continue
                    if userSearchPostOption.isdigit():
                        userSearchPostOption = int(userSearchPostOption)
                    if userSearchPostOption == 0:
                        searchMore = False
                    if userSearchPostOption == 'quit':
                        exit()

            if userOptionSearch == 2:
                searchMore = True
                while searchMore:
                    print('Enter search term')
                    ticketOptionSearchField = input()
                    while not app.ticketsObj.searchableFieldsCheck(ticketOptionSearchField):
                        print('Wrong option, Type 0 to go back or please try again:')
                        ticketOptionSearchField = input()
                    if ticketOptionSearchField == '0':
                        break
                    print('Enter search value')
                    ticketOptionSearchValue = input()
                    app.ticketsObj.searchData(ticketOptionSearchValue, ticketOptionSearchField)
                    print('Select 1) Search Again 0) Back')
                    ticketSearchPostOption = input()
                    if (not ticketSearchPostOption.isdigit()) & (ticketSearchPostOption != 'quit'):
                        print('Invalid Option, Try Again!')
                        continue
                    if ticketSearchPostOption.isdigit():
                        ticketSearchPostOption = int(ticketSearchPostOption)
                    if ticketSearchPostOption == 0:
                        break
                    if ticketSearchPostOption == 'quit':
                        exit()

            if userOptionSearch == 3:
                searchMore = True
                while searchMore:
                    print('Enter search term')
                    orgOptionSearchField = input()
                    while not app.orgsObj.searchableFieldsCheck(orgOptionSearchField):
                        print('Wrong option, Type 0 to go back or please try again:')
                        orgOptionSearchField = input()
                    if orgOptionSearchField == '0':
                        break
                    print('Enter search value')
                    orgOptionSearchValue = input()
                    app.orgsObj.searchData(orgOptionSearchValue, orgOptionSearchField)
                    print('Select 1) Search Again 0) Back')
                    orgSearchPostOption = input()
                    if (not orgSearchPostOption.isdigit()) & (orgSearchPostOption != 'quit'):
                        print('Invalid Option, Try Again!')
                        continue
                    if orgSearchPostOption.isdigit():
                        orgSearchPostOption = int(orgSearchPostOption)
                    if orgSearchPostOption == 0:
                        break
                    if orgSearchPostOption == 'quit':
                        exit()

            if userOptionSearch == 0:
                userWantSearch = False

            if userOptionSearch == 'quit':
                exit()

            if userOptionSearch not in [0, 1, 2, 3, 'quit']:
                print('Invalid Option, Try Again!')

    if userOption == 2:
        print('Search fields for User data:')
        print('----------------------------------')
        app.usersObj.searchableFields()
        print('\nSearch fields for Tickets data:')
        print('----------------------------------')
        app.ticketsObj.searchableFields()
        print('\nSearch fields for Organization data:')
        print('----------------------------------')
        app.orgsObj.searchableFields()

    if userOption == 'quit':
        exit()

    if userOption not in [1, 2, 'quit']:
        print('Invalid Option, Try Again!')
