import matplotlib.pyplot as plt
import numpy as np

def analyze_convergence(generation_plot, end_time, improvement_threshold=0.5, stable_generations=50, num_generations=1000):
    """
    Analyzes the generation plot to determine the convergence generation and time to convergence.
    Prints the results directly.
    """
    for i in range(len(generation_plot) - stable_generations):
        recent_returns = generation_plot[i:i + stable_generations]
        improvement = (max(recent_returns) - min(recent_returns)) / max(recent_returns) * 100
        if improvement < improvement_threshold:
            convergence_generation = i + stable_generations
            time_to_convergence = end_time * (convergence_generation / num_generations)
            print(f"Convergence achieved at generation: {convergence_generation}")
            print(f"Time to convergence: {time_to_convergence:.2f} seconds")
            return

    print("Convergence not achieved within specified generations.")


def validate_and_plot(best_portfolio, generation_plot, num_months, title="Task 1", output_file="Task_1.png"):
    """
    Validates that each monthly allocation in the best portfolio sums to 1 and plots the best return over generations.

    """
    # Validate that each month's allocation sums to 1
    allocation_sums = [np.isclose(best_portfolio[month].sum(), 1) for month in range(num_months)]
    if all(allocation_sums):
        print("All monthly allocations sum to 1.")
    else:
        print("Error: Not all monthly allocations sum to 1.")

    # Plotting the best return over generations
    plt.plot(range(len(generation_plot)), generation_plot, label="Best Return")
    plt.xlabel("Generation")
    plt.ylabel("Best Return")
    plt.title(title)
    plt.legend()
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.show()