import pytest
import subprocess
import sys
import threading
import pandas as pd
import math

def exec_command(command, cwd=None):
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               universal_newlines=True)
    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            for output in process.stdout.readlines():
                print(output.strip())
            break


def test_example_one():
    command = "np_shape_lab -R 10 -q 600 -c 0.005 -t 1 -v 1 -b 40 -s 40 -S 25000 -D 4 -F n"
    command_list = command.split();
    exec_command(command_list, cwd="..")
    df = pd.read_csv('outfiles/area.dat', sep=r"\s+", header=None)
    t = df.iat[-1, 1]
    assert math.isclose(t, 15.675, rel_tol=1e-1)

    df = pd.read_csv('outfiles/energy_in_parts_kE_bE_sE_tE_ljE_esE.dat', sep=r"\s+", header=None)
    t = df.iat[-1, 4]
    assert math.isclose(t, 380.971, rel_tol=1e-1)


def test_example_two():
    command = "np_shape_lab -R 10 -q 600 -c 0.01 -t 1 -v 1 -b 40 -s 40 -S 25000 -D 4 -F n"
    command_list = command.split();
    exec_command(command_list, cwd="..")
    df = pd.read_csv('outfiles/area.dat', sep=r"\s+", header=None)
    t = df.iat[-1, 1]
    assert math.isclose(t, 13.2595, rel_tol=1e-2)

    df = pd.read_csv('outfiles/energy_in_parts_kE_bE_sE_tE_ljE_esE.dat', sep=r"\s+", header=None)
    t = df.iat[-1, 4]
    assert math.isclose(t, 322.264, rel_tol=1e-1)


def test_example_three():
    command = "np_shape_lab -R 10 -q 600 -N 2 -p 0.5 -c 0.005 -t 1 -v 1 -b 40 -s 40 -S 25000 -D 4 -F n"
    command_list = command.split();
    exec_command(command_list, cwd="..")
    df = pd.read_csv('outfiles/area.dat', sep=r"\s+", header=None)
    t = df.iat[-1, 1]
    assert math.isclose(t, 12.5275, rel_tol=1e-2)

    df = pd.read_csv('outfiles/energy_in_parts_kE_bE_sE_tE_ljE_esE.dat', sep=r"\s+", header=None)
    t = df.iat[-1, 4]
    assert math.isclose(t, 304.473, rel_tol=1e-1)


def test_example_four():
    command = "np_shape_lab -R 10 -q 0 -c 0.005 -t 0 -v 0 -b 1 -s 1000 -S 25000 -D 4 -F n -B y"
    command_list = command.split();
    exec_command(command_list, cwd="..")
    df = pd.read_csv('outfiles/area.dat', sep=r"\s+", header=None)
    t = df.iat[-1, 1]
    assert math.isclose(t, 12.3795, rel_tol=1e-2)

    df = pd.read_csv('outfiles/energy_in_parts_kE_bE_sE_tE_ljE_esE.dat', sep=r"\s+", header=None)
    t = df.iat[-1, 3]
    assert math.isclose(t, 5.87409, rel_tol=1e-1)

def test_example_five():
    command = "np_shape_lab -R 10 -q 600 -N 2 -p 0.5 -c 0.005 -t 1 -v 1 -b 40 -s 40 -S 25000 -D 4 -F n -H y"
    command_list = command.split();
    exec_command(command_list, cwd="..")
    df = pd.read_csv('outfiles/area.dat', sep=r"\s+", header=None)
    t = df.iat[-1, 1]
    assert math.isclose(t, 12.5099, rel_tol=1e-2)

    df = pd.read_csv('outfiles/energy_in_parts_kE_bE_sE_tE_ljE_esE.dat', sep=r"\s+", header=None)
    t = df.iat[-1, 6]
    assert math.isclose(t, 304.044, rel_tol=1e-1)


