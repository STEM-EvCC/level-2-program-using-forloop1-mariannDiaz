# Write a Python program that:

# Counts the total number of space missions.
# Counts the number of successful missions.
# Calculates the success rate of the missions.
# Lists all the missions that were launched before the year 2000.

# Implement the Analysis:

    # Use a for loop to iterate through the list of missions.
    # Count the total number of missions.
    # Count the number of successful missions.
    # Identify and list all missions launched before the year 2000.

# Output the Results:

    # Print the total number of missions.
    # Print the number of successful missions.
    # Print the success rate as a percentage.
    # Print the names of the missions launched before the year 2000.

mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]


def total_missions():
    missions_counter = 0
    for i in mission_names:
        missions_counter += 1
    print( "Total number of missions: ", missions_counter)


def successful_missions():
    succes_counter = 0
    for i in mission_success:
        if i:
            succes_counter += 1
    print("Number of successful missions: ", succes_counter)


def success_rate():
    success_rate = 0
    for i in mission_success:
        if i:
            success_rate += 1

    rate = (success_rate / len(mission_success)) * 100 
    print("Success rate: {:.2f}%".format(rate))


def print_missions_names():
    print("Missions launched before the year 2000: ")
    for i in range(len(mission_years)):
        if mission_years[i] < 2000:
            print("-" , mission_names[i])


total_missions()
successful_missions()
success_rate()
print_missions_names()




