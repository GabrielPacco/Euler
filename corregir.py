for i in range(n - 1):
        h = x[i + 1] - x[i]
        k1 = h * f(x[i], y[i], x[i])
        l1 = h * g(x[i], y[i], x[i])
        k2 = h * f(x[i] + k1 / 2, y[i] + l1 / 2, x[i] + h / 2)
        l2 = h * g(x[i] + k1 / 2, y[i] + l1 / 2, x[i] + h / 2)
        k3 = h * f(x[i] + k2 / 2, y[i] + l2 / 2, x[i] + h / 2)
        l3 = h * g(x[i] + k2 / 2, y[i] + l2 / 2, x[i] + h / 2)
        k4 = h * f(x[i] + k3, y[i] + l3, x[i] + h)
        l4 = h * g(x[i] + k3, y[i] + l3, x[i] + h)
        x[i + 1] = x[i] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + 2 * k4)
        y[i + 1] = y[i] + (1 / 6) * (l1 + 2 * l2 + 2 * l3 + 2 * l4)