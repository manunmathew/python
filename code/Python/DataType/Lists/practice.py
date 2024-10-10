    # n = int(input('Enter the start number: '))

    # sp = " "

    # for i in range(1, n + 1):
    #     bin = []
    #     num = i
    #     while num != 0:
    #         bin.append(str(num % 2))
    #         num = num // 2
    #     bin.reverse()
    #     ln = len(bin)

    #     oct = []
    #     num = i
    #     while num != 0:
    #         oct.append(str(num % 8))
    #         num = num // 8
    #     oct.reverse()


    #     hex = []
    #     num = i
    #     while num != 0:
    #         h = num % 16
    #         if h < 10:
    #             hex.append(str(h))
    #         elif h == 10 :
    #             hex.append(("A"))
    #         elif h == 11 :
    #             hex.append(("B"))
    #         elif h == 12 :
    #             hex.append(("C"))
    #         elif h == 13 :
    #             hex.append(("D"))
    #         elif h == 14 :
    #             hex.append(("E"))
    #         elif h == 15 :
    #             hex.append(("F"))
    #         num = num // 16
    #     hex.reverse()
    #     print(i, end= "    ")
    #     print(sp * ln, end= "")
    #     print(''.join(oct), end= "")
    #     print(sp * ln, end= "")
    #     print(''.join(hex), end= "")
    #     print(sp * ln, end= "")
    #     print(''.join(bin), end= "")

    #     print()

# n = 17

# ln = len(bin(n))
# print(ln)
# for i in range(1, n+1):
#     print(i, end= "")
#     print(oct(i), end= "")
#     print(hex(i), end= "")
#     print(bin(i), end= "")
#     print()



# ln = len(bin(n)[2:])  # Length of the binary representation without the '0b' prefix
# print(ln)

# for i in range(1, n+1):
#     decimal = str(i).ljust(ln)
#     octal = oct(i)[2:].ljust(ln)
#     hexa = hex(i)[2:].upper().ljust(ln)
#     binary = bin(i)[2:].ljust(ln)

#     print(f"{decimal} {octal} {hexa} {binary}")


s = "q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M"

y = s.split()
z = s
for i in y:
    c = i.capitalize()
    z = z.replace(c, i)
print(z)
