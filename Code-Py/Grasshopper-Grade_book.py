<<<<<<< HEAD
'''

Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

'''
#
#
#
import statistics as st
def get_grade(s1, s2, s3):
    score = st.mean([s1, s2, s3])
    if 90 <= score <= 100: return 'A'
    elif 80 <= score < 90: return 'B'
    elif 70 <= score < 80: return 'C'
    elif 60 <= score < 70: return 'D'
    else: return 'F'
# the mean() has only 1 args, so you need to put variables in a list
=======
'''

Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

'''
#
#
#
import statistics as st
def get_grade(s1, s2, s3):
    score = st.mean([s1, s2, s3])
    if 90 <= score <= 100: return 'A'
    elif 80 <= score < 90: return 'B'
    elif 70 <= score < 80: return 'C'
    elif 60 <= score < 70: return 'D'
    else: return 'F'
# the mean() has only 1 args, so you need to put variables in a list
>>>>>>> refs/remotes/origin/main
#