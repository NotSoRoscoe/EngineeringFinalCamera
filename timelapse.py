from microbit import *

# Dictionary Timelapse Interval
time_choices = {0: 1000,  # 01 second
                1: 3000,  # 02 seconds
                2: 5000,  # 05 seconds
                3: 10000,  # 10 seconds
                4: 15000,  # 15 seconds
                5: 30000,  # 30 seconds
                6: 45000,  # 45 seconds
                7: 60000,  # 60 seconds
                8: 90000}  # 90 seconds

# Dictionary Timelapse Interval Strings to Display
show_times = {0: '1 SEC',
              1: '2 SEC',
              2: '5 SEC',
              3: '10 SEC',
              4: '15 SEC',
              5: '30 SEC',
              6: '45 SEC',
              7: '60 SEC',
              8: '90 SEC'}

# Dictionary Timelapse Duration
duration_choices = {0: 60000,  # 01 minute
                    1: 120000,  # 02 minutes
                    2: 300000,  # 05 minutes
                    3: 600000,  # 10 minutes
                    4: 900000,  # 15 minutes
                    5: 1800000,  # 30 minutes
                    6: 3600000,  # 01 hours
                    7: 7200000,  # 02 hours
                    8: 14400000}  # 04 hours

# Dictionary Timelapse Duration Strings to Display
show_durations = {0: '1 MIN',
                  1: '2 MIN',
                  2: '5 MIN',
                  3: '10 MIN',
                  4: '15 MIN',
                  5: '30 MIN',
                  6: '1 HOUR',
                  7: '2 HOUR',
                  8: '4 HOUR'}

screen_filler = [Image("90000:"
                       "90000:"
                       "90000:"
                       "90000:"
                       "90000"),
                 Image("99900:"
                       "99900:"
                       "99900:"
                       "99900:"
                       "99000"),
                 Image("99990:"
                       "99990:"
                       "99990:"
                       "99990:"
                       "99990"),
                 Image("99999:"
                       "99999:"
                       "99999:"
                       "99999:"
                       "99999")]

menu_cycle = -1  # to increment when searching dictionaries
time_interval = -1  # how long to wait for timelapse
total_time = -1  # running time for timelapse


#  -------------------- Function to Send Photo Pulses -------------------------
#
#          The use can hopefully be for both timelapse and panorama
#
#                              The parameters
#      take_photos(Interval, Full Panorama Angle/Total Time, True/False)
#                For panorama use True. For timelapse use False
#  ----------------------------------------------------------------------------


def take_photos(interval, total, panorama):
    photo_number = total // interval

    # TODO Mock up part of Panorama Function
    if panorama:
        while True:
            display.scroll("A to set start point", wait=False, loop=True)
            if button_a.was_pressed():  # to reset initial position
                hdg = compass.heading()
                display.scroll("set")
                i = 1
                display.show(Image.HAPPY)
                sleep(500)
                display.clear()
                while i in range(1, photo_number + 1):
                    if button_a.was_pressed():
                        i = -1
                        break
                    if compass.heading() - hdg < 0:
                        correct = 360
                    else:
                        correct = 0
                    if (compass.heading() - hdg + correct) > (total + interval):
                        display.show(Image.ARROW_E)
                    elif (compass.heading() - hdg + correct) < (i * interval):
                        display.show(i)
                    elif (compass.heading() - hdg + correct) >= (i * interval):
                        i += 1
                        display.show(Image.HAPPY)
                        sleep(500)
                        display.clear()
                if i == (photo_number + 1):
                    display.show(Image.HAPPY)
                    sleep(500)
                    display.clear()
                    break
                display.scroll("A to reset start", wait=False, loop=True)
    else:
        pin0.write_digital(1)         # This is outside the loop so the function
        sleep(50)                     # will start and stop immediately with a
        pin0.write_digital(0)         # picture
        display.show(Image.HAPPY)
        sleep(5)
        display.clear()
        for pic in range(photo_number - 1):
            sleep(interval)
            pin0.write_digital(1)
            sleep(50)
            pin0.write_digital(0)
            display.show(Image.HAPPY)
            sleep(5)
            display.clear()
        pin0.write_digital(1)


def progress_bar(progress, divisions, increment, count):
    increment += divisions
    if progress >= divisions:
        display.show(screen_filler[count])
        sleep(1000)
    return increment

#  ------------------ Function to Increment Menu Number -----------------------
#
#                  This is super simple placeholder menu
#                system for the dictionaries above just for
#                now more to test how the above function
#                works or not
#  ----------------------------------------------------------------------------


def menu_cycler(cycle, end_point):
    if cycle == end_point - 1:
        cycle = 0
    else:
        cycle += 1
    return cycle


#  ---------------------------- Time Lapse Loop -------------------------------
#  ----------------------------------------------------------------------------


while True:
    menu_cycle = 0
    time_interval = time_choices[menu_cycle]
    total_time = duration_choices[menu_cycle]

    display.show("A")
    if button_b.was_pressed():
        compass.heading()
        angle_total = 180
        angle_interval = 45
        take_photos(angle_interval, angle_total, True)

    if button_a.was_pressed():
        display.scroll(show_times[menu_cycle], wait=False, loop=True)

        while True:
            if button_a.was_pressed():
                menu_cycle = menu_cycler(menu_cycle, len(show_times))
                time_interval = time_choices[menu_cycle]
                display.scroll(show_times[menu_cycle], wait=False, loop=True)
                continue

            if button_b.was_pressed():
                menu_cycle = 0
                break

        display.scroll(show_durations[menu_cycle], wait=False, loop=True)

        while True:
            if button_a.was_pressed():
                menu_cycle = menu_cycler(menu_cycle, len(show_durations))
                total_time = duration_choices[menu_cycle]
                display.scroll(show_durations[menu_cycle], wait=False, loop=True)
                continue

            if button_b.was_pressed():
                break

        while True:
            take_photos(time_interval, total_time, False)
            display.scroll("ALL DONE")
            display.clear()
            sleep(1000)
            break
