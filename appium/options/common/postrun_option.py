# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from typing import Optional

from .supports_capabilities import SupportsCapabilities

POSTRUN = 'postrun'


class PostrunOption(SupportsCapabilities):
    @property
    def postrun(self) -> Optional[str]:
        """
        :return: System script which is supposed to be executed upon
        driver session quit.
        """
        return self.get_capability(POSTRUN)

    @postrun.setter
    def postrun(self, value: str) -> None:
        """
        Set a system script to execute upon driver session quit.
        """
        self.set_capability(POSTRUN, value)