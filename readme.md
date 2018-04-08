# Landing Rocket Lander with DDSM

This is an implementation of the Rocket Lander Environment using [Deep Deterministic Selective Memory](https://github.com/FitMachineLearning/FitML).

The Author for this environment is [arex18](https://github.com/arex18/rocket-lander)


### Results

The agent starts to land regularily after 500 episodes.
You can see the agent in action [here](https://www.youtube.com/watch?v=RdRnBCFMVd4)

![environment 3](https://user-images.githubusercontent.com/16338481/33860598-870fd702-ded1-11e7-8bdb-86fa01e2db47.JPG)


### How to run

To run the simulation follow the steps below:
* Download or clone the repository https://github.com/FitMachineLearning/rocket-lander
* Install the necessary dependencies. Usually *pip install <package name>*
* run the project with the following command *python Main_Sim.py*


### Prerequisites

List of libraries needed to run the project: (some, e.g. cvxpy require other pre-requisites). Windows users head to the 
life-saving list of [Windows Python Extension Libraries](Unofficial Windows Binaries for Python Extension Packages)
to install cvxpy and any other failing pip installs.

```
tensorflow
matplotlib
gym
numpy
Box2D
logging
pyglet
cvxpy
abc
concurrent

python pip install PATH_TO_YOUR_DOWNLOADED_LIBRARY (ending in whl)
```
### AUtho: Who is Michel Aka
Michel is an AI researcher and a graduate from University of Montreal who currently works in the Healthcare industry.

References: https://gym.openai.com/envs/LunarLander-v2/

## License

This project is licensed under the MIT License.
