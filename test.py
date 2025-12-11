import os
def open_file(file_path, demande=None):
    f = open(file_path, 'r')
    var_result = []
    var_avantresult = []
    for line in f:
        if ':' in line:
            avantresult = line.split(':', 1)[0].strip()
            result = line.split(':', 1)[1].strip()
            var_avantresult.append(avantresult)
            var_result.append(result)
            
    if demande is None:
        for res in var_result:
            print(res)
    else:
        i = 0
        for i, res_avant in enumerate(var_avantresult):
            if res_avant == demande:
                print(var_result[i])
            i+=1
    f.close()


chem1 = "ADE_RT1_Septembre2025_Decembre2025.ics"
chem2= "evenementSAE_15_2025.ics"

open_file(chem1,"CREATED")