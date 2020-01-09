class Contact:
    def __init__(self):
        self.Contactlist = []

    def addContact(self, name):
        self.Contactlist.append(name)

    def displayContact(self):
        for c in self.Contactlist:
            print(c, end=' ')

    def delete_Contact(self, name):
        for i in self.Contactlist:
            if (i == name):
                self.Contactlist.remove(name)
                print('DELETED NAME IS ', name)
                break
        else:
            print('element not present')


obj = Contact()
obj.addContact('naeem')
obj.addContact('ahmed')
obj.displayContact()

print(" ")

obj.delete_Contact('naeem')
obj.displayContact()
