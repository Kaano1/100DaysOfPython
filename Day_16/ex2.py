from prettytable import PrettyTable

head = PrettyTable()
head.add_column("City Name", ["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
head.add_column("Area", [1298, 2819, 21, 280, 3333, 122, 1236])
head.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,1554769])
head.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])
head.align = "l"
print(head)
