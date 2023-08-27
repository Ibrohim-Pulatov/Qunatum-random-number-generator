import cirq
import numpy as np
count=int(input("enter a number"))
number = 0
def random_binary():
    circuit = cirq.Circuit()
    q0=cirq.LineQubit(0)
    q1=cirq.LineQubit(1)
    q2=cirq.LineQubit(2)
    q3=cirq.LineQubit(3)
    circuit.append(cirq.H(q0))
    circuit.append(cirq.H(q1))
    circuit.append(cirq.H(q2))
    circuit.append(cirq.H(q3))
    circuit.append(cirq.measure(q0,q1,q2,q3,key='a'))
    simulator = cirq.Simulator()
    state=str(simulator.run(circuit).measurements.get('a'))
    binary=state.strip("[]")

    return binary
def binary_to_decimal():
    binary=random_binary()
    if binary=="0 0 0 0":
        return 0

    elif binary=="0 0 0 1":
        return 1
    elif binary=="0 0 1 0":
        return 2
    elif binary=="0 0 1 1":
        return 3
    elif binary=="0 1 0 0":
        return 4
    elif binary=="0 1 0 1":
        return 5
    elif binary=="0 1 1 0":
        return 6
    elif binary=="0 1 1 1":
        return 7
    elif binary=="1 0 0 0":
        return 8
    elif binary=="1 0 0 1":
        return 9
    else:
        return binary_to_decimal()
for i in range(count):
    decimal=binary_to_decimal()
    while(i==0 and decimal==0 and count>1):
        decimal=binary_to_decimal()
    number=number+decimal*pow(10,i)
print(number)







