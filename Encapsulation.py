# Define Employee class with protected EmployeeID and private SSN properties
class Employee:
    def __init__(self):
        self._protectedEmployeeID = 0000
        self.__privateSSN = '555-55-5555'

    def getPrivate(self):
        print(self.__privateSSN)

    def setPrivate(self, private):
        self.__privateSSN = private

# Create employee 'Linda'
Linda = Employee()

# Set Linda's EmployeeID and SSN
Linda._protectedEmployeeID = 1234
Linda.setPrivate('123-45-6789')

# Display Linda's EmployeeID and SSN
print(Linda._protectedEmployeeID)
Linda.getPrivate()
