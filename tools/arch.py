# Copyright 2020 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Architecture-specific information."""

import collections
import json


class Arch(
    collections.namedtuple(
        "Arch",
        [
            "arch_nr",
            "arch_name",
            "bits",
            "syscalls",
            "constants",
            "syscall_groups",
        ],
    )
):
    """Holds architecture-specific information."""

    def truncate_word(self, value):
        """Return the value truncated to fit in a word."""
        return value & self.max_unsigned

    @property
    def min_signed(self):
        """The smallest signed value that can be represented in a word."""
        return -(1 << (self.bits - 1))

    @property
    def max_unsigned(self):
        """The largest unsigned value that can be represented in a word."""
        return (1 << self.bits) - 1

    @staticmethod
    def load_from_json(json_path):
        """Return an Arch from a .json file."""
<<<<<<< HEAD   (113ad6 Suppress errors about unused -c arguments)
        with open(json_path, 'r') as json_file:
||||||| BASE
=======
        with open(json_path, "rb") as json_file:
>>>>>>> BRANCH (7bdbb4 system: cleanup leaked FILE)
            return Arch.load_from_json_bytes(json_file.read())

    @staticmethod
    def load_from_json_bytes(json_bytes):
        """Return an Arch from a json string."""
        constants = json.loads(json_bytes)
        return Arch(
            arch_nr=constants["arch_nr"],
            arch_name=constants["arch_name"],
            bits=constants["bits"],
            syscalls=constants["syscalls"],
            constants=constants["constants"],
            syscall_groups=constants.get("syscall_groups", {}),
        )
