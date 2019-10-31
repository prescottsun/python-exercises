class Person:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)
        
    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1

    def print_contact_info(self):
        print('%s\'s email: %s , %s\'s phone number: %s' %(self.name, self.email, self.name, self.phone))

    def add_friend(self, name):
        self.friends.append(name)

    def num_friends(self):
        print(len(self.friends))



sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)
print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)

sonny.print_contact_info()

jordan.add_friend(sonny)

jordan.num_friends()

print(sonny.greeting_count)

print(str(jordan))