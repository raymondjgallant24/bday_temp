# main.py
from helpers import gen_test_case  # Ensure this matches the function name in helpers.py
from dataset import load_dataset
from temp_calculation import get_birthday_temp

def obtain_user_input():
    print("This program is designed to take your birthday and provide you with the temperature of your location")
    user_name = input("Hello, what is your name?: ")
    user_bday = input(f"Hello, {user_name}, Please provide me with your Birthday in a MM/DD/YYYY format: ")
    user_lat = float(input(f"Thank you, {user_name}, Next I will need your latitude coordinate: "))
    user_lon = float(input(f"{user_name}, Now all I need is your longitude coordinate and I can begin the process"))

    user_info = {
        "name": user_name,
        "birthday": user_bday,
        "lat": user_lat,
        "lon": user_lon
    }
    return user_info

def main():
    ds = load_dataset()
    user_info = obtain_user_input()

    start_time = time.time()
    air_temp = get_birthday_temp(ds, user_info)
    end_time = time.time()
    
    print(f"The average air temperature on {user_info['name']}'s birthday ({user_info['birthday']}) at the location of ({user_info['lat']}, {user_info['lon']}) was {air_temp:.2f} degrees Fahrenheit.")
    total_time = end_time - start_time
    print(f" The total execution time is {total_time:.10f} seconds")

if __name__ == "__main__":
    main()
