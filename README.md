# Staubli_Gripper
In this repository, a VAL3 program is implemented to control the pneumatic gripper of a Staubli TX2-60L robot with Python. The VAL3 program is based on [ros-industrial staubli VAL3](https://github.com/ros-industrial/staubli_val3_driver/tree/master/staubli_val3_driver/val3).
<figure >
  <img src="/images/im4.jpg" width="600" align=""/>
</figure>


# Hardware Overview

<figure >
  <img src="/images/im1.png" width="350" align="right"/>
</figure>

The gripper is designed to hold the load. For this, it needs a pneumatic system (compressed air pressure supply or vacuum) which comes from the outlets at the forearm (A1, A2, B1, B2, P2).

Staubli TX2-60L robot has 2 optional solenoid valves (EV1 and EV2). These valves are connected between pneumatic connection (P1) at the base and outlet (A1, B1, A2, B2) at the forearm. The solenoid valves can be of three types: Monostable, Bistable and Closed at mid position. The python program sends a digital output to these solenoid valves using a TCP port.

Our Hardware:
- Staubli TX2-60L robot
- CS9 controller
- Two Closed at mid position solenoid valves
- Compressed air pressure connection




# Steps
  [1. Check your hardware](#1)<br/>
  [2. Set pneumatic connection](#2)<br/>
  [3. Find relation between digital output and pneumatic output](#3)<br/>
  [4. Bring your robot controller and operating PC in the same network](#4)<br/>
  [5. Add new TCP server Socket in Emulator](#5)<br/>
  [6. Write your own VAL3 code and integrate it with ros-industrial staubli VAL3](#6)<br/>
  [7. Transfer Modified ros-server VAL3 code to robot controller using FTP](#7)<br/>
  [8. Send Gripper control command from your PC using Python code](#8)<br/>

<a name="1"/><br/>
## 1. Check your hardware
At first, ensure that your robot has solenoid valves (EV1 and EV2). To do so, in the emulator go to `IO`--> `Boards`. If the robot has solenoid valves, you will see `Arm - ValveIO` in this page. Next, go to `Arm-ValveIO` --> `Digital Out`. Here, you will find the type of your solenoid valves.

<a name="2"/><br/>
## 2. Set pneumatic connection
To control the gripper using the solenoid valves, pnematic connection should be connected to **P1**.

<a name="3"/><br/>
## 3. Find relation between digital output and pneumatic output
The relation between digital output and pneumatic output is dependent on the solenoid valve type. It can be checked using the emulator. For this, the emulator profile needs to be in maintenance mode (`Settings`--> `Profiles`--> Change the current profile to `maintenance` by giving password--> `Login`). 

Now, you can manually turn on and off the solenoid valves. To do so, go to `IO` --> `Boards`--> `Arm-ValveIO` --> `Digital out`. Here you can see all valves and their `on/off` status. Now by pressing the shutdown button, you can change the status of the valves.

Our robot has two Close at mid position solenoid valves. In Table 1, the relation between Digital Outputs (V2, V2 Enable), Pneumatic Outputs at forearm (A2, B2) and Gripper Status are shown. 


<p align="center">
<a name="tab1"/><br/>
Table 1
</p>

| Condition no.| Valve 2 <br/>(CLOSED AT MID POS)| Valve 2 Enable | Pneumatic output   A2 | Pneumatic output  B2 | Gripper Status |
| -------------| -------------------------- | -------------- |------------------------------ |------------------------------ | -------- |
|01| 0 | 0 | close | close | no change | 
|02| 0  | 1 | close  | open | open |
|03| 1 | 0 | close | close | no change |
|04| 1 | 1 | open | close | close |

<a name="4"/><br/>
## 4. Bring your robot controller and operating PC in the same network
Connect your computer with the robot controller with an ethernet cable. Your computer and the robot controller have to be in the same ethernet subnet, i.e. the first 3 numbers of your computer ethernet ip have to be the same as the robot controller ip, the last number should be different. <br/>
(So if the robot controller ip is 192.168.0.254, then your computer ip could be 192.168.0.10) 

<a name="5"/><br/>
## 5. Add new TCP server Socket in Emulator
From your PC you can send data to the robot controller using a python program. For this, you need a TCP server socket in your robot controller. <br /> In emulator, `Main menu`:
1. `IO` --> `Socket` --> `TCP Servers` --> `"+"` <br />
2. Configure a new socket: 
   * Name: Gripper_socket, Port: 5000, Timeout: -1, End of string: 13

<a name="6"/><br/>
## 6. Write your own VAL3 code and integrate it with [ros-industrial staubli VAL3](https://github.com/ros-industrial/staubli_val3_driver/tree/master/staubli_val3_driver/val3) code 
You can do this in two ways:

* [Directly changing the VAL3 code](https://github.com/FAU-FAPS/staubli_gripper/tree/main/Integration_using_VAL3_program)
* [Using Staubli Robotics Suite (SRS)](https://github.com/FAU-FAPS/staubli_gripper/tree/main/Integration_using_Staubli_Robotics_Suite)

<a name="7"/><br/>
## 7. Transfer Modified ros-server VAL3 code to robot controller using FTP
* Download and install FileZilla 
* Open FileZilla. Go to `File`--> `Site Manager`--> `General`
* Create a `New site`. Give it a name (i.e s1)
  + Protocol: FTP-File Transfer Portocol
  + Host: Write the robot ip
  + Port: At which port the robot controller is connected
  + User: default
  + Password: write the password
* Then `Connect`
* If the connection is successful, transfer the modified ros_server folder to (/usr/usrapp) folder of the robot controller 

<a name="8"/><br/>
## 8. Send Gripper control command from your PC using Python code
* Download [raptor_gripper.py](https://github.com/FAU-FAPS/staubli_gripper/blob/main/raptor_gripper.py) in your PC
* For gripper operation: 
```python
import raptor_gripper

# create gripper object 
gripper = raptor_gripper.Gripper(robot_ip='192.168.0.250', robot_tcp_port=5000) 
# open gripper 
gripper.open()
# close gripper 
gripper.close() 
```

## Authors and acknowledgment
This publication is based on the project [staubli_val3_driver](https://github.com/ros-industrial/staubli_val3_driver). The gripper extension was developed by [Tabassum Nova](https://github.com/TabassumNova) and [Oguz Kedilioglu](https://github.com/Oguked). 

## License
[Apache-2.0 license](LICENSE) 

