def Morse(input):
    Sandi = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    Huruf = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    i = 0

    while True:
        try:
            if input == Sandi[i]:
                output = Huruf[i]
                return(output)
                break
            else:
                i += 1
        except:
            output = "Not Found"
            return(output)
            break
