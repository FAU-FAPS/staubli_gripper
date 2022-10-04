# Getting Started with Staubli Robotics Suite (SRS)

1. Plug in the license dongle; Install SRS in a windows operating system.
2. Open SRS program; To create new robot cell, `New` --> `New cell wizard`.
3. Give it a Name (i.e tx2_60l) and select the Path.
4. Select-> `Add a local controller`. It will show all the installed robot schematics.
5. Select your robot (i.e TX2-60L floor mounted robot)
6. Select `Valves` if you have any (i.e Closed at mid position); In the `Options` -->`Select a pack`-->`VAL3`. select the following `Demo mode`: VAL3, advCtrlFunctions, carriedPart, oemLicence, remoteMaintenance, remoteMcp, spline, valKernel, valTrack
7. In the `Finish page`, check if correct controller and valves are chosen (i.e TX2-60L, controller: Cs9 and Valves: Closed at mid position)
8. To see the 3D view, under `Home`--> `Show 3D view`
8. Go to the path where you have saved the new robot cell; You will find one folder named Controller1 and one file named tx2_60l.cell
9. Inside the path (~\tx2_60l\Controller1\usr\usrapp), copy [ros_server and ros_libs](https://github.com/ros-industrial/staubli_val3_driver/tree/master/staubli_val3_driver/val3) folders
10. Inside SRS, in `Cell Explorer` block- right click on `Controller1`, select--> `Open Application` and load **ros_server.pjx** file. Then you will find `ros_server` in the `Cell Explorer` block.
11. To show the emulator, under `Home`--> `Show Emulator`
12. Create two sockets (TCP Servers) on the emulator for staubli_val3_driver: <br/> 
  `Control panel` --> `I/O` --> `Socket` --> `TCP Servers` <br/>
  Configure two sockets <br/>
    + Name: Feedback, Port: 11002, Timeout: -1, Delimiter: 13, Nagle: Off <br/>
    + Name: Motion, Port: 11000, Timeout: -1, Delimiter: 13, Nagle: Off <br/>
12. In the `Cell Explorer` block, right click on `ros_server`--> `Run Application`. The virtual emulator will show the same page as the real emulator.
![Semantic description of image](/images/new_im1.PNG)

