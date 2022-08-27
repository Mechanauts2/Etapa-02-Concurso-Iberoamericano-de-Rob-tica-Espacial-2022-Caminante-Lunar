{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52e99be1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Se importan las librerias necesarias\n",
    "import math\n",
    "import numpy as np\n",
    "import rospy\n",
    "import time\n",
    "from sensor_msgs.msg import LaserScan\n",
    "from geometry_msgs.msg import Twist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65135603",
   "metadata": {},
   "outputs": [],
   "source": [
    "# A collection of conversion function for extracting numpy arrays from messages. http://wiki.ros.org/ros_numpy\n",
    "import ros_numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e118f69c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Iniciamos el nodo y se define el publisher de la velocidad a la que se movera la base del robot\n",
    "rospy.init_node('evasion_notebook_node') \n",
    "base_vel_pub = rospy.Publisher('/hsrb/command_velocity', Twist, queue_size=10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "834dbd09",
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time_1 = rospy.Time.now().to_sec()  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74a07511",
   "metadata": {},
   "outputs": [],
   "source": [
    "def move_base_vel(vx, vy, vw):\n",
    "    twist = Twist()\n",
    "    twist.linear.x = vx\n",
    "    twist.linear.y = vy\n",
    "    twist.angular.z = vw \n",
    "    base_vel_pub.publish(twist)\n",
    "\n",
    "def move_base(x,y,yaw,timeout=5):\n",
    "    start_time = rospy.Time.now().to_sec()\n",
    "    while rospy.Time.now().to_sec() - start_time < timeout:  \n",
    "        move_base_vel(x, y, yaw)    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7a39503",
   "metadata": {},
   "outputs": [],
   "source": [
    "def move_forward():\n",
    "    move_base(0.10,0,0,3)\n",
    "def move_backward():\n",
    "    move_base(-0.10,0,0,3)\n",
    "def turn_left():\n",
    "    move_base(0.0,0,0.12*np.pi,4)\n",
    "def turn_right():\n",
    "    move_base(0.0,0,-0.12*np.pi,4)\n",
    "def move_forward_1():\n",
    "    move_base(0.10,0,0,45)\n",
    "def move_backward_1():\n",
    "    move_base(-0.10,0,0,40)\n",
    "def turn_right_1():\n",
    "    move_base(0.0,0,-0.12*np.pi,3.5)\n",
    "def turn_left_1():\n",
    "    move_base(0.0,0,0.12*np.pi,3.5)\n",
    "def move_backward_2():\n",
    "    move_base(-0.10,0,0,40)\n",
    "def move_forward_2():\n",
    "    move_base(0.10,0,0,40)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a92380a",
   "metadata": {},
   "outputs": [],
   "source": [
    "move_forward()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7562335",
   "metadata": {},
   "outputs": [],
   "source": [
    "turn_right()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b280ef7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "move_forward_1()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2ed69b3d",
   "metadata": {},
   "outputs": [],
   "source": [
    "turn_right_1()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea6eabd9",
   "metadata": {},
   "outputs": [],
   "source": [
    "move_forward_2()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e95aa93d",
   "metadata": {},
   "outputs": [],
   "source": [
    "start_time = rospy.Time.now().to_sec()  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c0cc096",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tf2_ros\n",
    "tfBuffer = tf2_ros.Buffer()\n",
    "listener = tf2_ros.TransformListener(tfBuffer)\n",
    "def get_coords ():\n",
    "    trans = tfBuffer.lookup_transform('map', 'base_link', rospy.Time())\n",
    "    return trans\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "754ded50",
   "metadata": {},
   "outputs": [],
   "source": [
    "coords_start= get_coords()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a2a8915",
   "metadata": {},
   "outputs": [],
   "source": [
    "coords_end= get_coords()\n",
    "coords_start.transform.translation,coords_end.transform.translation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76dbdc69",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(coords_start.transform.translation,coords_end.transform.translation)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd8d8152",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(start_time_1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "204dfeda",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(start_time)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
