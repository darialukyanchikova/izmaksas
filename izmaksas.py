a = ["kapučīno", "caffè latte", "caffè macchiato", "nevēlos iegādāties kafiju"]
b = [3, 3, 2, 0]
c = input("Kādu kafiju Jūs vēlaties pasūtīt? - ")
if c in a: print(b[a.index(c)], "eiro")
else: print("Tādu kafiju nav iespējams iegādāties")
d = ["govs pienu", "mandeļu pienu", "bez piena"]
e = [1, 1, 0]
f = input("Kādu pienu Jūs vēlaties pievienot kafijai? - ")
if f in d: print(e[d.index(f)], "eiro")
else: print("Tādu pienu nav iespējas pievienot")
g = ["medus kūku", "šokolādes kūku", "tiramisu"]
h = [3, 3, 4]
i = input("Kādu kūku Jūs vēlaties pasūtīt? - ")
if i in g: print(h[g.index(i)], "eiro")
else: print("Tādu kūku nav iespējams pasūtīt")
print("Jūs pasūtījāt",c, f, i)
print("Jums jāsamaksā",(b[a.index(c)])+(e[d.index(f)])+(h[g.index(i)]), "eiro")