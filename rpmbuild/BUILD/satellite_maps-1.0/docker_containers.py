#!/usr/bin/python3

import satellite_maps.helper as helper


class DockerContainers:

    def __init__(self):
        self.information = helper.convert('docker_containers.json')

    def display(self):
        for image in self.information:
            print(image.get('name'))