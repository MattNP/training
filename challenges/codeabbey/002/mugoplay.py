"""sum in loop"""
VAR1 = (
    "667 1192 825 201 1092 712 59 736 421 794" +
    "739 999 198 1017 680 861 200 819" +
    "725 730 276 677 965 311 678 363 1134 1017" +
    "93 1000 387 750 892 1202 942 684" +
    "614 991 119 1025")
VAR2 = VAR1.split(" ")
SUMA = 0
for e in VAR2:
    SUMA += int(e)
print SUMA
