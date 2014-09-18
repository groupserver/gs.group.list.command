# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import unicode_literals
from enum import Enum


class CommandResult(Enum):
    '''An enumeration of the different results from processing a command.'''
    # __order__ is only needed in 2.x
    __order__ = 'notACommand commandStop commandContinue '

    #: The ``Subject`` did not contain a command
    notACommand = 0

    #: The command was processed, and processing of this email should stop.
    commandStop = 1

    #: The command was processed, and processing of this email should
    #: continue.
    commandContinue = 2
