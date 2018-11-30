Engineering Final PanoLapse
----------------------------

#### Project Title <br>
PanoLapse
___

#### Team 
Calvin Mack, Roscoe Welch, Braden Parks

___

#### Project Objective 

We set out to make a useful tool in which a typical camera 
user can use the micro:bit as a time lapse timer (intervalometer) and panorama assistant.
The micro:bit capabilities used were primarily the compass and internal timer. These 
allowed us to actually pull off the panorama(compass) and the time
lapse(timer). Pin0 was also used to send a signal for the camera shutter.

___

#### Sources

https://microbit.org/guide/python/ <br>
http://docs.micropython.org/en/latest/ <br>
https://microbit-micropython.readthedocs.io/en/latest/tutorials/io.html <br>
https://www.instructables.com/id/How-to-build-a-shutter-release-cable-for-the-Canon/ <br>


___

#### Design
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

#### Development 

* Initial plan was each person focused on different sections. Roscoe was
timelapse, Calvin was panorama, and Braden was the menu system. These went
well, but required a lot of planning. 

* Roscoe made a function to test interval and total time choices with flashing
smile images.

* Calvin made a progress bar to visualize and test the micro:bit compass

* Braden had a hard time theorizing the menu system and overall where to start 
the initial menus had a lot of conflicting errors between the two systems.

* Before hooking up micro:bit to the camera, we used a [shutter release 
peripheral](https://shop.usa.canon.com/shop/en/catalog/remote-switch-rs-60e3)
and took voltage readings with the micro:bit. The pin0.read_analog() function
was used, displayed 400 (about 1 volt) unpressed and 1 (0.003 volts) when pressed.
Scale was 0-1023. 1023 = 3.3 volts. 

  * Reading from camera was 600-700 (around 2 volts).

  * To trigger shutter needed to send a low signal.
  
  * Input was 2.5 mm jack.

* Initially with write_digital(0) Shutter only went once and had to disconnect 
cord. Had to send a high signal afterward.


___
 

#### Testing Describe your testing approach. What was successful and what failed?

Theorizing ideas on a white board helped a lot when we would come together and 
then split off again. I think it helped us just formulate ideas and come up with 
new ways to think about it Tinkering and trial and error were also great ways to 
think about things differently Braden had a lot of tinkering going on and 
constantly had to scrap code.

___

#### Demo

Calvin made a presentation and tried to go into detail about it with the
hardware. We then answered questions based on it. The demo itself went really
well we got it working and were able to show off the basics of it functionality

![](https://github.com/NotSoRoscoe/EngineeringFinalCamera/blob/master/assets/20181126_192613.jpg)

![](https://github.com/NotSoRoscoe/EngineeringFinalCamera/blob/master/assets/20181126_192710.jpg)

____

#### Summary

Summarize your project, from idea to demo. Point out lessons learned.
Mention the most important features of the micro:bit that supported your
application.