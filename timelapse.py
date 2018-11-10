from microbit import *

# Dictionary Timelapse Interval
time_choices = {0: 1000,     # 01 second
                1: 3000,     # 02 seconds
                2: 5000,     # 05 seconds
                3: 10000,    # 10 seconds
                4: 15000,    # 15 seconds
                5: 30000,    # 30 seconds
                6: 45000,    # 45 seconds
                7: 60000,    # 60 seconds
                8: 90000}    # 90 seconds

# Dictionary Timelapse Interval Strings to Display
show_time_intervals = {0: '1 second',
                       1: '2 seconds',
                       2: '5 seconds',
                       3: '10 seconds',
                       4: '15 seconds',
                       5: '30 seconds',
                       6: '45 seconds',
                       7: '60 seconds',
                       8: '90 seconds'}

# Dictionary Timelapse Duration
duration_choices = {0: 60000,      # 01 minute
                    1: 120000,     # 02 minutes
                    2: 300000,     # 05 minutes
                    3: 600000,     # 10 minutes
                    4: 900000,     # 15 minutes
                    5: 1800000,    # 30 minutes
                    6: 3600000,    # 01 hours
                    7: 7200000,    # 02 hours
                    8: 14400000}   # 04 hours

# Dictionary Timelapse Duration Strings to Display
show_durations = {0: '1 minute',
                  1: '2 minutes',
                  2: '5 minutes',
                  3: '10 minutes',
                  4: '15 minutes',
                  5: '30 minutes',
                  6: '1 hours',
                  7: '2 hours',
                  8: '4 hours'}

menu_cycle = -1  # to increment when searching dictionaries


#  -------------------- Function to Send Photo Pulses -------------------------
#
#          The use can hopefully be for both timelapse and panorama
#
#                              The parameters
#      take_photos(Interval, Full Panorama Angle/Total Time, True/False)
#                For panorama use True. For timelapse use False
#  ----------------------------------------------------------------------------


def take_photos(interval, total, panorama):
    photo_number = total // interval  # Loop Number
    #   May be useful for panorama part but is needed for timelapse part

    # TODO Mock up part of Panorama Function
    #    The code in the 'if' statements are just an idea of how
    #    you might want to use the function. I don't know if this
    #    part would even work the way it is.
    if panorama:
        angle = 0
        initial_heading = compass.heading()
        while angle <= total:
            current_heading = compass.heading() - initial_heading
            if current_heading < 0:
                current_heading += 360
            if current_heading > 360:
                current_heading -= 360
            if current_heading >= angle:
                pin0.write_digital(1)
                angle += interval
        pass

    else:
        for photos in range(photo_number):
            # pin0.write_digital(1)  # TODO undo Comment. Delete next 3 lines.
            display.show(Image.HAPPY)
            sleep(200)
            display.clear()
            sleep(interval)


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
    display.scroll("Press a to continue")

    if button_a.was_pressed():
        
        while True:
            # display.scroll("5 sec") # TODO delete
            # time_interval = 5000    # TODO delete

            # TODO comment out to test While loops
            menu_cycle = 0
            display.scroll(show_time_intervals[menu_cycle])
            time_interval = time_choices[menu_cycle]

            if button_a.was_pressed():
                menu_cycle = menu_cycler(menu_cycle, len(show_time_intervals))
                break

        while True:
            display.scroll(show_time_intervals[menu_cycle])
            time_interval = time_choices[menu_cycle]

            if button_a.was_pressed():
                menu_cycle = menu_cycler(menu_cycle, len(show_time_intervals))
                continue

            elif button_b.is_pressed():
                break

        while True:
            # display.scroll("10 pics")
            # total_time = 60000
            # take_photos(time_interval, total_time, False)

            # TODO comment out for tests
            menu_cycle = 0
            display.scroll(show_durations[menu_cycle])
            total_time = time_choices[menu_cycle]

            if button_a.was_pressed():
                menu_cycle = menu_cycler(menu_cycle, len(show_time_intervals))
                break

        while True:
            display.scroll(show_durations[menu_cycle])
            total_time = time_choices[menu_cycle]

            if button_a.was_pressed():
                menu_cycle = menu_cycler(menu_cycle, len(show_durations))
                continue

            elif button_b.was_pressed():
                take_photos(time_interval, total_time, False)
                # for photos in range(photo_number):
                #     # pin0.write_digital(1)  # TODO test and delete.
                #     display.show(Image.HAPPY)
                #     sleep(200)
                #     display.clear()
                #     sleep(interval)
                break

    else:         # TODO not sure this is needed or not so try test w/o
        continue
