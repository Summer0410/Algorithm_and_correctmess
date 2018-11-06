############################################################################################
#       Run this script to see the test results                                            #
#       ie:run in terminal ->Python testCases.py                                                             #
#                                                                                          #
############################################################################################


from parserBase import ParserBase
#Main function to test the 18 test cases provided
def main():
  testCases = [["x", ">", "y"],
                ["x"],
                ["x", "+", "y"],
                ["x", "+", "y", ">=", "x", "*", "(", "y", "-", "3", ")"],
                ["y", ">", "(", "y", "-", "3", ")"],
                ["x", "<", "y", "AND", "y", "<", "z"],
                ["x", ">", "y", "AND", "[", "y", "=", "z", "OR", "y", "=", "z", "*", "(", "x", "+", "1", ")", "]"],
                ["FORALL", "x", "::", "[", "x", "<", "5", "IMP", "x", "*", "x", "<", "25", "]"],
                ["FORALL", "x", "::", "x", ">", "y"],
                ["FORALL", "x", "::", "[", "x", "AND", "y", "]"],
                ["EXISTS", "y", "::", "[", "FORALL", "x", "::", "x", ">", "y", "]"],
                ["EXISTS", "y", "::", "[", "FORALL", "x", "::", "x", ">", "y"],
                ["x", "+", "y", ">", "yz", "+", "xxx"],
                ["(", "x", "+", "y", ")", "*", "z", ">", "yz", "+", "xxx"],
                ["(", "x", "+", "y", "*", "z", ">", "yz", "+", "xxx"],
                ["x", "+", "(", "y", "*", "z", ")", ">", "yz", "+", "xxx"],
                ["x", "*", "y", "=", "qr"],
                ["x", "y"]]
  expectedValue = [True,False,False,True,True,True,True,True,True,False,True,False,True,True,False,True,True,False]
  Flag = False
  for  i in range(0,18):
    currentTestCase = ParserBase(testCases[i])
    currentExpectedValue = expectedValue[i]
    # print("Sim(%s,%s) is %s" %(masterFile,comparingTextfiles[i],sim))
    print("Case%s :"%(i+1))
    if(currentExpectedValue==currentTestCase.parse(currentTestCase.s)):
      print("PASSED")
    else:
      print("FAILED")
      Flag = True
  if(Flag == True):
    print("There is test case failed")
  else:
    print("All test cases passed")

if __name__ == '__main__':
  main()

