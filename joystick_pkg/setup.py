import glob
import os

from setuptools import setup
from setuptools import find_packages

package_name = 'joystick_pkg'
share_dir = 'share/' + package_name

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share_dir', ['package.xml']),
        (share_dir + '/launch', glob.glob(os.path.join('launch', '*.launch.py'))),
        (share_dir + '/param', glob.glob(os.path.join('param', '*.yaml')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='leejeonghun',
    maintainer_email='jhleee1214@gmail.com',
    keywords=['ROS2'],
    description='ROS2 joystick with python',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtlesim_joy = joystick_pkg.turtlesim_joy.turtlesim_joy:main',
            'turtlebot3_joy = joystick_pkg.turtlebot3_joy.turtlebot3_joy:main',
        ],
    },
)
