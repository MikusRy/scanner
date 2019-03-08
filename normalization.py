def normalize_x1(temp: list, span: int):
    master_position = 0
    compared_position = 0

    while compared_position < len(temp):
        if (temp[compared_position][0][0] - temp[master_position][0][0]) <= span:
            temp[compared_position][0][0] = temp[master_position][0][0]
            temp[compared_position][1][0] = temp[master_position][0][0]
            compared_position += 1
        else:
            master_position = compared_position
            temp[compared_position][0][0] = temp[compared_position][1][0]
            compared_position += 1
    return temp


def normalize_x2(temp: list, span: int):
    master_position = 0
    compared_position = 0

    while compared_position < len(temp):
        if (temp[compared_position][2][0] - temp[master_position][2][0]) <= span:
            temp[compared_position][2][0] = temp[master_position][2][0]
            temp[compared_position][3][0] = temp[master_position][2][0]
            compared_position += 1
        else:
            master_position = compared_position
            temp[compared_position][2][0] = temp[compared_position][3][0]
            compared_position += 1
    return temp


def normalize_y1(temp: list, span: int):
    master_position = 0
    compared_position = 0

    while compared_position < len(temp):
        if (temp[compared_position][0][1] - temp[master_position][0][1]) <= span:
            temp[compared_position][0][1] = temp[master_position][0][1]
            temp[compared_position][1][1] = temp[master_position][0][1]
            compared_position += 1
        else:
            master_position = compared_position
            temp[compared_position][0][1] = temp[compared_position][1][1]
            compared_position += 1
    return temp


def normalize_y2(temp: list, span: int):
    master_position = 0
    compared_position = 0

    while compared_position < len(temp):
        if (temp[compared_position][2][1] - temp[master_position][2][1]) <= span:
            temp[compared_position][2][1] = temp[master_position][2][1]
            temp[compared_position][3][1] = temp[master_position][2][1]
            compared_position += 1
        else:
            master_position = compared_position
            temp[compared_position][2][1] = temp[compared_position][3][1]
            compared_position += 1
    return temp


def normalize(temp: list, span: int):

    # Sort all points by Y
    for item in temp:
        item.sort(key=lambda x: x[1])
    # Sort all Y
    temp.sort(key=lambda x: x[0][1])

    temp = normalize_y1(temp, span)
    temp = normalize_y2(temp, span)

    for item in temp:
        item.sort(key=lambda x: x[0])

    temp.sort()
    temp = normalize_x1(temp, span)
    temp = normalize_x2(temp, span)

    return temp