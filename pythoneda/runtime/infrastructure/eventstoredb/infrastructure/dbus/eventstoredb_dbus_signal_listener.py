# vim: set fileencoding=utf-8
"""
pythoneda/runtime/infrastructure/eventstoredb/infrastructure/dbus/eventstoredb_dbus_signal_listener.py

This file defines the EventstoredbDbusSignalListener class.

Copyright (C) 2024-today rydnr's pythoneda-runtime-infrastructure/eventstoredb-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from dbus_next import BusType, Message
from pythoneda.shared.runtime.infrastructure.events.eventstoredb import (
    EventstoredbBootRequested,
)
from pythoneda.shared.runtime.infrastructure.events.infrastructure.eventstoredb.dbus import (
    EventstoredbDbusBootRequested,
)
from pythoneda.shared.infrastructure.dbus import DbusSignalListener
from typing import Dict


class EventstoredbDbusSignalListener(DbusSignalListener):

    """
    A Port that listens to EventStoreDB-relevant d-bus signals.

    Class name: EventstoredbDbusSignalListener

    Responsibilities:
        - Connect to d-bus.
        - Listen to signals relevant to EventStoreDB.

    Collaborators:
        - pythoneda.shared.application.PythonEDA: Receives relevant domain events.
        - pythoneda.runtime.infrastructure.events.infrastructure.eventstoredb.dbus.EventstoredbDbusBootRequested
    """

    def __init__(self):
        """
        Creates a new EventstoredbDbusSignalListener instance.
        """
        super().__init__()

    def signal_receivers(self, app) -> Dict:
        """
        Retrieves the configured signal receivers.
        :param app: The PythonEDA instance.
        :type app: pythoneda.shared.application.PythonEDA
        :return: A dictionary with the signal name as key, and the tuple interface and bus type as the value.
        :rtype: Dict
        """
        result = {}
        key = self.__class__.full_class_name(EventstoredbBootRequested)
        result[key] = [EventstoredbDbusBootRequested, BusType.SYSTEM]
        return result


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
