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
from gs.group.list.command.processor import ProcessEmailCommand
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
        pec = ProcessEmailCommand(self.fauxGroup, e)
        self.assertEqual(command, pec.command)

    def test_command_lowercase(self):
        'Test that we extract the lower-case command.'
        command = 'Test'
        e = self.get_email(command)
        pec = ProcessEmailCommand(self.fauxGroup, e)
        self.assertEqual(command.lower(), pec.command)
