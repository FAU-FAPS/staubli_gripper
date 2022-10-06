# Write a new program and integrate it into ros_server using SRS (Demo_Gripper)
1. Create [a new robot cell](https://github.com/FAU-FAPS/staubli_gripper/tree/master/Getting_started_with_Staubli_Robotics_Suite) in SRS and load [ros_server and ros_lib](https://github.com/ros-industrial/staubli_val3_driver/tree/master/staubli_val3_driver/val3) in it.
2. Create one new socket (TCP Servers) on the emulator: <br/> 
  `Control panel` --> `I/O` --> `Socket` --> `TCP Servers` <br/>
  Configure one socket: <br/>
    + Name: Gripper_socket, Port: 5000, Timeout: -1, Delimiter: 13, Nagle: Off <br/>
1. For the gripper operation, we needed one new sio. In `Cell Explorer` block, right click on `ros_server`--> `Add`--> `New Data`--> `sio`. Give it a Name (gripper_sio), select--> `Public`
2. For the gripper operation, we needed two new dio. In `Cell Explorer` block, right click on `ros_server`--> `Add`--> `New Data`--> `dio`. Give it a Name (**v2_clsMid**, **v2_enable**), select--> `Public`
3. In the `Data` block (beside `Cell Explorer`), all the new created sio and dio can be seen.
4. Under-> `Home`--> `Physical IOs`. Link Logical sio and dio to the Physical IOs by drag and drop from `Data` block
![Semantic description of image](/images/new_im2.PNG)
5. In `Cell Explorer` block, right click on `ros_server`--> `Add`--> `New Program`. Give it a Name [(gripper_operation)](https://github.com/FAU-FAPS/staubli_gripper/blob/master/Modified%20ros_server/ros_server/gripper_operation.pgx), select-> `Public`.
Write the program inside `begin` and `end`. If any local variable is needed, in `Cell explorer`--> `ros_server` --> right click on `gripper_operation()`--> `Add`--> `New Local Variable`--> `variable type (i.e num)` and give it a name.
For the gripper operation, we needed two local variables: **l_nIndex** and **l_nByte**
6. To add new lines on the monitor, `Cell Explorer`--> `ros_server`--> `interface`--> `uxMonitor.html`
    - Add new `Label` from `Toolbox`
    - Give an Id of the label (i.e msg1)
    ![Semantic description of image](/images/new_im3.PNG)
    - Inside the program
    ```python
    userPage("uxMonitor")
    userPageSet("uxMonitor", "msg1", "innerHTML", "Connected")
    ```
    [Details of userPage() and userPageSet() can be found in [VAL Reference Manual](https://github.com/FAU-FAPS/staubli_gripper/blob/master/VAL%20Reference%20Manual%20-%20Version%208.PDF)]
6. In `ros_Server`--> [`start.pgx`](https://github.com/FAU-FAPS/staubli_gripper/blob/master/Modified%20ros_server/ros_server/start.pgx), add lines 
    ```python
    sGripperTaskName = "gripperTask"
    taskCreateSync sGripperTaskName, .02, bGripOverrun, gripper_operation()
    ```
    [Details of taskCreateSync can be found in [VAL Reference Manual](https://github.com/FAU-FAPS/staubli_gripper/blob/master/VAL%20Reference%20Manual%20-%20Version%208.PDF)]

    For this we need two global variables: **bGripOverrun (bool)** and **sGripperTaskName (string)**. To create these, `Cell Explorer`-->right click--> `ros_server`-->     `Add`--> `New Data`--> `bool`. Give it a Name (bGripOverrun)-> `Public`
