""" Unit tests for algorithms.py"""

# Author: Genevieve Hayes
# License: BSD 3 clause

<<<<<<< HEAD
try:
    import mlrose_hiive
except:
    import sys
    sys.path.append("..")
import unittest
import numpy as np
from mlrose_hiive import (OneMax, DiscreteOpt, ContinuousOpt, hill_climb,
                          random_hill_climb, simulated_annealing, genetic_alg,
                          mimic)
=======
import unittest
import numpy as np
from mlrose import (OneMax, DiscreteOpt, ContinuousOpt, hill_climb,
                    random_hill_climb, simulated_annealing, genetic_alg,
                    mimic)
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd


class TestAlgorithms(unittest.TestCase):
    """Tests for optimization algorithms."""

    @staticmethod
<<<<<<< HEAD
    def test_mimic_discrete_max():
        """Test mimic function for a discrete maximization problem"""

        problem = DiscreteOpt(5, OneMax(), maximize=True)
        best_state, best_fitness, _ = mimic(problem, max_attempts=50)

        x = np.array([1, 1, 1, 1, 1])

        assert (np.array_equal(best_state, x) and best_fitness == 5)

    @staticmethod
    def test_mimic_discrete_min():
        """Test mimic function for a discrete minimization problem"""

        problem = DiscreteOpt(5, OneMax(), maximize=False)
        best_state, best_fitness, _ = mimic(problem, max_attempts=50)

        x = np.array([0, 0, 0, 0, 0])

        assert (np.array_equal(best_state, x) and best_fitness == 0)

    @staticmethod
=======
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd
    def test_hill_climb_discrete_max():
        """Test hill_climb function for a discrete maximization problem"""

        problem = DiscreteOpt(5, OneMax(), maximize=True)
<<<<<<< HEAD
        best_state, best_fitness, _ = hill_climb(problem, restarts=20)
=======
        best_state, best_fitness = hill_climb(problem, restarts=20)
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd

        x = np.array([1, 1, 1, 1, 1])

        assert (np.array_equal(best_state, x) and best_fitness == 5)

    @staticmethod
    def test_hill_climb_continuous_max():
        """Test hill_climb function for a continuous maximization problem"""

        problem = ContinuousOpt(5, OneMax(), maximize=True)
<<<<<<< HEAD
        best_state, best_fitness, _ = hill_climb(problem, restarts=20)
=======
        best_state, best_fitness = hill_climb(problem, restarts=20)
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd

        x = np.array([1, 1, 1, 1, 1])

        assert (np.array_equal(best_state, x) and best_fitness == 5)

    @staticmethod
    def test_hill_climb_discrete_min():
        """Test hill_climb function for a discrete minimization problem"""

        problem = DiscreteOpt(5, OneMax(), maximize=False)
<<<<<<< HEAD
        best_state, best_fitness, _ = hill_climb(problem, restarts=20)
=======
        best_state, best_fitness = hill_climb(problem, restarts=20)
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd

        x = np.array([0, 0, 0, 0, 0])

        assert (np.array_equal(best_state, x) and best_fitness == 0)

    @staticmethod
    def test_hill_climb_continuous_min():
        """Test hill_climb function for a continuous minimization problem"""

        problem = ContinuousOpt(5, OneMax(), maximize=False)
<<<<<<< HEAD
        best_state, best_fitness, _ = hill_climb(problem, restarts=20)
=======
        best_state, best_fitness = hill_climb(problem, restarts=20)
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd

        x = np.array([0, 0, 0, 0, 0])

        assert (np.array_equal(best_state, x) and best_fitness == 0)

    @staticmethod
    def test_hill_climb_max_iters():
        """Test hill_climb function with max_iters less than infinite"""

        problem = DiscreteOpt(5, OneMax(), maximize=True)
        x = np.array([0, 0, 0, 0, 0])

<<<<<<< HEAD
        best_state, best_fitness, _ = hill_climb(problem, max_iters=1,
=======
        best_state, best_fitness = hill_climb(problem, max_iters=1,
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd
                                              restarts=0, init_state=x)

        assert best_fitness == 1

    @staticmethod
    def test_random_hill_climb_discrete_max():
        """Test random_hill_climb function for a discrete maximization
        problem"""

        problem = DiscreteOpt(5, OneMax(), maximize=True)
<<<<<<< HEAD
        best_state, best_fitness, _ = random_hill_climb(problem, max_attempts=10,
=======
        best_state, best_fitness = random_hill_climb(problem, max_attempts=10,
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd
                                                     restarts=20)

        x = np.array([1, 1, 1, 1, 1])

        assert (np.array_equal(best_state, x) and best_fitness == 5)

    @staticmethod
    def test_random_hill_climb_continuous_max():
        """Test random_hill_climb function for a continuous maximization
        problem"""

        problem = ContinuousOpt(5, OneMax(), maximize=True)
<<<<<<< HEAD
        best_state, best_fitness, _ = random_hill_climb(problem, max_attempts=10,
=======
        best_state, best_fitness = random_hill_climb(problem, max_attempts=10,
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd
                                                     restarts=20)

        x = np.array([1, 1, 1, 1, 1])

        assert (np.array_equal(best_state, x) and best_fitness == 5)

    @staticmethod
    def test_random_hill_climb_discrete_min():
        """Test random_hill_climb function for a discrete minimization
        problem"""

        problem = DiscreteOpt(5, OneMax(), maximize=False)
<<<<<<< HEAD
        best_state, best_fitness, _ = random_hill_climb(problem, max_attempts=10,
=======
        best_state, best_fitness = random_hill_climb(problem, max_attempts=10,
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd
                                                     restarts=20)

        x = np.array([0, 0, 0, 0, 0])

        assert (np.array_equal(best_state, x) and best_fitness == 0)

    @staticmethod
    def test_random_hill_climb_continuous_min():
        """Test random_hill_climb function for a continuous minimization
        problem"""

        problem = ContinuousOpt(5, OneMax(), maximize=False)
<<<<<<< HEAD
        best_state, best_fitness, _ = random_hill_climb(problem, max_attempts=10,
=======
        best_state, best_fitness = random_hill_climb(problem, max_attempts=10,
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd
                                                     restarts=20)

        x = np.array([0, 0, 0, 0, 0])

        assert (np.array_equal(best_state, x) and best_fitness == 0)

    @staticmethod
    def test_random_hill_climb_max_iters():
        """Test random_hill_climb function with max_iters less than infinite"""

        problem = DiscreteOpt(5, OneMax(), maximize=True)
        x = np.array([0, 0, 0, 0, 0])

<<<<<<< HEAD
        best_state, best_fitness, _ = random_hill_climb(problem, max_attempts=1,
=======
        best_state, best_fitness = random_hill_climb(problem, max_attempts=1,
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd
                                                     max_iters=1, restarts=0,
                                                     init_state=x)

        assert best_fitness == 1

    @staticmethod
    def test_simulated_annealing_discrete_max():
        """Test simulated_annealing function for a discrete maximization
        problem"""

        problem = DiscreteOpt(5, OneMax(), maximize=True)
<<<<<<< HEAD
        best_state, best_fitness, _ = simulated_annealing(problem,
=======
        best_state, best_fitness = simulated_annealing(problem,
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd
                                                       max_attempts=50)

        x = np.array([1, 1, 1, 1, 1])

        assert (np.array_equal(best_state, x) and best_fitness == 5)

    @staticmethod
    def test_simulated_annealing_continuous_max():
        """Test simulated_annealing function for a continuous maximization
        problem"""

        problem = ContinuousOpt(5, OneMax(), maximize=True)
<<<<<<< HEAD
        best_state, best_fitness, _ = simulated_annealing(problem,
=======
        best_state, best_fitness = simulated_annealing(problem,
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd
                                                       max_attempts=50)

        x = np.array([1, 1, 1, 1, 1])

        assert (np.array_equal(best_state, x) and best_fitness == 5)

    @staticmethod
    def test_simulated_annealing_discrete_min():
        """Test simulated_annealing function for a discrete minimization
        problem"""

        problem = DiscreteOpt(5, OneMax(), maximize=False)
<<<<<<< HEAD
        best_state, best_fitness, _ = simulated_annealing(problem,
=======
        best_state, best_fitness = simulated_annealing(problem,
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd
                                                       max_attempts=50)

        x = np.array([0, 0, 0, 0, 0])

        assert (np.array_equal(best_state, x) and best_fitness == 0)

    @staticmethod
    def test_simulated_annealing_continuous_min():
        """Test simulated_annealing function for a continuous minimization
        problem"""

        problem = ContinuousOpt(5, OneMax(), maximize=False)
<<<<<<< HEAD
        best_state, best_fitness, _ = simulated_annealing(problem,
=======
        best_state, best_fitness = simulated_annealing(problem,
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd
                                                       max_attempts=50)

        x = np.array([0, 0, 0, 0, 0])

        assert (np.array_equal(best_state, x) and best_fitness == 0)

    @staticmethod
    def test_simulated_annealing_max_iters():
        """Test simulated_annealing function with max_iters less than
        infinite"""

        problem = DiscreteOpt(5, OneMax(), maximize=True)
        x = np.array([0, 0, 0, 0, 0])

<<<<<<< HEAD
        best_state, best_fitness, _ = simulated_annealing(
=======
        best_state, best_fitness = simulated_annealing(
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd
            problem, max_attempts=1,
            max_iters=1, init_state=x)

        assert best_fitness == 1

    @staticmethod
    def test_genetic_alg_discrete_max():
        """Test genetic_alg function for a discrete maximization problem"""

        problem = DiscreteOpt(5, OneMax(), maximize=True)
<<<<<<< HEAD
        best_state, best_fitness, _ = genetic_alg(problem, max_attempts=50)
=======
        best_state, best_fitness = genetic_alg(problem, max_attempts=50)
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd

        x = np.array([1, 1, 1, 1, 1])

        assert (np.array_equal(best_state, x) and best_fitness == 5)

    @staticmethod
    def test_genetic_alg_continuous_max():
        """Test genetic_alg function for a continuous maximization problem"""

        problem = ContinuousOpt(5, OneMax(), maximize=True)
<<<<<<< HEAD
        best_state, best_fitness, _ = genetic_alg(problem, max_attempts=200)
=======
        best_state, best_fitness = genetic_alg(problem, max_attempts=200)
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd

        x = np.array([1, 1, 1, 1, 1])

        assert (np.allclose(best_state, x, atol=0.5) and best_fitness > 4)

    @staticmethod
    def test_genetic_alg_discrete_min():
        """Test genetic_alg function for a discrete minimization problem"""

        problem = DiscreteOpt(5, OneMax(), maximize=False)
<<<<<<< HEAD
        best_state, best_fitness, _ = genetic_alg(problem, max_attempts=50)
=======
        best_state, best_fitness = genetic_alg(problem, max_attempts=50)
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd

        x = np.array([0, 0, 0, 0, 0])

        assert (np.array_equal(best_state, x) and best_fitness == 0)

    @staticmethod
    def test_genetic_alg_continuous_min():
        """Test genetic_alg function for a continuous minimization problem"""

        problem = ContinuousOpt(5, OneMax(), maximize=False)
<<<<<<< HEAD
        best_state, best_fitness, _ = genetic_alg(problem, max_attempts=200)
=======
        best_state, best_fitness = genetic_alg(problem, max_attempts=200)
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd

        x = np.array([0, 0, 0, 0, 0])

        assert (np.allclose(best_state, x, atol=0.5) and best_fitness < 1)

<<<<<<< HEAD
=======
    @staticmethod
    def test_mimic_discrete_max():
        """Test mimic function for a discrete maximization problem"""

        problem = DiscreteOpt(5, OneMax(), maximize=True)
        best_state, best_fitness = mimic(problem, max_attempts=50)

        x = np.array([1, 1, 1, 1, 1])

        assert (np.array_equal(best_state, x) and best_fitness == 5)

    @staticmethod
    def test_mimic_discrete_min():
        """Test mimic function for a discrete minimization problem"""

        problem = DiscreteOpt(5, OneMax(), maximize=False)
        best_state, best_fitness = mimic(problem, max_attempts=50)

        x = np.array([0, 0, 0, 0, 0])

        assert (np.array_equal(best_state, x) and best_fitness == 0)

    @staticmethod
    def test_mimic_discrete_max_fast():
        """Test mimic function for a discrete maximization problem using
        fast mimic"""

        problem = DiscreteOpt(5, OneMax(), maximize=True)
        best_state, best_fitness = mimic(problem, max_attempts=50,
                                         fast_mimic=True)

        x = np.array([1, 1, 1, 1, 1])

        assert (np.array_equal(best_state, x) and best_fitness == 5)

    @staticmethod
    def test_mimic_discrete_min_fast():
        """Test mimic function for a discrete minimization problem using
        fast mimic"""

        problem = DiscreteOpt(5, OneMax(), maximize=False)
        best_state, best_fitness = mimic(problem, max_attempts=50,
                                         fast_mimic=True)

        x = np.array([0, 0, 0, 0, 0])

        assert (np.array_equal(best_state, x) and best_fitness == 0)

>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd

if __name__ == '__main__':
    unittest.main()
