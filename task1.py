import random
import math


def generate_random_point(bounds):
    return [random.uniform(b[0], b[1]) for b in bounds]


# Визначення функції Сфери
def sphere_function(x):
    return sum(xi**2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current_solution = generate_random_point(bounds)
    current_value = func(current_solution)

    for _ in range(iterations):
        neighbor = [
            random.uniform(max(b[0], x - 0.1), min(b[1], x + 0.1))
            for x, b in zip(current_solution, bounds)
        ]
        neighbor_value = func(neighbor)

        if abs(neighbor_value - current_value) < epsilon:
            break

        if neighbor_value < current_value:
            current_solution, current_value = neighbor, neighbor_value

    return current_solution, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best_solution = generate_random_point(bounds)
    best_value = func(best_solution)

    for _ in range(iterations):
        candidate = generate_random_point(bounds)
        candidate_value = func(candidate)

        if abs(candidate_value - best_value) < epsilon:
            break

        if candidate_value < best_value:
            best_solution, best_value = candidate, candidate_value

    return best_solution, best_value


# Simulated Annealing
def simulated_annealing(
    func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6
):
    current_solution = generate_random_point(bounds)
    current_value = func(current_solution)

    for _ in range(iterations):
        neighbor = [
            random.uniform(max(b[0], x - 0.1), min(b[1], x + 0.1))
            for x, b in zip(current_solution, bounds)
        ]
        neighbor_value = func(neighbor)

        if abs(neighbor_value - current_value) < epsilon or temp < epsilon:
            break

        if neighbor_value < current_value or random.uniform(0, 1) < math.exp(
            (current_value - neighbor_value) / temp
        ):
            current_solution, current_value = neighbor, neighbor_value

        temp *= cooling_rate

    return current_solution, current_value


if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
