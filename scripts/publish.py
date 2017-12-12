#! /usr/bin/env python3

import sys

from riddles.jarvis.jarvis import Jarvis
from riddles.jarvis.tasks.publish_microservice import publish_microservice_latest

if __name__ == '__main__':
    args = sys.argv[1::]

    jarvis = Jarvis([
        publish_microservice_latest,
    ])

    jarvis.run(['jarvis', 'publish', 'image', args[0]])
