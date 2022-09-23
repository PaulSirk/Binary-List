class binaryList:
    def __init__(self, dataType):
        self.binaryList = []
        self.dataType = dataType

    def __check_class(self, value) -> None:
        if type(value) != self.dataType:
            raise ValueError("Incorrect Data Type")

    # returns -1 if element is not found
    def search(self, search_num) -> int:
        self.__check_class(search_num)
        binaryLength : int = len(self.binaryList)

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

    def insert_element(self, element) -> None:
        valid = self.__check_class(element)
        binaryLength : int = len(self.binaryList)

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
                    for i in range(center, binaryLength):
                        if self.binaryList[i] <= element:
                            self.binaryList.insert(i+1, element)
                            return
                else:
                    for j in range(0, center):
                        if self.binaryList[j] >= element:
                            self.binaryList.insert(j, element)
                            return

            return

    def delete_element(self, delete_num) -> None:
        present_num : int = self.search(delete_num)
        if present_num == -1:
            print("Element is not present.")
        else:
            del self.binaryList[present_num]
                
        return

