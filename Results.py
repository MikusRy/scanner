
def find(data: list, size: dict):
    found = False
    # [0] - X0 , [1] - Y0 , [2] - X1 , [3] - Y1
    area = []
    result = []

    for item in data:
        if not found:
            if int(0.35 * float(size['width'])) < max(item[0][0], item[1][0], item[2][0], item[3][0]) - min(item[0][0], item[1][0], item[2][0], item[3][0]) < int(0.7 * float(size['width'])) \
                    and max(item[0][1], item[1][1], item[2][1], item[3][1]) - min(item[0][1], item[1][1], item[2][1], item[3][1]) > int(0.6 * float(size['height'])):
                result.append(item)
                found = True
                area = [min(item[0][0], item[1][0], item[2][0], item[3][0]),
                        min(item[0][1], item[1][1], item[2][1], item[3][1]),
                        max(item[0][0], item[1][0], item[2][0], item[3][0]),
                        max(item[0][1], item[1][1], item[2][1], item[3][1])]
        else:
            if item[0][0] > item[1][0]:
                item[0][0], item[1][0] = item[1][0], item[0][0]
            if item[2][0] > item[3][0]:
                item[2][0], item[3][0] = item[3][0], item[2][0]

            if area[0] <= item[0][0] <= area[2] and area[1] <= item[0][1] <= area[3]:
                if (item[1][0] - item[0][0]) > 100 and (item[3][0] - item[2][0]) > 100 and (item[3][1] - item[2][1]) - (item[1][1] - item[0][1]) <= 20:
                    result.append(item)

    return result


def group(data: list, span: int = 15):

    result = {}
    question = 0
    y_temp = 0
    temp = []

    for i in range(1, len(data)-1):
        if y_temp == 0:
            y_temp = data[i][0][1]

        if data[i][0][1] - y_temp <= span:
            temp.append(data[i])
        else:
            if question == 0:
                temp = []
                question += 1
                y_temp = data[i][0][1]
                temp.append(data[i])
            else:
                result["q" + str(question)] = temp
                question += 1
                temp = []
                temp.append(data[i])
                y_temp = data[i][0][1]

        result["q" + str(question)] = temp

    return result


def contains(area: list, point: list):
    x0, x1, y0, y1 = 0, 0, 0, 0

    for item in area:
        if item[0] < x0 or x0 == 0:
            x0 = item[0]
        if item[0] > x1:
            x1 = item[0]

        if item[1] < y0 or y0 == 0:
            y0 = item[1]
        if item[1] > y1:
            y1 = item[1]

    return True if (x0 < point[0] <= x1) and (y0 < point[1] <= y1) else False


def evaluate(data: dict, handicap: int):
    results = {}

    for i in range(1, len(data)):
        # placeholders for answers
        results["q" + str(i)] = {'A': True,
                                 'B': True,
                                 'C': True,
                                 'D': True}

        # save answers data to temp value
        temp = data["q" + str(i)]
        temp.sort()
        # containers values of number and control block
        begin = temp[0]
        end = temp[len(temp)-1]
        # find width of answering area
        begin_x_max = max(begin[0][0], begin[1][0], begin[2][0], begin[3][0])
        end_x_min = min(end[0][0], end[1][0], end[2][0], end[3][0])
        # find y which should be always within question box
        y = (min(end[1][1], end[1][1], end[2][1], end[3][1]) + max(begin[0][1], begin[1][1], begin[2][1], begin[3][1])) // 2

        width = end_x_min - begin_x_max
        gap = width // 4

        current_x = begin_x_max + handicap

        for item in temp[1:-1]:
            if results["q" + str(i)]['A']:
                results["q" + str(i)]['A'] = not contains(item, [current_x, y])
            if results["q" + str(i)]['B']:
                results["q" + str(i)]['B'] = not contains(item, [current_x + gap, y])
            if results["q" + str(i)]['C']:
                results["q" + str(i)]['C'] = not contains(item, [current_x + (gap * 2), y])
            if results["q" + str(i)]['D']:
                results["q" + str(i)]['D'] = not contains(item, [current_x + (gap * 3), y])

    return results
