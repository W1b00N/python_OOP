# ClassInstanceVariable

# Class Variable คือ ตัวแปรที่ทำงานภายใน class
# ส่วนอื่นสามารถเข้าถึงข้อมูลส่วนนี้ได้เลย (static attribute)
# โดยไม่จำเป็นต้องสร้าง Object ขึ้นมา

# instance Variable คือ ตัวแปรที่อยู่ภายใน object
# สามารถเข้าถึงข้อมูลส่วนนี้โดยต้องสร้าง Object ขึ้นมา


class Employee:
    # class variable
    __minSalary = 12000
    __maxSalary = 50000
    _companyName = 'บริษัท XYZ จำกัด'

    def __init__(self, name, salary, department):
        # instance variable
        self.__name = name
        self.__salary = salary
        self.__department = department

    def _showData(self):
        print('ชื่อพนักงาน = {}'+self.__name)
        print('เงินเดือน = {}'+self.__salary)
        print('แผนก = {}'+self.__department)

emp1 = Employee('วิบูลย์', 50000, 'วิชาการ')
# print('เงินเดือนขั้นต่ำ = '+str(Employee.__minSalary))
print(Employee._companyName)