"""This module enables to open and close the pneumatic gripper of a Staeubli robot with a CS9 control."""

import socket
import time 


class Gripper(): 
    """
    Gripper class containing opening and closing functions for the pneumatic gripper of a Staeubli robot. 
    """
    
    def __init__(self, robot_ip='192.168.0.250', robot_tcp_port=5000) -> None:
        """
        Initiliazes gripper object. 

        Args:
            robot_ip (str, optional): The IP address of the robot. Defaults to '192.168.0.250'.
            robot_tcp_port (int, optional): The TCP port on the robot controller. Defaults to 5000.
        """
        self.robot_ip = robot_ip
        self.robot_tcp_port = robot_tcp_port 
        self.sleeptime = 10 # time inbetween operations; in seconds; 
        print("[GRIPPER] Initialized with IP "+str(self.robot_ip)+" and port "+str(self.robot_tcp_port)) 
        

    def open(self): 
        """
        Opens the gripper by controlling the air supply with valves. 
        The process takes around 10 seconds. 
        """
        print("[GRIPPER] Opening...") 
        BUFFER_SIZE = 1024
        MESSAGE = b"2"
        time.sleep(self.sleeptime) 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.robot_ip, self.robot_tcp_port))
        s.send(MESSAGE)
        print("[GRIPPER] Opening finished") 


    def close(self): 
        """
        Closes the gripper by controlling the air supply with valves. 
        The process takes around 10 seconds. 
        """
        print("[GRIPPER] Closing...") 
        BUFFER_SIZE = 1024
        MESSAGE = b"1"
        time.sleep(self.sleeptime)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.robot_ip, self.robot_tcp_port))
        s.send(MESSAGE)
        print("[GRIPPER] Closing finished") 



