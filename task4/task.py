import csv
import numpy as np


input = '''Возрастная группа;Электроника;Одежда;Книги;Обувь
18-24;20;15;10;5
25-34;30;20;15;10
35-44;25;25;20;15
45-54;20;20;25;20
55 плюс;15;15;30;25'''


def solve(data: np.array):
    row_sums = np.sum(data, axis=1)
    total_sum = np.sum(row_sums)

    prob_matrix = np.zeros_like(data, dtype=float)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            prob_matrix[i, j] = data[i, j] / total_sum if total_sum != 0 else 0

    p_a = np.sum(prob_matrix, axis=1)
    p_b = np.sum(prob_matrix, axis=0)
    
    h_ab = -np.sum(prob_matrix[prob_matrix > 0] * np.log2(prob_matrix[prob_matrix > 0]))
    h_a = -np.sum(p_a[p_a > 0] * np.log2(p_a[p_a > 0]))
    h_b = -np.sum(p_b[p_b > 0] * np.log2(p_b[p_b > 0]))

    h_b_a = h_ab - h_a
    i_b_a = h_b - h_b_a
    return np.array([h_ab, h_a, h_b, h_b_a, i_b_a])


def main(input):
    parser = csv.reader(input.strip().splitlines()[1:], delimiter=";")
    data = np.array([list(map(int, row[1:])) for row in parser])
    result = solve(data)
    print(result)
    
if __name__ == "__main__":
    main(input)