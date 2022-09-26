class binaryList:
    def __init__(self, dataType):
        self.binaryList = []
        self.length = 0
        self.dataType = dataType

    def __check_class(self, value) -> None:
        if type(value) != self.dataType:
            raise ValueError("Incorrect Data Type")

    '''def __check_int(self, num) -> None:
        if type(num) != int or num != None:
            raise ValueError("Input a number.")'''

    # returns -1 if element is not found
    def search(self, search_num) -> int:
        self.__check_class(search_num)
        binaryLength : int = self.length

        not_found : int = -1

        if binaryLength == 0:
            return not_found

        if binaryLength == 1:
            if self.binaryList[0] == search_num:
                return 0
            else:
                return not_found

        center : int  = binaryLength // 2

        if self.binaryList[center] <= search_num:
            for i in range(center, binaryLength):
                if self.binaryList[i] == search_num:
                    return i
        else:
            for j in range(0, center):
                if self.binaryList[j] == search_num:
                    return j

        return not_found

    def insert(self, element) -> None:
        valid = self.__check_class(element)
        binaryLength : int = self.length

        if binaryLength == 0:
            self.binaryList.insert(0, element)
        elif binaryLength == 1:
            if self.binaryList[0] >  element:
                self.binaryList.insert(0, element)
            else:
                self.binaryList.append(element)

        else:
            if self.binaryList[0] >= element:
                self.binaryList.insert(0, element)
            elif self.binaryList[binaryLength-1] <= element:
                self.binaryList.append(element)
            else:
                center = binaryLength // 2
                if self.binaryList[center] <= element:
                    for i in range(0, center, -1):
                        if self.binaryList[i] <= element:
                            self.binaryList.insert(i+1, element)
                            break
                else:
                    for j in range(center, binaryLength):
                        if self.binaryList[j] >= element:
                            self.binaryList.insert(j, element)
                            break
        self.length += 1
        return

    def delete(self, delete_num) -> None:
        present_num : int = self.search(delete_num)
        if present_num == -1:
            print("Element is not present.")
        else:
            del self.binaryList[present_num]
            self.length -= 1
        return

    def look(self, start, end = None, steps = None) -> None:
        if start == None:
            raise ValueError("start can not be 'None'")

        if end == None or start == end:
            print(self.binaryList[start])
        elif end != None and steps == None:
            print(self.binaryList[start:end])
        else:
            print(self.binaryList[start:end:steps])
        return

x = binaryList(int)

x.insert(0)
x.insert(3)
x.insert(2)
x.insert(1)
