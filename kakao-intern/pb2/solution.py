def solution(places):
    answer = []

    move_pos = [(-1, 0), (-2, 0), (-1, -1), (0, -1), (0, -2), (1, 0), (2, 0), (1, 1),
                (0, 1), (0, 2), (1, -1), (-1, 1)]

    sit_person_pos = [[] for _ in range(len(places))]

    for idx, p in enumerate(places):
        for i in range(len(p)):
            for j in range(len(p)):
                if p[i][j] == "P":
                    sit_person_pos[idx].append((i, j))

    for idx, person in enumerate(sit_person_pos):
        check = True
        for p in person:
            y, x = p
            for dx, dy in move_pos:
                if -1 < x+dx < 5 and -1 < y+dy < 5:
                    if places[idx][y+dy][x+dx] == "P":
                        if abs(dx-dy) == 1:
                            check = False
                            print(idx, dx, dy, x, y)
                            break
                        if dy == 0 and dx == -2:
                            if places[idx][y][x-1] == "X":
                                continue
                            check = False
                            continue
                        if dy == 0 and dx == 2:
                            if places[idx][y][x+1] == "X":
                                continue
                            check = False
                            break

                        if dy == 2 and dx == 0:
                            if places[idx][y+1][x] == "X":
                                continue
                            check = False
                            break

                        if dy == -2 and dx == 0:
                            if places[idx][y-1][x] == "X":
                                continue
                            check = False
                            break

                        if dy == -1 and dx == -1:
                            if places[idx][y][x-1] == "X" and places[idx][y-1][x] == "X":
                                continue
                            check = False
                            break

                        if dy == 1 and dx == 1:
                            if places[idx][y][x+1] == "X" and places[idx][y+1][x] == "X":
                                continue
                            check = False
                            break

                        if dy == -1 and dx == 1:
                            if places[idx][y][x+1] == "X" and places[idx][y-1][x] == "X":
                                continue
                            check = False
                            break

                        if dy == 1 and dx == -1:
                            if places[idx][y][x-1] == "X" and places[idx][y+1][x] == "X":
                                continue
                            check = False
                            break

            if not check:
                break
        if not check:
            answer.append(0)
            continue
        answer.append(1)

    return answer
