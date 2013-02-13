#!/usr/bin/env python
# Copyright 2013 Locaweb.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# @author: Willian Molinari (PotHix), Locaweb.

import os

from Cheetah.Template import Template


class Writer(object):

    def __init__(self, output_path):
        self.tpl = os.path.join(os.path.dirname(__file__), 'templates/%s.tmpl')
        self.output_path = "/etc/haproxy/conf.d/"

    def write(self, template, output_path, options={}):
        render = Template(file=self.tpl % template, searchList=[options])

        with open(output_path, 'w') as file:
            file.write(str(render))

    def global_writer(self, opts={}):
        name = "global"
        file_name = "00-%s" % name
        self.write(self.name, self.output_path + file_name + ".conf", opts)

    def frontend_writer(self, opts={}):
        name = "frontend"
        file_name = "90-%s-%s" % (name, opts["name"])
        self.write(self.name, self.output_path + file_name + ".conf", opts)

    def backend_writer(self, opts={}):
        name = "frontend"
        file_name = "90-%s-%s" % (name, opts["name"])
        self.write(self.name, self.output_path + file_name + ".conf", opts)
