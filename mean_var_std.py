import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        flat_matrix = np.array(list)
        three_x_matrx = flat_matrix.reshape((3,3))

        mean_flat = float(flat_matrix.mean())
        mean_axis1 = [float(x) for x in three_x_matrx.mean(axis=1)]
        mean_axis2 = [float(x) for x in three_x_matrx.mean(axis=0)]

        var_flat = float(flat_matrix.var())
        var_axis1 = [float(x) for x in three_x_matrx.var(axis=1)]
        var_axis2 = [float(x) for x in three_x_matrx.var(axis=0)]

        std_flat = float(flat_matrix.std())
        std_axis1 = [float(x) for x in three_x_matrx.std(axis=1)]
        std_axis2 = [float(x) for x in three_x_matrx.std(axis=0)]

        max_flat = flat_matrix.max()
        max_axis1 = [x for x in three_x_matrx.max(axis=1)]
        max_axis2 = [x for x in three_x_matrx.max(axis=0)]

        min_flat = flat_matrix.min()
        min_axis1 = [x for x in three_x_matrx.min(axis=1)]
        min_axis2 = [x for x in three_x_matrx.min(axis=0)]

        sum_flat = flat_matrix.sum()
        sum_axis1 = [x for x in three_x_matrx.sum(axis=1)]
        sum_axis2 = [x for x in three_x_matrx.sum(axis=0)]

        calculations = {
            'mean': [mean_axis2, mean_axis1, mean_flat],
            'variance': [var_axis2, var_axis1, var_flat],
            'standard deviation': [std_axis2, std_axis1, std_flat],
            'max': [max_axis2, max_axis1, max_flat],
            'min': [min_axis2, min_axis1, min_flat],
            'sum': [sum_axis2, sum_axis1, sum_flat]
            }

    return calculations