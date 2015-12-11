# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2014, 2015 OnlineGroups.net and Contributors.
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
from __future__ import absolute_import, unicode_literals, print_function
from email.message import Message
from email.parser import Parser
import shlex
import sys
from zope.cachedescriptors.property import Lazy
from zope.component import queryAdapter
from .interfaces import IEmailCommand
from .result import CommandResult


class ProcessEmailCommand(object):
    '''Process an email command

:param group: A group object.
:param email: An email message.
:type email: :class:`email.message.Message`'''

    def __init__(self, group, email, request):
        self.group = group
        self.email = email
        self.request = request

    @Lazy
    def command(self):
        retval = None
        subject = self.email.get('Subject', '')
        try:
            splitSubject = shlex.split(subject)
        except ValueError:
            splitSubject = None
        if splitSubject:
            components = [c.lower() for c in splitSubject
                          if c.lower() != 're:']
            retval = components[0] if components else None
        return retval

    def process(self):
        '''Process the command in the email

:returns: The result of processing the command
:rtype: ``.result.CommandResult``'''
        retval = CommandResult.notACommand
        if self.command:
            a = queryAdapter(self.group, IEmailCommand, self.command)
            if a:
                retval = a.process(self.email, self.request)
        return retval


STRING = basestring if (sys.version_info < (3, )) else str


def process_command(group, email, request):
    '''Process a command in an email message

:param obj group: The group that recieved the email message.
:param email: The email message that was recieved (which may or may not
              contain a command).
:type email: str or :class:`email.message.Message`
:param obj request: The current browser request object.
:returns: If a command was processed, and if email processing should
          continue.
:rtype: :class:`.CommandResult`

When an email is recieved it needs to checked to see if its ``Subject``
header is command, and the command executed if necessary. The
:func:`.process_command` function performs both of these tasks. The result
will be either

* :attr:`.CommandResut.notACommand` if the email is a normal message,
* :attr:`.CommandResut.commandStop` if the email contained a command and
  processing should stop, or
* :attr:`.CommandResut.commandContinue` if the email contained a command and
  processing should continue.
'''
    if isinstance(email, Message):
        e = email
    elif isinstance(email, STRING):
        p = Parser()
        e = p.parsestr(email)
    else:
        m = 'email must be a string or a email.message.Message'
        raise TypeError(m)
    emailProcessor = ProcessEmailCommand(group, e, request)
    retval = emailProcessor.process()
    return retval
