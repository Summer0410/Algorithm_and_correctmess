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
            print("I came here")
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
        if(self.isIdSequence(current) == True):
            self.expect(current)#remove current
            current = self.s[0]
            if(self.isRelop(current) == True):
                self.expect(current)#remove current
                current = self.s[0]
                if(self.isIdSequence(current) == True):
                    return True
                else:
                    return False
            else:
                return False
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
    def compare(self,s):
        current = self.s[0]
        if(self.isIdSequence(current) == True):
            self.expect(current)#remove current
            current = self.s[0]
            if(self.isRelop(current) == True):
                self.expect(current)#remove current
                current = self.s[0]
                if(self.isIdSequence(current) == True or self.isNumSequence(current) == True):
                    self.expect(current)#remove current
                    return (len(self.s) == 0)
                else:
                    return(self.operation(self.s))
            else:
                return False
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
test1 = ParserBase(['(','zz','+','y',')'])
print(test1.operation(test1.s))
