"""This program is designed to determine the award a person competing in a triathlon will receive.
The program uses the times for each event, by each player to dsplay these results and outcome.
The program makes use of a qualification and total time criteria for the award outcome."""

swimming_time = float(input("Enter swimming completion time(minutes): \n"))
cycling_time = float(input("Enter cycling completion time(minutes): \n"))
running_time = float(input("Enter running completeion time(minutes): \n"))
total_time = round((swimming_time + cycling_time + running_time), 2)

if total_time <= 100:
    print(f'''Your total qualifying time is: {total_time} minutes,\
you are awarded provincial colours!''')
elif total_time > 100 and total_time <= 105:
    print(f'''Your total qualifying time is: {total_time} minutes,\
you are awarded provincial half colours''')
elif total_time >= 106 and total_time <= 110:
    print(f'''Your total qualifying time is: {total_time} minutes,\
you are awarded a provincial scroll!''')
else:
    print(f'''Your total qualifying time is: {total_time} minutes,\
no award this time, better luck next time.''')
