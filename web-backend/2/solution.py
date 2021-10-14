def solution(rows, columns, queries):
    answer = []

    array = [[0 for _ in range(columns)] for _ in range(rows)]
    comparison = [[0 for _ in range(columns)] for _ in range(rows)]

    for r in range(rows):
        for c in range(columns):
            comparison[r][c] = r*columns+c+1
            array[r][c] = r*columns+c+1

    for q in queries:
        temp = list()
        y_1, x_1, y_2, x_2 = q[0], q[1], q[2], q[3]
        comparison[y_1-1][x_1-1:x_2] = [comparison[y_1][x_1-1]]+comparison[y_1-1][x_1-1:x_2-1]
        temp.extend(comparison[y_1-1][x_1-1:x_2])
        comparison[y_1][x_2-1] = array[y_1-1][x_2-1]
        temp.append(comparison[y_1][x_2-1])
        for i in range(y_1+1, y_2):
            comparison[i][x_2-1] = array[i-1][x_2-1]
            temp.append(comparison[i][x_2-1])
        comparison[y_2-1][x_2-2] = array[y_2-1][x_2-1]
        temp.append(comparison[y_2-1][x_2-2])
        for i in range(x_2-2, x_1-2, -1):
            comparison[y_2-1][i] = array[y_2-1][i+1]
            temp.append(comparison[y_2-1][i])
        comparison[y_2-1][x_1-1] = array[y_2-1][x_1]
        temp.append(comparison[y_2-1][x_1-1])
        for i in range(y_2-2, y_1-1, -1):
            comparison[i][x_1-1] = array[i+1][x_1-1]
            temp.append(comparison[i][x_1-1])
        temp.sort()
        answer.append(temp[0])
        for i in range(rows):
            for j in range(columns):
                array[i][j] = comparison[i][j]

    return answer
