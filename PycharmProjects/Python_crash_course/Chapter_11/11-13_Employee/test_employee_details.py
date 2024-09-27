from Employee_details import Employee

def test_give_default_raise():
    employee = Employee('John', 'Doe', 20_000)
    employee.give_raise()
    assert employee.pay == 25_000


def test_give_custom_raise():
    employee = Employee('Richard', 'Smith', 50_000)
    employee.give_raise(10_000)
    assert employee.pay == 60_000
