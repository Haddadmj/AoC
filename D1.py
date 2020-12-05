def AoC_Part1():
    with open("D1_in.txt",'r') as inFile:
        fileContent = inFile.readlines()
        for x in fileContent:
            for y in fileContent[1:]:
                xInt = int(x)
                yInt = int(y)
                if ( xInt + yInt == 2020):
                    return (xInt * yInt)

def AoC_Part2():
    with open("D1_in.txt",'r') as inFile:
        fileContent = inFile.readlines()
        for x in fileContent:
            for y in fileContent[1:]:
                for z in fileContent[2:]:
                    xInt = int(x)
                    yInt = int(y)
                    zInt = int(z)
                    if ( xInt + yInt + zInt == 2020):
                        return (xInt * yInt * zInt)

print(AoC_Part1())
print(AoC_Part2())