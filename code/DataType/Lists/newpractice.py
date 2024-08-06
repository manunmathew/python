if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks.get(query_name)
    sum = 0
    for i in marks:
        sum += i
    x = sum / (len(marks))
    h = round(x, 2)
    print(f"{h:.2f}")
