'''The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
Example 
 
 
 

The query_name is 'beta'. beta's average score is .
Input Format
The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.
Constraints



Output Format
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg=student_marks[query_name][0]+student_marks[query_name][1]+student_marks[query_name][2]
    avg1=avg/3
    print("%.2f" % avg1);
    
