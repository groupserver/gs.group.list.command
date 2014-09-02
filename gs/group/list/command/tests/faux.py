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
from __future__ import absolute_import, unicode_literals
from zope.component import getGlobalSiteManager
from zope.interface import Interface, implementer
from gs.group.list.command.interfaces import IEmailCommand
from gs.group.list.command.result import CommandResult


class IFauxGroup(Interface):
    'This is not a group'


@implementer(IFauxGroup)
class FauxGroup(object):
    'This is not a group'


class FauxCommand(object):
    retval = None

    def __init__(self, group):
        self.group = group

    @classmethod
    def process(cls, email, request):
        return cls.retval


@implementer(IEmailCommand)
class FauxCommandStop(FauxCommand):
    retval = CommandResult.commandStop


@implementer(IEmailCommand)
class FauxCommandContinue(FauxCommand):
    retval = CommandResult.commandContinue


gsm = getGlobalSiteManager()
gsm.registerAdapter(FauxCommandStop, (IFauxGroup,), IEmailCommand, 'stop')
gsm.registerAdapter(FauxCommandContinue, (IFauxGroup,), IEmailCommand,
                    'continue')
