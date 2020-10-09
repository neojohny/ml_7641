#!/bin/bash

echo "Running tests on test_activation.py"
<<<<<<< HEAD
python3 test_activation.py

echo "Running tests on test_decay.py"
python3 test_decay.py

echo "Running tests on test_fitness.py"
python3 test_fitness.py

echo "Running tests on test_algorithms.py"
python3 test_algorithms.py

echo "Running tests on test_opt_probs.py"
python3 test_opt_probs.py

echo "Running tests on test_neural.py"
python3 test_neural.py
=======
python test_activation.py

echo "Running tests on test_decay.py"
python test_decay.py

echo "Running tests on test_fitness.py"
python test_fitness.py

echo "Running tests on test_algorithms.py"
python test_algorithms.py

echo "Running tests on test_opt_probs.py"
python test_opt_probs.py

echo "Running tests on test_neural.py"
python test_neural.py
>>>>>>> 0cbf9e925d017530bd9b68dea67f81a0d031cdbd

echo "Finished all tests"
