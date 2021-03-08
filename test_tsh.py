import pytest


@pytest.mark.parametrize("first, last, age, gender, tsh_data, expected", [
                ('John', 'Doe', 32, 'Male', [3, 4, 5, 6], "hypothyroidism"),
                ('Amy', 'May', 3.5, 'Female', [9, 9, 9], "hypothyroidism"),
                ('John', 'May', 89, 'male', [0.1, 2, 3], "hyperthyroidism"),
                ('Amy', 'Doe', 28, 'Female', [0.1, 0.1], "hyperthyroidism"),
                ('Amy', 'Doe', 28, 'Female', [2, 3], "normal thyroid function")
                ])
def test_diagnoseTSH(first, last, age, gender, tsh_data, expected):
    from tsh import diagnoseTSH
    from tsh import create_patient

    patient = create_patient(first, last, age, gender, tsh_data)
    answer = diagnoseTSH(patient)
    assert answer == expected
