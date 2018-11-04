class ParserBase:
    """ base class for parsers
    """
    
    def __init__(self, code):
        self.s = code   # list of tokens (strings) to be parsed
        self.f = True   # flag set to false if an error occurs

    def consume(self):
        """ remove first item from s
        """
        self.s = self.s[1:]

    def expect(self, a):
        """ Try to remove a from start of s
        """
        if (len(self.s) > 0 and a == self.s[0]):
            self.consume()
        else:
            self.f = False
    
    def parse(self,s):
        """You must overide this method to do the parsing
        Since this one is not overidden, the parsing fails.
        """
        current = s[0]
        self.f = False
    def command(self,s):
        current = self.s[0]
        if(current == 'FORALL'): 
            self.expect(current)#remove current
            current = self.s[0]
            if (self.isIdSequence(current) == True):
                self.expect(current)#remove current
                current = self.s[0]
                if(current =='::'):
                    self.expect(current)#remove current
                    return(self.expression(self.s))
                else:
                    return False
            else:
                return False
       
        if(current == 'EXIST'):
            self.expect(current)#remove current
            current = self.s[0]
            if (self.isIdSequence(current) == True):
                self.expect(current)#remove current
                current = self.s[0]
                if (current == '::'):
                    self.expect(current)#remove current
                    current = self.s[0]
                    print(self.s)
                    if(current =='['and self.s[len(self.s)-1]==']'):#check pairong nracket
                        self.expect(current)#remove current
                        s.pop()#remove another half bracket
                        return (self.command(self.s))
            else:
                return False   
        else:
            return False
            
    def expression(self,s):
        current = self.s[0]
        if(self.basicCompare(self.s) ==True):
            self.expect(self.s[0])
            current = self.s[0]
            if(self.isPredop(current)==True):
                self.expect(self.s[0])
                current = self.s[0]
                if(self.compare(self.s)== True):
                    return True
                else:
                    return False
            else:
                return False

        if(self.compare(self.s) == True):
            return True
        if(current == '[' and s[len(self.s)-1]==']' ):
            self.expect(current)#remove current
            self.s.pop()#remove another half bracket
            return (self.expression(self.s))
        else:
           return False
    def operation(self,a):
        current = self.s[0]
        if(self.isIdSequence(current) == True):
            self.expect(current)#remove current
            current = self.s[0]
            if(self.isOp(current) == True):
                self.expect(current)#remove current
                current = self.s[0]
                if(len(self.s)==1):
                    return (self.isIdSequence(current) or self.isNumSequence)
                else:
                    return self.operation(self.s)
            else:
                return False
        if(current =='(' and self.s[len(self.s)-1]==')'):
            self.expect(current)#remove current
            self.s.pop()#remove another half bracket
            return self.operation(self.s)
        else:
            return False
    def basicOperation(self, a):
        current = self.s[0]
        if(self.isIdSequence(current) == True):
            self.expect(current)#remove current
            current = self.s[0]
            if(self.isOp(current) == True):
                self.expect(current)#remove current
                current = self.s[0]
                return (self.isIdSequence(current) or self.isNumSequence)
            else:
                return False
        else:
            return False

    def compare(self,s):
        current = self.s[0]
        if(self.isOp(self.s[1])== True):
            if(self.basicOperation(self.s) == True):
                self.expect(self.s[0])
                current = self.s[0]
                if(self.isRelop(current) == True):
                    self.expect(current)#remove current
                    current = self.s[0]
                    if(self.isNumSequence(current) ==True and len(self.s)==1):
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            if(self.isIdSequence(current) == True):
                self.expect(current)
                current = self.s[0]
                if(self.isRelop(current) == True):
                    self.expect(current)#remove current
                    current = self.s[0]
                    if(self.isIdSequence(current) == True or self.isNumSequence(current) == True):
                        print("I came to the last...")
                        self.expect(current)#remove current
                        return (len(self.s) == 0)
                    else:
                        return(self.operation(self.s))
                else:
                    return False
    def basicCompare(self, s):
        current = self.s[0]
        if(self.isOp(self.s[1])== True):
            if(self.basicOperation(self.s) == True):
                self.expect(self.s[0])
                current = self.s[0]
                if(self.isRelop(current) == True):
                    self.expect(current)#remove current
                    current = self.s[0]
                    if(self.isNumSequence(current) ==True):
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            if(self.isIdSequence(current) == True):
                self.expect(current)
                current = self.s[0]
                if(self.isRelop(current) == True):
                    self.expect(current)#remove current
                    current = self.s[0]
                    if(self.isIdSequence(current) == True or self.isNumSequence(current) == True):
                        print("I came to the last...")
                        self.expect(current)#remove current
                        return (len(self.s) == 0)
                    else:
                        return(self.operation(self.s))
                else:
                    return False
  
    def isIdSequence(self,currentString):
        isSequence = True
        for l in currentString:
            if(l.isalpha() == False):
                isSequence = False
        return isSequence
    def isNumSequence(self,currentString):
        isSequence = True
        for l in currentString:
            if(l.isdigit() == False):
                isSequence = False
        return isSequence
   
    def isOp(self,currentString):
        if(currentString == '-'or currentString == '+'or currentString =='*'or currentString=='/'):
            return True 
        else:
            return False
    def isRelop(self,currentString):
        if(currentString =='>'or currentString=='<'or currentString=='='or currentString=='>='or currentString=='<='):
           # print(currentString)
            return True
        else:
            return False
    def isPredop(self,currentString):
        if(currentString == 'AND'or currentString =='OR'or currentString=='IMP'):
            return True
        else:
            return False

#test1 = ParserBase(["FORALL", "x","::","x",">","y"])
test1 = ParserBase(['y','+','x','>','3','AND','y','=','x'])
print(test1.expression(test1.s))