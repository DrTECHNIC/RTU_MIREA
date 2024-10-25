from types import NoneType

import pytest
from tarfile import TarFile
from terminal import Terminal
from application import Application

@pytest.fixture
def terminal():
    name = "user"
    fs_path = "vfs.tar"
    t = Terminal(name, fs_path, TarFile(fs_path, "a"))
    return t


def test_init_1(terminal):
    assert terminal.application is None


def test_init_2(terminal):
    assert terminal.filesystem is not None


def test_link(terminal):
    terminal.link(Application(terminal))
    assert terminal.application is not None


def test_cd_1(terminal):
    assert terminal.cd([]) == ""


def test_cd_2(terminal):
    assert terminal.cd(["dir_1/.."]) == ""


def test_cd_3(terminal):
    assert terminal.cd(["dir_1"]) == "dir_1/"


def test_ls_1(terminal):
    assert NoneType


def test_ls_2(terminal):
    terminal.path = terminal.cd(["dir_1"])
    assert NoneType


def test_ls_3(terminal):
    assert NoneType


def test_cat_1(terminal):
    assert NoneType


def test_cat_2(terminal):
    assert NoneType


def test_cat_3(terminal):
    terminal.cur_d = terminal.cd(["dir_3"])
    assert NoneType


def test_touch_1(terminal, capfd):
    terminal.touch(["test.txt"])
    assert NoneType


def test_touch_2(terminal, capfd):
    terminal.touch(["test"])
    assert NoneType


def test_touch_3(terminal, capfd):
    terminal.touch(["test.png"])
    assert NoneType