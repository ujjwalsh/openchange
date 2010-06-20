#!/usr/bin/python

from openchange import mapi

SPropValue = mapi.SPropValue()
SPropValue.add(mapi.PR_SUBJECT, "This is a test")
SPropValue.add(mapi.PR_VERSIONING_FLAGS, 2)
SPropValue.add(mapi.PR_IMPORTANCE, 4096)
SPropValue.add(mapi.PR_MESSAGE_TO_ME, True)
SPropValue.add(mapi.PR_MESSAGE_CC_ME, False)
SPropValue.add(mapi.PR_CURRENT_VERSION, 0x0f10000000000012)

SPropValue.dump("Python: ")

