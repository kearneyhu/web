# Project Title

Contains the flask code to host a webserver that enables video streaming from a webcam. 

## Getting Started

1. Take note of which port the flask webserver is using. Default port is 5000.
2. Now you need to port forward everything. Don't use the same inbound port as the port to be forwarded. 
   For example, to port forward for the flask server, port forward such that [your public ip]:5001 points to [webserver host local ip]:5000
   For example, to port forward for the motion, port forward such that [your public ip]:8082 points to [webserver host local ip]:8081
3. Edit the html files in /flaskserver/templates such that the public ip addresses pointing to the webcam stream corresponds to your own public ip


### Prerequisites

Make sure the software used to stream video to a certain port "motion" is set up. Take note of which port "motion" is streaming video to. Default port is 8081.

