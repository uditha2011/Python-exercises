def convert(s):
    # Split the time string into hours and minutes
    hours, minutes = map(int, s.split(':'))

    # Convert hours and minutes to a float representing the time in hours
    time_in_hours = hours + minutes / 60.0
    # print(time_in_hours)
    return time_in_hours

def main():
    # Prompt the user for a time in 24-hour format
    time_input = input("What time is it? ")


        # Convert the input time to a float
    time_in_hours = convert(time_input)

        # Check if it's breakfast time, lunch time, or dinner time
    if 7.0 <= time_in_hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_in_hours <= 13.0:
        print("lunch time")
    elif 18.0 <= time_in_hours <= 19.0:
        print("dinner time")
    else:
        # If it's not mealtime, don't output anything
        pass

main()