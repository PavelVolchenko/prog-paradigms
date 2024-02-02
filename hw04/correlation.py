def average(array):
    return sum(array) / len(array)


def variance(array):
    return sum([(i - average(array)) ** 2 for i in array])


def covariance(array_1, array_2):
    return sum([(i - average(array_1)) * (j - average(array_2))
                for i, j in zip(array_1, array_2)])


def correlation(array_1, array_2):
    return covariance(array_1, array_2) / (
            variance(array_1) * variance(array_2)) ** 0.5


x = [2, 5, 7, 2, 8, 2, 6]
y = [4, 3, 2, 7, 4, 4, 2]

print(correlation(x, y))
