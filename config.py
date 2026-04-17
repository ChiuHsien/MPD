
import torch

# ATR2IDX = {
#     'right': 0,
#     'left': 1,
# }
ATR2IDX = {
    "UNSPECIFIED": 0,
    "Dont_Care": 1,
    "Short": 2,
    "Open": 3,
    "Space": 4,
    "Line": 5,
    "Nick": 6,
    "Protrusion": 7,
    "Island": 8,
    "Pinhole": 9,
    "Drill": 10,
    "LaserDrillPlated": 11,
    "A0": 12,
    "A1": 13,
    "A2": 14,
    "A9": 15,
    "B0": 16,
    "C0": 17,
    "D0": 18,
    "E0": 19,
    "E1": 20,
    "F0": 21,
    "F1": 22,
    "H0": 23,
    "I0": 24,
    "J0": 25,
    "J1": 26,
    "K0": 27,
    "L0": 28,
    "L1": 29,
    "M1": 30,
    "N0": 31,
    "O1": 32,
    "O0": 33,
    "P0": 34,
    "Q0": 35,
    "R0": 36,
    "S1": 37,
    "S2": 38,
    "S3": 39,
    "S4": 40,
    "S6": 41,
    "S8": 42,
    "T0": 43,
    "U0": 44,
    "V0": 45,
    "X0": 46,
    "Y0": 47,
    "Y1": 48,
    "Z0": 49,
    "U1": 50,
    "Z9": 51,
    "AOS": 52,
    "L2": 53,
    "L3": 54,
    "L4": 55,
    "S5": 56,
    "Next": 57,
}
OBJ2IDX = {
    'group0': 0,
    'group1': 1,
    'group2': 2,
    'group3': 3,
    'group4': 4,
}
# OBJ2IDX = {
#     'Group1': 0,
#     'Group2': 1,
#     'Group3': 2,
#     'Group4': 3,
#     'Group5': 4,
# }
IDX2ATR = {v : k for k, v in ATR2IDX.items()}

IDX2OBJ = {v : k for k, v in OBJ2IDX.items()}

classes = []
for va in IDX2ATR.values():
    for vo in IDX2OBJ.values():
        classes.append(f"{va} {vo}")

CLS2IDX = {classes[i] : i for i in range(len(classes))}
