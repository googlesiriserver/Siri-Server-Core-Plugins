#!/usr/bin/python
# -*- coding: utf-8 -*-


from plugin import *
from siriObjects.systemObjects import ResultCallback
import uuid

class thatswhatsirisaid(Plugin):
    
    @register("en-US", ".*so.*big.*")
    def thatswhatsirisaid(self, speech, language, matchedRegex):
        if language == 'en-US':
            self.say("That's what she said!")
        self.complete_request()

    @register("en-US", ".*so.*long.*")
    def thatswhatsirisaid(self, speech, language, matchedRegex):
        if language == 'en-US':
            self.say("That's what she said!")
        self.complete_request()

    @register("en-US", ".*stick.*it.*in.*")
    def thatswhatsirisaid(self, speech, language, matchedRegex):
        if language == 'en-US':
            self.say("That's what she said!")
        self.complete_request()

    @register("en-US", ".*push.*it.*")
    def thatswhatsirisaid(self, speech, language, matchedRegex):
        if language == 'en-US':
            self.say("That's what she said!")
        self.complete_request()