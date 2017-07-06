					###Student Attendance Record I###

#You are given a string representing an attendance rec#ord for a student. The record only contains the following three characters:
#1.	'A' : Absent.
#2.	'L' : Late.
#3.	'P' : Present.
#A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
#You need to return whether the student could be rewarded according to his attendance record.
#Example 1:
#Input: "PPALLP"
#Output: True
#Example 2:
#Input: "PPALLL"
#Output: False

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('A') > 1 or "LLL" in s:
           return False
        else:
           return True	

