# main_test.py

import time
from helpers import gen_mass_cases
from dataset import load_dataset
from temp_calculation import get_birthday_temp

def main():
    #change the cases var to determine how many cases you would like to run
    cases = 1000
    test_cases = gen_mass_cases(cases)
    ds = load_dataset()
    total_time = 0

    for test_case in test_cases:
        start_time = time.time()
        air_temp = get_birthday_temp(ds, test_case)
        end_time = time.time()
        total_time += end_time - start_time

        print(f"The average air temperature on {test_case['name']}'s birthday ({test_case['birthday']}) at the location of ({test_case['lat']}, {test_case['lon']}) was {air_temp:.2f} degrees Fahrenheit.")

    avg_time = total_time / cases
    print(f" The average execution time over {cases} cases is {avg_time:.10f} seconds")

if __name__ == "__main__":
    main()
