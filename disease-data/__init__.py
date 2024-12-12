import check50
from re import escape


@check50.check()
def exists():
    """data_analysis.py exists"""
    check50.exists("data_analysis.py")
    check50.include("testing.py")
    check50.include("disease1.txt")
    check50.include("disease2.txt")


@check50.check(exists)
def test_load_data():
    """load_data successfully parses disease1.txt and disease2.txt"""
    disease1_expected = {'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]}
    disease2_expected = {'Hogwarts': [5, 12, 18, 29, 33, 34, 34], 'Alderaan': [100, 200, 300, 400, 500, 600, 700], "Helm's Deep": [2, 3, 3, 5, 7, 7, 8], 'Mordor': [247, 448, 937, 1370, 2109, 3720, 5268], 'Shire': [1, 1, 1, 1, 1, 1, 1], 'Diagon Alley': [14, 28, 47, 72, 89, 97, 102]}
    tests = { "disease1.txt": disease1_expected, "disease2.txt": disease2_expected }
    for filename, expected_output in tests.items():
        # Run the student's program
        output = check50.run("python3 testing.py load_data").stdin(filename, prompt=True).stdout()
        
        # Convert actual output to a Python dictionary
        try:
            actual_output = eval(output.strip())
        except Exception as e:
            raise check50.Failure(f"Program output could not be parsed as a dictionary. Exception: {e} \nDid you remove all of your print statements?")
        
        # Compare the dictionaries directly
        if actual_output != expected_output:
            raise check50.Failure(
                f"Expected {expected_output},\n but got {actual_output}"
            )

@check50.check(test_load_data)
def test_daily_cases():
    """daily_cases successfully changes the cumulative values to daily new cases"""
    disease1_expected = {'Evermore': [1, 0, 0, 0, 0, 0, 0], 'Vanguard City': [1, 1, 1, 1, 1, 1, 1], 'Excelsior': [1, 0, 1, 1, 2, 3, 5]}
    disease2_expected = {'Hogwarts': [5, 7, 6, 11, 4, 1, 0], 'Alderaan': [100, 100, 100, 100, 100, 100, 100], "Helm's Deep": [2, 1, 0, 2, 2, 0, 1], 'Mordor': [247, 201, 489, 433, 739, 1611, 1548], 'Shire': [1, 0, 0, 0, 0, 0, 0], 'Diagon Alley': [14, 14, 19, 25, 17, 8, 5]}
    tests = { "disease1.txt": disease1_expected, "disease2.txt": disease2_expected }
    for filename, expected_output in tests.items():
        # Run the student's program
        output = check50.run("python3 testing.py daily_cases").stdin(filename, prompt=True).stdout()
        
        # Convert actual output to a Python dictionary
        try:
            actual_output = eval(output.strip())
        except Exception as e:
            raise check50.Failure(f"Program output could not be parsed as a dictionary. Exception: {e} \nDid you remove all of your print statements?")
        
        # Compare the dictionaries directly
        if actual_output != expected_output:
            raise check50.Failure(
                f"Expected {expected_output},\n but got {actual_output}"
            )


# Test locally in a directory with data_analysis.py
# check50 --dev ~/code/mrsharp-check50/disease-data

# reference:
# https://github.com/cs50/problems/blob/2022/python/meal/__init__.py
# https://cs50.readthedocs.io/projects/check50/en/latest/check_writer/#check-writer