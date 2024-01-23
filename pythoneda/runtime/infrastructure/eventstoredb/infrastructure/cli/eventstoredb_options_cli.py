# vim: set fileencoding=utf-8
"""
pythoneda/runtime/infrastructure/eventstoredb/infrastructure/cli/eventstoredb_options_cli.py

This file defines the EventstoredbOptionsCli class.

Copyright (C) 2024-today rydnr's https://github.com/pythoneda-runtime-infrastructure/eventstoredb-infrastructure

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
from argparse import ArgumentParser
from pythoneda.shared import PrimaryPort
from pythoneda.shared.application import PythonEDA
from pythoneda.shared.infrastructure.cli import CliHandler


class EventstoredbOptionsCli(CliHandler, PrimaryPort):

    """
    A PrimaryPort used to gather EventStoreDB options.

    Class name: EventstoredbOptionsCli

    Responsibilities:
        - Parse the command-line to retrieve the EventStoreDB options.

    Collaborators:
        - pythoneda.runtime.infrastructure.eventstoredb.application.EventstoredbApp: They are notified back with the information retrieved from the command line.
    """

    def __init__(self):
        """
        Creates a new EventstoredbOptionsCli instance.
        """
        super().__init__("Provide the EventStoreDB options")

    @classmethod
    def priority(cls) -> int:
        """
        Retrieves the priority of this port.
        :return: The priority.
        :rtype: int
        """
        return 90

    @classmethod
    @property
    def is_one_shot_compatible(cls) -> bool:
        """
        Retrieves whether this primary port should be instantiated when
        "one-shot" behavior is active.
        It should return False unless the port listens to future messages
        from outside.
        :return: True in such case.
        :rtype: bool
        """
        return True

    def add_arguments(self, parser: ArgumentParser):
        """
        Defines the specific CLI arguments.
        :param parser: The parser.
        :type parser: argparse.ArgumentParser
        """
        parser.add_argument(
            "-p",
            "--http-port",
            required=False,
            help="The HTTP port",
        )

        parser.add_argument(
            "-t",
            "--tcp-port",
            required=False,
            help="The TCP/IP port",
        )

        parser.add_argument(
            "-s",
            "--cluster-size",
            required=False,
            help="The cluster size",
        )

        parser.add_argument(
            "-r",
            "--run-projections",
            required=False,
            help="Which projections to run",
        )

        parser.add_argument(
            "-i",
            "--insecure",
            required=False,
            help="Whether to run EventStoreDB in insecure mode",
        )

        parser.add_argument(
            "-a",
            "--enable-atom-over-http",
            required=False,
            help="Whether to enable Atom over HTTP",
        )

    async def handle(self, app: PythonEDA, args):
        """
        Processes the command specified from the command line.
        :param app: The PythonEDA instance.
        :type app: pythoneda.shared.application.PythonEDA
        :param args: The CLI args.
        :type args: argparse.args
        """
        await app.accept_options(
            {
                "http-port": args.http_port,
                "tcp-port": args.tcp_port,
                "cluster-size": args.cluster_size,
                "run-projections": args.run_projections,
                "insecure": args.insecure,
            }
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
