import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic_gates import *

def test_label_1():
    gate = ANDGate("TestGate")
    assert gate.get_label() == "TestGate"

def test_label_2():
    gate = ANDGate("")
    assert gate.get_label() == ""

def test_set_pins():
    gate = ANDGate("TestGate")
    gate.set_pins(1, 0)
    assert gate.get_pin_a() == 1
    assert gate.get_pin_b() == 0

def test_set_next_pin_1():
    gate = ANDGate("TestGate")
    gate.set_pin_a(1)
    gate.set_next_pin(0)
    assert gate.get_pin_a() == 1
    assert gate.get_pin_b() == 0

def test_set_next_pin_2():
    gate = ANDGate("TestGate")
    gate.set_next_pin(0)
    assert gate.get_pin_a() == 0
    assert gate.get_pin_b() == None

def test_set_next_pin_3():
    gate = ANDGate("TestGate")
    gate.set_pin_a(1)
    gate.set_pin_b(1)
    gate.set_next_pin(0)
    assert gate.get_pin_a() == 1
    assert gate.get_pin_b() == 1

def test_and_gate_1():
    gate = ANDGate("TestGate")
    gate.set_pins(1, 0)
    assert gate.get_output() == 0

def test_and_gate_2():
    gate = ANDGate("TestGate")
    gate.set_pins(1, 1)
    assert gate.get_output() == 1

def test_or_gate_1():
    gate = ORGate("TestGate")
    gate.set_pins(1, 0)
    assert gate.get_output() == 1

def test_or_gate_2():
    gate = ORGate("TestGate")
    gate.set_pins(0, 0)
    assert gate.get_output() == 0

def test_xor_gate_1():
    gate = XORGate("TestGate")
    gate.set_pins(1, 1)
    assert gate.get_output() == 0

def test_xor_gate_2():
    gate = XORGate("TestGate")
    gate.set_pins(1, 0)
    assert gate.get_output() == 1

def test_nand_gate_1():
    gate = NANDGate("TestGate")
    gate.set_pins(1, 0)
    assert gate.get_output() == 1

def test_nand_gate_2():
    gate = NANDGate("TestGate")
    gate.set_pins(1, 1)
    assert gate.get_output() == 0

def test_not_gate_1():
    gate = NOTGate("TestGate")
    gate.set_pin(0)
    assert gate.get_output() == 1

def test_not_gate_2():
    gate = NOTGate("TestGate")
    gate.set_pin(1)
    assert gate.get_output() == 0

def test_nor_gate_1():
    gate = NORGate("TestGate")
    gate.set_pins(1, 0)
    assert gate.get_output() == 0

def test_nor_gate_2():
    gate = NORGate("TestGate")
    gate.set_pins(0, 0)
    assert gate.get_output() == 1

def test_connector():
    gate1 = ANDGate("Test1")
    gate1.set_pins(0, 1)
    gate2 = ORGate("Test2")
    gate2.set_pins(1, 0)
    conn = Connector(gate1, gate2)
    assert conn.from_gate == gate1
    assert conn.to_gate == gate2