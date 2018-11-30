Engineering Final PanoLapse
----------------------------

### Project Title 
##### PanoLapse
___

### Team 
Calvin Mack, Roscoe Welch, Braden Parks

___

### Project Objective 

We set out to make a useful tool in which a typical camera 
user can use the micro:bit as a time lapse timer (intervalometer) and panorama assistant.
The micro:bit capabilities used were primarily the compass and internal timer. These 
allowed us to actually pull off the panorama(compass) and the time
lapse(timer). Pin0 was also used to send a signal for the camera shutter.

___

### Sources

https://microbit.org/guide/python/ <br>
http://docs.micropython.org/en/latest/ <br>
https://microbit-micropython.readthedocs.io/en/latest/tutorials/io.html <br>
https://www.instructables.com/id/How-to-build-a-shutter-release-cable-for-the-Canon/ <br>

___

### Design
Describe your design briefly and reference any supporting materials
in the assets folder. Talk about input, output, processing, and storage 
(aka memory) in your design.

The design is mainly menu navigation as follows: 

* The user chooses from the opening menu to go into either the timelapse mode
(a button) or panorama mode (b button). 

* Cycle (a button) a list of choices for interval angle/time. Press b to select.

* Cycle (a button) a list of choices for the total angle/time. Press b to select.

* *For panorama only* - Press a to set starting point and after countdown
begin turning camera slowly.

* Camera starts taking pictures. Once done it will return to opening menu.
 
The input is taken purely from the buttons and compass readings.
The output consists of both the LEDs on the 5x5 screen and a low to high signal
from pin0 used for the camera shutter. 
Most of the code is nested while loops that keeps navigation menus separate 
and organized. The memory is mainly used to hold the list of menu choice displays
and the corresponding values.   
 
Calvin created a sleeve to attach the micro:bit to
the camera. This prevents the camera's hotshoe from interfering with the micro:bit
as well as keep it attached to the camera, preventing any dangling of the micro:bit.

___

### Development 

* Initial plan was each person focused on different sections. Roscoe was
timelapse, Calvin was panorama, and Braden was the menu system. These went
well, but required a lot of planning. 

* Roscoe made a function to test interval and total time choices with flashing
smile images.

* Calvin made a progress bar to visualize and test the micro:bit compass

* Braden had a hard time theorizing the menu system and overall where to start 
the initial menus. Had a lot of conflicting errors between the two systems.

* Before hooking up micro:bit to the camera (Canon Rebel t3i), we used a
[shutter release peripheral](https://shop.usa.canon.com/shop/en/catalog/remote-switch-rs-60e3)
and took voltage readings with the micro:bit. The pin0.read_analog() function
was used, displayed 400 (about 1 volt) unpressed and 1 (0.003 volts) when pressed.
Scale was 0-1023. 1023 = 3.3 volts. 

  * Reading from camera was 600-700 (around 2 volts).

  * To trigger shutter needed to send a low signal.
  
  * Input was 2.5 mm jack.

* Initially with write_digital(0) Shutter only went once and had to disconnect 
cord. Had to send a high signal (write_digital(1)) afterward.

* Compass readings with progress display was not consistent. 

* Added to take_pictures function to be used for both panorama and timelapse. 
Had fix for when so progress bar would be correct when crossing from 359* to 0*.

* Menu made with while True loops with breaks to navigate to the next section. 
Function made to cycle through dictionaries.

* added an input to set/reset the compass initial heading before taking pictures.

* Opening menu display was incorrect (not scrolling or all jumbled). 
While trying to fix the issue ran into the micro:bit's storage limit.
Deleted progress display for panorama and replaced with what picture number 
you were currently on.  

* Possible continuation.
  * Optimize code and put progress meter back in.
  * Have panorama be able to turn left. Can be done with similar idea as we have
  but switching addition to subtraction and vise versa.

___
 

### Testing

Our approach was start small and add little by little. Starting with something 
like just making the micro:bit flash every 10 seconds for a minute. Then adding
an input to start the flashing. After that add a display menu of one item to
click through showing the interval of 5 seconds and total of one minute. Creating
a dictionary and menu cycler to choose different options. This way of small additions
continued until the project was complete.

If we tried thinking of a new way to approach an idea we would start with the most
basic form of that idea. For example when we tried something new with the compass
to understand how it worked, We would try a new hex file that just displayed the
value of the compass heading and then adding ideas to that before taking that idea
back to out main file.     

Theorizing ideas on a white board helped a lot when we would come together. 
it helped formulate ideas and come up with new ways of thinking about our approach. 
Trial and error were also great ways to think about things differently
We had a lot of tinkering going on and constantly had to scrap code.

One thing that failed is the opening menu display. The message would be displayed
incorrectly when the option to skip the message with an input was available. It 
would only display correctly if that part was taken out, even though the rest of
the menu uses the same idea without issue. So you have to wait for the full message
to scroll by before feedback from an input is shown. 

___

### Demo

Calvin made a presentation and went into detail about the hardware and design. 
We then answered questions about the . The demo itself went really
well. We showed it working and were able to show off the basics of it functionality.

![](https://github.com/NotSoRoscoe/EngineeringFinalCamera/blob/master/assets/20181126_192613.jpg)

![](https://github.com/NotSoRoscoe/EngineeringFinalCamera/blob/master/assets/20181126_192710.jpg)

____

### Summary

We started with idea to make the micro:bit be a dual time lapse/panorama controller
and through a decent amount of trial and error achieved our goal when we demonstrated
it to the class. We learned the difficulties of both programming and the workings
of hardware, in our case specifically the compass of the micro:bit as well as figuring
out the working of the camera. The most important features were the compass, timer,
and output from the pins. Those features are the foundation of our idea and without
them we would not have been able to make the PanoLapse.