def decryption(encrptd_mssg):
    dcrpt_prps = encrptd_mssg.split()

    #print(dcrpt_prps)

    string = ""
    dcrptd_mssg = []
    for i in range(len(dcrpt_prps[0]) + 1):
        for j in range(len(dcrpt_prps) + 1):
            try:
                
                if dcrpt_prps[j][i] != "_":
                    string += dcrpt_prps[j][i]
                else:
                    dcrptd_mssg.append(string)
                    string = ""
            except IndexError:
                continue
                
    dcrptd_mssg.append(string)


    dcrptd_str = ""

    for i in dcrptd_mssg:
        dcrptd_str += i + " "

    return dcrptd_str


if __name__ == "__main__":
    mssg = decryption("W_td hiha aset t__a")

    print(mssg)