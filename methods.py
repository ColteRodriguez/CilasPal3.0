# Library of Parsing algorithms. Both take .pdf files as string arrays and return necessary data arrays
# Yes, these algs are disgusting, but pdfs are stubborn little files, and I am yet to find a more efficient solution

def thirteensingle(List, List2):
    littleQArray = []
    bigQArray = []
    Index = List2.index("volume / undersize")
    startIndex = Index + 29
    endIndex = startIndex + 7

    # Extracting the User defined size classes
    for i in range(4):
        bigQArray.append(List2[startIndex:endIndex])
        startIndex = startIndex + 13
        endIndex = endIndex + 13

    startIndex = startIndex - 1
    endIndex = endIndex - 1
    for i in range(6):
        bigQArray.append(List2[startIndex:endIndex])
        startIndex = startIndex + 12
        endIndex = endIndex + 12

    startIndex = startIndex + 6
    endIndex = endIndex + 6
    for i in range(3):
        bigQArray.append(List2[startIndex:endIndex])
        startIndex = startIndex + 13
        endIndex = endIndex + 13

    # Extracting the Full Size Class
    sIndex = List2.index('undersize') + 44
    eIndex = sIndex + 6
    for i in range(6):
        for j in range(10):
            ins = List[sIndex:eIndex]
            littleQArray.append(ins)
            sIndex = sIndex + 20
            eIndex = eIndex + 20

        sIndex = sIndex + 8
        eIndex = eIndex + 8

    for i in range(2):
        for j in range(10):
            ins = List[sIndex:eIndex]
            littleQArray.append(ins)
            sIndex = sIndex + 19
            eIndex = eIndex + 19
        sIndex = sIndex + 8
        eIndex = eIndex + 8

    for j in range(3):
        ins = List[sIndex:eIndex]
        littleQArray.append(ins)
        sIndex = sIndex + 19
        eIndex = eIndex + 19

    for j in range(6):
        ins = List[sIndex:eIndex]
        littleQArray.append(ins)
        sIndex = sIndex + 20
        eIndex = eIndex + 20
    sIndex = sIndex + 28
    eIndex = eIndex + 28
    for j in range(11):
        ins = List[sIndex:eIndex]
        littleQArray.append(ins)
        sIndex = sIndex + 20
        eIndex = eIndex + 20

    # retrieving mean and median
    Apples = List.index('Mean diameter : ')
    ApplesFinal = Apples + 16
    mean = List[ApplesFinal: ApplesFinal + 6]
    median = List[Apples - 37:Apples - 30]

    # retrieving sample name
    nameIndexStart = List.index('Sample ref.')
    nameIndexFinish = List.index('Sample Name')
    sampleName = List[nameIndexStart + 13: nameIndexFinish]

    littleQArray.insert(0, sampleName)
    bigQArray.insert(0, sampleName)
    littleQArray.insert(1, mean)
    littleQArray.insert(2, median)

    # printing info to console for error detection
    return littleQArray, bigQArray


def fifteensingle(List, List2):
    littleQArray = []
    bigQArray = []
    Index = List2.index("volume / undersize")
    startIndex = Index + 29
    endIndex = startIndex + 7

    # Extracting the User defined size classes
    for i in range(4):
        bigQArray.append(List2[startIndex:endIndex])
        startIndex = startIndex + 13
        endIndex = endIndex + 13

    startIndex = startIndex - 1
    endIndex = endIndex - 1
    for i in range(6):
        bigQArray.append(List2[startIndex:endIndex])
        startIndex = startIndex + 12
        endIndex = endIndex + 12

    startIndex = startIndex + 5
    endIndex = endIndex + 5
    for i in range(3):
        bigQArray.append(List2[startIndex:endIndex])
        startIndex = startIndex + 13
        endIndex = endIndex + 13

    # Extracting the Full Size Class
    sIndex = List2.index('undersize') + 44
    eIndex = sIndex + 6

    for j in range(10):
        ins = List[sIndex:eIndex]
        littleQArray.append(ins)
        sIndex = sIndex + 20
        eIndex = eIndex + 20

    sIndex = sIndex + 5
    eIndex = eIndex + 5

    for i in range(4):
        for j in range(10):
            ins = List[sIndex:eIndex]
            littleQArray.append(ins)
            sIndex = sIndex + 19
            eIndex = eIndex + 19
        sIndex = sIndex + 5
        eIndex = eIndex + 5
    sIndex = sIndex + 4
    eIndex = eIndex + 4

    for j in range(10):
        ins = List[sIndex:eIndex]
        littleQArray.append(ins)
        sIndex = sIndex + 20
        eIndex = eIndex + 20
    sIndex = sIndex + 8
    eIndex = eIndex + 8

    for i in range(2):
        for j in range(10):
            ins = List[sIndex:eIndex]
            littleQArray.append(ins)
            sIndex = sIndex + 19
            eIndex = eIndex + 19

        sIndex = sIndex + 8
        eIndex = eIndex + 8

    sIndex = sIndex - 1
    eIndex = eIndex - 1

    for j in range(3):
        ins = List[sIndex:eIndex]
        littleQArray.append(ins)
        sIndex = sIndex + 19
        eIndex = eIndex + 19

    for j in range(6):
        ins = List[sIndex:eIndex]
        littleQArray.append(ins)
        sIndex = sIndex + 20
        eIndex = eIndex + 20
    sIndex = sIndex + 28
    eIndex = eIndex + 28
    for j in range(11):
        ins = List[sIndex:eIndex]
        littleQArray.append(ins)
        sIndex = sIndex + 20
        eIndex = eIndex + 20

    # retrieving mean and median
    Apples = List.index('Mean diameter : ')
    ApplesFinal = Apples + 15
    mean = List[ApplesFinal: ApplesFinal + 6]
    median = List[Apples - 36:Apples - 30]

    # retrieving sample name
    nameIndexStart = List.index('Sample ref.')
    nameIndexFinish = List.index('Sample Name')
    sampleName = List[nameIndexStart + 13: nameIndexFinish]

    littleQArray.insert(0, sampleName)
    bigQArray.insert(0, sampleName)
    littleQArray.insert(1, mean)
    littleQArray.insert(2, median)

    # printing info to console for error detection
    return littleQArray, bigQArray
