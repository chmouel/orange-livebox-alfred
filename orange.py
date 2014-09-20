# -*- coding: utf-8 -*-
# Author: Chmouel Boudjnah <chmouel@chmouel.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import argparse
import sys
import urllib2

SERVER = "192.168.1.16"
REMOTE_URL = "http://%s:8080/remoteControl/cmd" % SERVER

OPERATIONS = {
    "UNIQUE": 0,
    "PROLONGER": 1,
    "RELACHE_APRES": 2,
}


CODE_TOUCHE = {
    "ON/OFF": 116,
    "0": 512,
    "1": 513,
    "2": 514,
    "3": 515,
    "4": 516,
    "5": 517,
    "6": 518,
    "7": 519,
    "8": 520,
    "9": 521,
    "CH+": 402,
    "CH-": 403,
    "VOL+": 115,
    "VOL-": 114,
    "MUTE": 113,
    "UP": 103,
    "DOWN": 108,
    "LEFT": 105,
    "RIGHT": 116,
    "OK": 352,
    "BACK": 158,
    "MENU": 139,
    "PLAY/PAUSE": 164,
    "FBWD": 168,
    "FFWD": 159,
    "REC": 167,
    "VOD": 393
}


def list_available_keys():
    xml = "<items>"
    for x in CODE_TOUCHE.keys():
        xml += """<item uid="%(key)s" arg="%(key)s">
  <title>%(key)s</title>
  <subtitle>Press Key %(key)s</subtitle>
  <autocomplete>%(key)s</autocomplete>
</item>""" % dict(key=x)
    xml += "</items>"
    print(xml)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', dest='time', type=int, default=1,
                        help="Run the action number of times (default: 1)")
    parser.add_argument('-l', dest='list', action='store_true',
                        help="List all keys avail for MacOSX alfred")
    parser.add_argument('action', nargs="?", default="NONE")
    args = parser.parse_args()
    if args.list:
        list_available_keys()
        sys.exit(0)
    if args.action == "NONE":
        print("Besoin d'une action, du genre: " + " ".join(CODE_TOUCHE.keys()))
        sys.exit(1)

    if args.action not in CODE_TOUCHE:
        print("Besoin d'une action valide, du genre: " +
              " ".join(CODE_TOUCHE.keys()))
        sys.exit(1)

    for x in range(args.time):
        urllib2.urlopen(REMOTE_URL + "?operation=01&key=%s&mode=0" %
                        CODE_TOUCHE[args.action])

if __name__ == '__main__':
    main()


