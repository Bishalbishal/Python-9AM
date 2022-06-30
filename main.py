# ntc to ncell ( 2.5 bonus if 10min, if 20 min 5
# ntc to ntc 0.5
# ncell to ntc ( under 10 min = 5rs)
# ncell to ncell ( under 10 min = 1.5)


user_sim = ""
call_time = 0
bonus = 0
user_sim = input("Your SIM (Ncell or NTC): ".upper())
receiver = input("Receiver SIM (Ncell or NTC) : ".upper())
call_time = int(input("How long was your call? (In minutes): "))
if user_sim == "NTC" and receiver == "NCELL" and call_time != 100:
    if call_time < 10:
        bonus = 2.5
    elif call_time <= 20 and call_time > 10:
        bonus = 2.5 * 2
    elif call_time <= 30 and call_time > 20:
        bonus = 2.5 * 3
    elif call_time <= 40 and call_time > 30:
        bonus = 2.5 * 4
    elif call_time <= 50 and call_time > 40:
        bonus = 2.5 * 5
    elif call_time <= 60 and call_time > 50:
        bonus = 2.5 * 6
    elif call_time <= 70 and call_time > 60:
        bonus = 2.5 * 7
    elif call_time <= 80 and call_time > 70:
        bonus = 2.5 * 8
    elif call_time <= 90 and call_time > 80:
        bonus = 2.5 * 9
    elif call_time <= 100 and call_time > 90:
        bonus = 2.5 * 10
    else:
        print("Cannot exceed 100minutes of call time.")

elif user_sim == "NTC" and receiver == "NTC" and call_time != 100:
    if call_time < 10:
        bonus = 0.5
    elif call_time <= 20 and call_time > 10:
        bonus = 0.5 * 2
    elif call_time <= 30 and call_time > 20:
        bonus = 0.5 * 3
    elif call_time <= 40 and call_time > 30:
        bonus = 0.5 * 4
    elif call_time <= 50 and call_time > 40:
        bonus = 0.5 * 5
    elif call_time <= 60 and call_time > 50:
        bonus = 0.5 * 6
    elif call_time <= 70 and call_time > 60:
        bonus = 0.5 * 7
    elif call_time <= 80 and call_time > 70:
        bonus = 0.5 * 8
    elif call_time <= 90 and call_time > 80:
        bonus = 0.5 * 9
    elif call_time <= 100 and call_time > 90:
        bonus = 0.5 * 10
elif user_sim == "NCELL" and receiver == "NTC" and call_time != 100:
    if call_time < 10:
        bonus = 5
    elif call_time <= 20 and call_time > 10:
        bonus = 5 * 2
    elif call_time <= 30 and call_time > 20:
        bonus = 5 * 3
    elif call_time <= 40 and call_time > 30:
        bonus = 5 * 4
    elif call_time <= 50 and call_time > 40:
        bonus = 6 * 5
    elif call_time <= 60 and call_time > 50:
        bonus = 5 * 6
    elif call_time <= 70 and call_time > 60:
        bonus = 5 * 7
    elif call_time <= 80 and call_time > 70:
        bonus = 5 * 8
    elif call_time <= 90 and call_time > 80:
        bonus = 5 * 9
    elif call_time <= 100 and call_time > 90:
        bonus = 5 * 10
elif user_sim == "NCELL" and receiver == "NCELL" and call_time != 100:
    bonus += 1.5
    if call_time < 10:
        bonus = 1.5
    elif call_time <= 20 and call_time > 10:
        bonus = 1.5 * 2
    elif call_time <= 30 and call_time > 20:
        bonus = 1.5 * 3
    elif call_time <= 40 and call_time > 30:
        bonus = 1.5 * 4
    elif call_time <= 50 and call_time > 40:
        bonus = 1.5 * 5
    elif call_time <= 60 and call_time > 50:
        bonus = 1.5 * 6
    elif call_time <= 70 and call_time > 60:
        bonus = 1.5 * 7
    elif call_time <= 80 and call_time > 70:
        bonus = 1.5 * 8
    elif call_time <= 90 and call_time > 80:
        bonus = 1.5 * 9
    elif call_time <= 100 and call_time > 90:
        bonus = 1.5 * 10

print(bonus)


