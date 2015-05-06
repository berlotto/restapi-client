# -*- encoding: utf-8 -*-
#

from restapi import Client

ROOT = "http://localhost:8000"

api = Client(ROOT)

print(api.votes.get())
