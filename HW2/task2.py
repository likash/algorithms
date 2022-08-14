# 10 25 15 40 | 3
def count_gifts(X, Y, Z, W):
    count = 0
    total = 0

    if W % X == 0:
        count += 1
    if W % Y == 0:
        count += 1
    if W % Z == 0:
        count += 1

    while total < W:
        total += X
        total_X = total

        if total < W:
            while total < W:
                total += Y
                total_Y = total

                if total == W:
                    count += 1
                elif total < W:
                    while total < W:
                        total += Z
                        if total == W:
                            count += 1
                    total = total_Y
            total = total_X

    total = 0
    while total < W:
        total += X
        total_X = total

        if total < W:
            while total < W:
                total += Z
                if total == W:
                    count += 1
            total = total_X

    total = 0
    while total < W:
        total += Y
        total_Y = total
        if total < W:
            while total < W:
                total += Z
                if total == W:
                    count += 1
            total = total_Y

    return count


if __name__ == '__main__':
    X = int(input().strip())
    Y = int(input().strip())
    Z = int(input().strip())
    W = int(input().strip())

    result = count_gifts(X, Y, Z, W)

    print(result)
