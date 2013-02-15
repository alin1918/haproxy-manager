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


class ConfigFiles(object):

    def __init__(self, path="/etc/haproxy/conf.d/"):
        self.tpl = os.path.join(os.path.dirname(__file__), 'templates/%s.tmpl')
        self.path = path

    def global_writer(self, opts={}):
        name = "global"
        file_name = "00-%s" % name
        self._write(name, file_name, opts)

    def frontend_writer(self, opts={}):
        name = "frontend"
        file_name = "90-%s-%s" % (name, opts["name"])
        self._write(name, file_name, opts)

    def backend_writer(self, opts={}):
        name = "backend"
        file_name = "90-%s-%s" % (name, opts["name"])
        self._write(name, file_name, opts)

    def read(self, ftype, fname):
        file_name = self.file_name_for(ftype, fname)

        with open("%s/%s" % (self.path, file_name)) as f:
            file_params = dict([
                map(lambda x: x.strip(), i.strip().split(" ", 1))
                for i in f.readlines()
            ])

            return file_params

    def file_name_for(self, ftype, fname):
        if ftype == "frontend" or ftype == "backend":
            path = "90-%s-%s.cfg" % (ftype, fname)
        else:
            path = "00-%s.cfg" % ftype

        return path

    def _write(self, template, file_name, opts={}):
        render = Template(file=self.tpl % template, searchList=[opts])

        with open(self.path + file_name + ".cfg", 'w') as file:
            file.write(str(render))
