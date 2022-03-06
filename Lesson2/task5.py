# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

def ascii_out(strt, stp):
    if strt == stp:
        return str(strt) + ' - ' + chr(strt) + ' '
    if (strt - 31) % 10 == 0 and strt != 32:
        return str(strt) + ' - ' + chr(strt) + ' ' + '\n' + ascii_out(strt + 1, stp)
    else:
        return str(strt) + ' - ' + chr(strt) + ' ' + ascii_out(strt + 1, stp)


if __name__ == '__main__':
    print(ascii_out(32, 127))

