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
from email.parser import Parser
from unittest import TestCase
from gs.group.list.command.processor import (ProcessEmailCommand,
                                             process_command)
from gs.group.list.command.result import CommandResult
from .faux import FauxGroup


class TestProcessEmailCommand(TestCase):

    def setUp(self):
        self.fauxGroup = FauxGroup()

    @staticmethod
    def get_email(subject):
        retval = Parser().parsestr(
            'From: <member@example.com>\n'
            'To: <group@example.com>\n'
            'Subject: {0}\n'
            '\n'
            'Body would go here\n'.format(subject))
        return retval

    def test_command(self):
        'Test that the command is extracted from the Subject'
        command = 'test'
        e = self.get_email(command)
        pec = ProcessEmailCommand(self.fauxGroup, e, None)
        self.assertEqual(command, pec.command)

    def test_command_lowercase(self):
        'Test that we extract the lower-case command.'
        command = 'Test'
        e = self.get_email(command)
        pec = ProcessEmailCommand(self.fauxGroup, e, None)
        self.assertEqual(command.lower(), pec.command)

    def test_process_stop(self):
        'Test that we can process the (fake) Stop command'
        command = 'Stop'
        e = self.get_email(command)
        pec = ProcessEmailCommand(self.fauxGroup, e, None)
        r = pec.process()
        self.assertEqual(CommandResult.commandStop, r)

    def test_process_continue(self):
        'Test that we can process the (fake) Continue command'
        command = 'Continue'
        e = self.get_email(command)
        pec = ProcessEmailCommand(self.fauxGroup, e, None)
        r = pec.process()
        self.assertEqual(CommandResult.commandContinue, r)

    def test_not_a_command(self):
        'Test an email that does not contain a command'
        command = 'This is a dead parrot'
        e = self.get_email(command)
        pec = ProcessEmailCommand(self.fauxGroup, e, None)
        r = pec.process()
        self.assertEqual(CommandResult.notACommand, r)


class TestProcessCommandFunction(TestCase):
    'Test the process_email function'

    def setUp(self):
        self.fauxGroup = FauxGroup()

    def test_process_email(self):
        'Test that we correctly process an email'
        e = TestProcessEmailCommand.get_email('Putting the boot in')
        r = process_command(self.fauxGroup, e, None)
        self.assertEqual(CommandResult.notACommand, r)

    def test_process_string(self):
        'Test that we correctly process a string'
        s = ('From: <member@example.com>\n'
             'To: <group@example.com>\n'
             'Subject: Putting the boot in\n'
             '\n'
             'Body would go here\n')
        r = process_command(self.fauxGroup, s, None)
        self.assertEqual(CommandResult.notACommand, r)
