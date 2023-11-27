import devops_lab2.main as bmi

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.73,57)
    assert(result == 0)

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.73,100000)
    assert(result == 1)

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.73,1)
    assert(result == -1)

#test