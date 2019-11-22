#!/usr/bin/env python3
# coding: utf-8

# Copyright (C) 2017, 2018 Robert Griesel
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class OpenWorksheetsListView(Gtk.ListBox):
        
    def __init__(self):
        Gtk.ListBox.__init__(self)

        self.items = dict()
        self.selected_row = None
        self.visible_items_count = 0

    def add_item(self, item):
        try: item = self.items[item.get_worksheet()]
        except KeyError:
            self.items[item.get_worksheet()] = item
            self.prepend(item)
        else: item.set_last_saved(item.last_saved)
        self.visible_items_count += 1
        self.show_all()
        
    def remove_item(self, item):
        del(self.items[item.get_worksheet()])
        self.remove(item)
        self.visible_items_count -= 1
        self.show_all()


