def tax_s():
    income = float(input("Enter Your income: "))
    MPF = income * 0.05
    allowance = 132000
    if MPF > 18000:
        MPF  = 18000
    net_income = income - MPF - allowance
    net_income_stand = income - MPF
    print("Net chargeable income: ", net_income)
    stand_tax = net_income_stand*0.15
    tax = 0
    if net_income <= 0:
        tax = 0
    elif net_income <= 50000:
        tax = (net_income*0.02)
    elif net_income > 50000 and net_income <= 100000:
        tax =(net_income-50000)*(0.06) + 1000 
    elif net_income > 100000 and net_income <= 150000:
        tax = (net_income-100000)*(0.1)+ 1000 + 3000
    elif net_income > 150000 and net_income <= 200000:
        tax = (net_income-150000)*(0.14)+ 1000 + 3000 + 5000 
    elif net_income > 200000:
        tax = (net_income-200000)*(0.17) + 1000 + 3000 + 5000 + 7000
    if tax < stand_tax or tax == stand_tax:
        print("Deductions: ", MPF)
        print("Tax payable: ",tax)
    elif stand_tax < tax:
        print("Your Salaries is match to use the standard rate!")
        print("Deductions: ", MPF)
        print("The Standard Taxation: ", stand_tax)

def tax_j():
    income_H = float(input("Enter Your husband Income: "))
    income_W = float(input("Enter Your wife Income: "))
    allowance_j = 264000
    allowance = 132000
    income = income_H + income_W
### calculat MPF 
    MPF_H = income_H * 0.05
    MPF_W = income_W * 0.05
### Make sure MPF will not over 60000 per person
    if MPF_H > 18000 and MPF_W > 18000:
        MPF_H  = 18000
        MPF_W  = 18000
    elif MPF_H > 18000:
        MPF_H  = 18000
    elif MPF_W > 18000:
        MPF_W  = 18000
    else:
        MPF_H = income_H * 0.05
        MPF_W = income_W * 0.05

    MPF = MPF_H + MPF_W
    if MPF > 36000:
        MPF  = 36000
        
    net_income = income - MPF - allowance_j
    net_income_H = income_H - MPF_H - allowance
    net_income_W = income_W - MPF_W - allowance

    net_income_stand = income - MPF
    net_income_H_stand = income_H - MPF_H
    net_income_W_stand = income_W - MPF_W

    stand_tax = net_income_stand*0.15
    stand_tax_H = net_income_H_stand*0.15
    stand_tax_W = net_income_W_stand*0.15
##############################################################
    tax = 0
    if net_income <= 0:
        tax = 0
    elif net_income <= 50000:
        tax = (net_income*0.02)
    elif net_income > 50000 and net_income <= 100000:
        tax =(net_income-50000)*(0.06) + 1000 
    elif net_income > 100000 and net_income <= 150000:
        tax = (net_income-100000)*(0.1)+ 1000 + 3000
    elif net_income > 150000 and net_income <= 200000:
        tax = (net_income-150000)*(0.14)+ 1000 + 3000 + 5000 
    elif net_income > 200000:
        tax = (net_income-200000)*(0.17) + 1000 + 3000 + 5000 + 7000
##############################################################
    tax_H = 0
    if net_income_H <= 0:
        tax_H = 0
    elif net_income_H <= 50000:
        tax_H = (net_income_H*0.02)
    elif net_income_H > 50000 and net_income_H <= 100000:
        tax_H =(net_income_H-50000)*(0.06) + 1000 
    elif net_income_H > 100000 and net_income_H <= 150000:
        tax_H = (net_income_H-100000)*(0.1)+ 1000 + 3000
    elif net_income_H > 150000 and net_income_H <= 200000:
        tax_H = (net_income_H-150000)*(0.14)+ 1000 + 3000 + 5000 
    elif net_income_H > 200000:
        tax_H = (net_income_H-200000)*(0.17) + 1000 + 3000 + 5000 + 7000
##############################################################
    tax_W = 0
    if net_income_W <= 0:
        tax_W = 0
    elif net_income_W <= 50000:
        tax_W = (net_income_W*0.02)
    elif net_income_W > 50000 and net_income_W <= 100000:
        tax_W =(net_income_W-50000)*(0.06) + 1000 
    elif net_income_W > 100000 and net_income_W <= 150000:
        tax_W = (net_income_W-100000)*(0.1)+ 1000 + 3000
    elif net_income_W > 150000 and net_income_W <= 200000:
        tax_W = (net_income_W-150000)*(0.14)+ 1000 + 3000 + 5000 
    elif net_income > 200000:
        tax_W = (net_income_W-200000)*(0.17) + 1000 + 3000 + 5000 + 7000
##############################################################
    if tax_H < stand_tax_H and tax_W < stand_tax_W or tax_W == stand_tax_W or tax_H == stand_tax_H:
        print("Husband Net chargeable income: ", net_income_H)
        print("Deductions: ", MPF_H)
        print("Tax payable: ",tax_H)
        print("Wife Net chargeable income: ", net_income_W)
        print("Deductions: ", MPF_W)
        print("Tax payable: ",tax_W)
        tax_s = tax_H + tax_W
    elif stand_tax_H < tax_H and tax_W < stand_tax_W or tax_W == stand_tax_W:
        print("Husband Net chargeable income: ", net_income_H)
        print("Deductions: ", MPF_H)
        print("The Standard Taxation: ", stand_tax_H)
        print("Wife Net chargeable income: ", net_income_W)
        print("Deductions: ", MPF_W)
        print("Tax payable: ",tax_W)
        tax_s = stand_tax_H + tax_W
    elif tax_H < stand_tax_H and stand_tax_W < tax_W or tax_H == stand_tax_H:
        print("Husband Net chargeable income: ", net_income_H)
        print("Deductions: ", MPF_H)
        print("Tax payable: ",tax_H)
        print("Wife Net chargeable income: ", net_income_W)
        print("Deductions: ", MPF_W)
        print("The Standard Taxation: ", stand_tax_W)
        tax_s = tax_H + stand_tax_W
    elif stand_tax_H < tax_H and stand_tax_W < tax_W:
        print("Husband Net chargeable income: ", net_income_H)
        print("Deductions: ", MPF_H)
        print("The Standard Taxation: ", stand_tax_H)
        print("Wife Net chargeable income: ", net_income_W)
        print("Deductions: ", MPF_W)
        print("The Standard Taxation: ", stand_tax_W)     
        tax_s = stand_tax_H + stand_tax_W
##############################################################
    print("Under Separate Taxation: ",tax_s)
    if tax < stand_tax:
        print("Under Join Taxation: ",tax)
    elif stand_tax < tax:
        print("Under Join Taxation(standard): ", stand_tax)
    if tax > tax_s:
        print("Deductions: ", MPF)
        print("Under Separate Taxation is better: ",tax_s)
    elif tax < tax_s:
        if tax < stand_tax:
            print("Deductions: ", MPF)
            print("Under Join Taxation is better: ",tax)
        elif stand_tax < tax:
            print("Deductions: ", MPF)
            print("Under Join Taxation is better(standard): ", stand_tax)
    
def main():
    instructions = """\Enter one of the following:
       1 Under separate Taxation
       2 Under Join Taxation
       Q TO END \n"""
    
    while True:
        print(instructions)
        choice = input("Enter 1 or 2 or Q: ")
        
        if choice == "1" :
            tax_s()
        elif choice == "2" :
            tax_j()
        elif choice == "Q" :
            break
        
    print ("End joint tax calculate App")
    
if __name__ == '__main__':
    main()