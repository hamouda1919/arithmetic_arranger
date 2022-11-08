import re 


def arithmetic_arranger(problems, solve=False): 
    
    if (len(problems) > 5):
        return "Error: Too many problems."
    
    first = "" 
    second = "" 
    lines = "" 
    oprf = "" 
    string = ""
  
    for problem in problems:
           
        if (re.search("[^\s0-9.+-]", problem)):
        
            if(re.search("[/*]", problem)):     
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits." 
            
        firstNum = problem.split(' ')[0]
        operator = problem.split(' ')[1]
        secondNum = problem.split(' ')[2]
        
       
        if (len(firstNum) >= 5 or len(secondNum) >= 5):
            return "Error: Numbers cannot be more than four digits."
      
        opr = None 
        if (operator == '+'):            
            opr = str(int(firstNum) + int(secondNum))
        elif (operator == '-'):
            opr = str(int(firstNum) - int(secondNum))
        
        length = max(len(firstNum), len(secondNum)) + 2
        top = str(firstNum).rjust(length)
        bottom = operator + str(secondNum).rjust(length - 1)
        line = ""
        result = str(opr).rjust(length)
        for s in range(length):
            line += "-"
        
        
        if problem != problems[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            oprf += result + '    '
        else:
            first += top
            second += bottom
            lines += line
            oprf += result
        
    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + oprf
    else:
        string = first + '\n' + second + '\n' + lines
    return string