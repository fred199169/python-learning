# -*- coding: UTF-8 -*-
# !/usr/bin/python


class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


tom = Employee("tom", 100)
tom1 = Employee("tom1", 100)
tom2 = Employee("tom2", 100)
tom3 = Employee("tom3", 100)

print Employee.empCount
tom.displayEmployee()
