#!/usr/bin/python3

import os
import json
import colored as c

greenbluetext = c.fg(2) + c.bg(18) + c.attr(1)
orangetext = c.fg(130) + c.attr(1)
orangebg = c.fg(232) + c.bg(130) + c.attr(4) + c.attr(1)
bluebg = c.fg(232) + c.bg(4) + c.attr(4) + c.attr(1)
bluetext = c.fg(4) + c.attr(1)
greentext = c.fg(64) + c.attr(1)
greenbright = c.fg(10) + c.attr(1)
magentatext = c.fg(125) + c.attr(1)
magentabg = c.fg(232) + c.bg(125) + c.attr(1)
tealtext = c.fg(30) + c.attr(1)
tealbg = c.fg(232) + c.bg(30) + c.attr(4) + c.attr(1)
darkredtext = c.fg(88) + c.attr(1)
darkredbg = c.fg(232) + c.bg(88) + c.attr(4) + c.attr(1)
yellowtext = c.fg(142) + c.attr(1)
redtext = c.fg(196) + c.attr(1)
goldtext = c.fg(220) + c.attr(1)
slatebluetext = c.fg(99) + c.attr(1)
reset = c.attr(0)
boldwhite = c.fg(255) + c.attr(1)
blink = c.attr(5)


def convert(file_name):
    with open(file_name) as file:
        datastore = json.load(file)
        information = datastore["results"]
        return information


def directory_content(file_prefix):
    queried_items = []
    ls_output = os.listdir(os.getcwd())
    for x in ls_output:
        if x.startswith(file_prefix):
            queried_items.append(x)
    return queried_items


def get_my_description(data):
    #if data.get('description'):
    #    return data.get('description')
    #return "TBD"
    return data.get('description') if data.get('description') is not None else 'TBD'