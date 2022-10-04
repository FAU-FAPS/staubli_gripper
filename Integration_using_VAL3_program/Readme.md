# Write your own VAL3 Program (Demo_Gripper)

A simple demonstration on how to write a new VAL3 program for gripper control and integrate it with [ros-industrial staubli VAL3 driver](https://github.com/ros-industrial/staubli_val3_driver/tree/master/staubli_val3_driver/val3) is illustrated here. We tested this with Staubli TX2-60L robot (CS9 controller). Our robot has two Closed at mid position solenoid valves (EV1 and EV2). A new TCP server socket (Name: Gripper_socket, Port: 5000) has been created using the emulator. The relation between digital output and pneumatic output is shown in [Table 1](https://github.com/FAU-FAPS/staubli_gripper/blob/main/README.md). 

The steps are the following : 

- To define the newly created TCP server socket in VAL3, we need a **global variable (gripper_sio)**
- We selected Condition no. 02 and 04 from table 1 for our gripper operation. For this, we need two **global variables (v2_clsMid and v2_enable)**

| Condition no.| v2_clsMid| v2_enable |    Pneumatic output   A2      |     Pneumatic output  B2      | Gripper Status
| -------------| ---------| -------------- |------------------------------ |------------------------------ | ------ |
|02| 0 | 1 | close | open | open |
|04| 1  | 1 | open  | close | close |
- We add this global variable in the [**ros_server.dtx**](https://github.com/FAU-FAPS/staubli_gripper/blob/main/Modified%20ros_server/ros_server/ros_server.dtx) file. 
```python
    <Data name="gripper_sio" access="public" xsi:type="array" type="sio" size="1">
      <Value key="0" link="Socket\Gripper_socket" />
    </Data>
    <Data name="v2_clsMid" access="public" xsi:type="array" type="dio" size="1">
      <Value key="0" link="ValveIO\valve2" />
    </Data>
    <Data name="v2_enable" access="public" xsi:type="array" type="dio" size="1">
      <Value key="0" link="ValveIO\valve2Enable" />
    </Data>
```
Here, `link` is an important factor. You will find this in emulator: <br/>
  > IO --> Socket --> TCP Servers --> Gripper_socket <br/>
  > IO--> Boards--> Arm-ValveIO--> Digital out --> Valve 2(CLOSED AT MID POS)

<img src="/images/Capture4.PNG" width="350"/> <img src="/images/Capture5.PNG" width="350"/>

- Create a new .pgx file inside the ros_server folder [(**gripper_operation.pgx**)](https://github.com/FAU-FAPS/staubli_gripper/blob/main/Modified%20ros_server/ros_server/gripper_operation.pgx). Write the program inside it. Write the local variables in the front.

- Now, integrate the newly created program in the ros-industrial staubli VAL3 driver. In **ros_Server**--> [**start.pgx**](https://github.com/FAU-FAPS/staubli_gripper/blob/main/Modified%20ros_server/ros_server/start.pgx)--> add the following lines to run the newly created program. 
```python
sGripperTaskName = "gripperTask"
taskCreateSync sGripperTaskName, .02, bGripOverrun, gripper_operation()
```

