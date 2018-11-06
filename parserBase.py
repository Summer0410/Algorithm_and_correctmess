class ParserBase:
    def __init__(self, code):
        self.s = code   # list of tokens (strings) to be parsed
        self.f = True   # flag set to false if an error occurs

    def consume(self):
        self.s = self.s[1:]

    def expect(self, a):
        if (len(self.s) > 0 and a == self.s[0]):
            self.consume()
        else:
            self.f = False
    
    def parse(self,s):
        return self.command(self.s)

    #The starting non-terminal****************************************************************************
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
        if(current == 'EXISTS'):
            self.expect(current)#remove current
            current = self.s[0]
            if (self.isIdSequence(current) == True):
                self.expect(current)#remove current
                current = self.s[0]
                if (current == '::'):
                    self.expect(current)#remove current
                    current = self.s[0]
                    if(current =='['and self.s[len(self.s)-1]==']'):#check pairong nracket
                        self.expect(current)#remove current
                        s.pop()#remove another half bracket
                        return (self.command(self.s))
            else:
                return False   
        if(self.basicExpression == True):
            self.expect(self.s[0])#remove current
            current = self.s[0]
            if(self.isPredop(current) == True):
                return (self.expression(self.s))
            else:
                return False
        else:
            return (self.expression(self.s))
#Non-terminal expression**********************************************************************88
    def expression(self,s):
        current = self.s[0]
        if(len(self.s)>1 and self.isRelop(self.s[1])==True):
            if(self.basicCompare(self.s) ==True):
                if(len(self.s)>1):
                    current = self.s[0]
                    if(self.isPredop(current)==True):
                        self.expect(self.s[0])
                        current = self.s[0]
                        if(current == '['):
                            return(self.expression(self.s))
                        else:
                            return (self.basicCompare(self.s)== True)
                    else:
                        return False
                else:
                    return True
        if(current == '[' and s[len(self.s)-1]==']' ):
            self.expect(current)#remove current
            self.s.pop()#remove another half bracket
            return (self.expression(self.s))
        if(self.basicOperation(self.s)==True and len(self.s)>1):
            self.expect(self.s[0])
            current = self.s[0]
            if(self.isRelop(current) == True):
                self.expect(current)
                if(len(self.s)>1):
                    return (self.basicOperation(self.s) == True)
                else:
                    current= self.s[0]
                    return (self.isIdSequence (current) == True)
            else:
                return False
        else:
            return False
#A help function of expression******************************************************************************8
    def basicExpression(self, a):
        current = self.s[0]
        if(self.basicCompare(self.s) ==True):
            self.expect(self.s[0])
            current = self.s[0]
            if(self.isPredop(current)==True):
                self.expect(self.s[0])
                current = self.s[0]
                return (self.basicCompare(self.s)== True)
            else:
                return False

        if(self.basicCompare(self.s) == True):
            return True
        if(current == '[' and self.s[len(self.s)-1]==']' ):
            self.expect(current)#remove current
            self.s.pop()#remove another half bracket
            return (self.expression(self.s))
        else:
           return False
# A function to check if the provied string is an opersion--non-Terminal******************************************************8
    def basicOperation(self, a):
        current = self.s[0]
        if(self.isIdSequence(current) == True and len(self.s)>1):
            self.expect(current)#remove current
            current = self.s[0]
            if(self.isOp(current) == True):
                self.expect(current)#remove current
                current = self.s[0]
                if(self.isIdSequence(current)==True or self.isNumSequence(current)==True ):
                    return True
                else:
                    if(current == '(' and len(self.s)>1):
                        self.expect(self.s[0])
                        if(self.basicOperation(self.s) == True and len(self.s) >1):
                            self.expect(self.s[0])
                            return (self.s[0] == ')')
                        else:
                            return False
            else:
                return False
        if(current == '(' and len(self.s)>1):
                        self.expect(self.s[0])
                        if(self.basicOperation(self.s) == True and len(self.s) >1):
                            self.expect(self.s[0])
                            if(self.s[0] == ')'):
                                self.expect(self.s[0])
                                if(len(self.s) == 0):
                                    return True
                                else:
                                    if(self.isOp(self.s[0])):
                                        self.expect(self.s[0])
                                        return (self.isNumSequence(self.s[0]) or self.isIdSequence(self.s[0]))
                                    else:
                                        return False
                            else:
                                return False
        else:
            return False
#A function to check if a given String is a valid comparison -- non-terninal***************************************************
    def basicCompare(self, s):
        current = self.s[0]
        if(len(self.s)>1 and self.isOp(self.s[1])== True):
            if(self.basicOperation(self.s) == True and len(self.s)>1):
                self.expect(self.s[0])
                current = self.s[0]
                if(self.isRelop(current) == True):
                    self.expect(current)#remove current
                    current = self.s[0]
                    return (self.isNumSequence(current) ==True)
                else:
                    return False
        else:
            if(self.isIdSequence(current) == True and len(self.s)>1):
                self.expect(current)
                current = self.s[0]
                if(self.isRelop(current) == True):
                    self.expect(current)#remove current
                    current = self.s[0]
                    if(self.isIdSequence(current) == True or self.isNumSequence(current) == True):
                        self.expect(current)#remove current
                        return True
                    else:
                        return(self.basicOperation(self.s))
                else:
                    return False
            else:
                return False
  # A function to check if a given string is a sequence of id*************************
    def isIdSequence(self,currentString):
        isSequence = True
        for l in currentString:
            if(l.isalpha() == False):
                isSequence = False
        return isSequence
  # A function to check if a given string is a sequence of num*************************
    def isNumSequence(self,currentString):
        isSequence = True
        for l in currentString:
            if(l.isdigit() == False):
                isSequence = False
        return isSequence
# A function to check if a given string is an operator*********************************
    def isOp(self,currentString):
        return (currentString == '-'or currentString == '+'or currentString =='*'or currentString=='/')
# A function to check if a given string is a relop********8*****************************
    def isRelop(self,currentString):
        return (currentString =='>'or currentString=='<'or currentString=='='or currentString=='>='or currentString=='<=')
# A function to check if a given string is a predop****************************************8
    def isPredop(self,currentString):
        return (currentString == 'AND'or currentString =='OR'or currentString=='IMP')
            
