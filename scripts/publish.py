#! /usr/bin/env python3

import sys

from src.jarvis import Jarvis
from src.tasks.publish_microservice import publish_microservice

if __name__ == '__main__':
    args = sys.argv[1::]

    jarvis = Jarvis([
        publish_microservice,
    ])

    jarvis.run(['jarvis', 'publish', args[0]])
