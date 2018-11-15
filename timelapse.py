from microbit import *

# Dictionary Timelapse Interval
time_choices = {0: 1000,   # 01 second
                1: 3000,   # 02 seconds
                2: 5000,   # 05 seconds
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
duration_choices = {0: 60000,     # 01 minute
                    1: 120000,    # 02 minutes
                    2: 300000,    # 05 minutes
                    3: 600000,    # 10 minutes
                    4: 900000,    # 15 minutes
                    5: 1800000,   # 30 minutes
                    6: 3600000,   # 01 hours
                    7: 7200000,   # 02 hours
                    8: 14400000}  # 04 hours

# Dictionary Timelapse Duration Strings to Display
show_durations = {0: '1 MIN',
                  1: '2 MIN',
                  2: '5 MIN',
                  3: '10 MIN',
                  4: '15 MIN',
                  5: '30 MIN',
                  6: '1 HR',
                  7: '2 HR',
                  8: '4 HR'}

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
#                       For both timelapse and panorama
#
#                              The parameters
#         Interval,  Total Angel/Time, True for Panorama/False for Timelapse
#  ----------------------------------------------------------------------------


def take_photos(interval, total, panorama):
    photo_number = total // interval

    # Panorama part
    if panorama:
        while True:
            display.scroll("A to set start point", wait=False, loop=True)
            if button_a.was_pressed():  # to reset initial position
                hdg = compass.heading()
                display.scroll("Start SET pic in 3...2...1...")
                i = 1
                camera_shutter()
                while i in range(1, photo_number + 1):
                    if button_a.was_pressed():         # to cancel
                        i = -1
                        break
                    if compass.heading() - hdg < 0:
                        hdg += 360
                    #  else:
                        #  correct_compass = 0
                    # For wiggle room if camera is turned the wrong way
                    if (compass.heading() - hdg) > (total + interval):
                        display.show(Image.ARROW_E)
                    elif (compass.heading() - hdg) < (i * interval):
                        display.show(i)
                    elif (compass.heading() - hdg) >= (i * interval):
                        i += 1
                        camera_shutter()
                if i == photo_number + 1:
                    pin0.write_digital(1)  # sets camera back to default
                    return
                else:
                    display.scroll("A to reset start", wait=False, loop=True)

    # Timelapse -starts and stops with picture-
    else:
        camera_shutter()
        for pic in range(photo_number - 1):
            sleep(interval)
            camera_shutter()
    pin0.write_digital(1)  # sets camera back to default

#  TODO delete when above works
#  def progress_bar(progress, divisions, increment, count):
#     increment += divisions
#     if progress >= divisions:
#         display.show(screen_filler[count])
#         sleep(1000)
#     return increment

#  ------------------ Function to Increment Menu Number -----------------------
#
#                      This is super simple menu system
#                   to rotate through the dictionaries above.


def menu_cycler(cycle, end_point):
    if cycle == end_point - 1:
        cycle = 0
    else:
        cycle += 1
    return cycle


# -------------------- Send Shutter Signal to Camera ---------------------------


def camera_shutter():
    pin0.write_digital(1)
    sleep(50)
    pin0.write_digital(0)
    display.show(Image.HAPPY)
    sleep(350)
    display.clear()


#  ------------------------------- Main ---------------------------------------
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
