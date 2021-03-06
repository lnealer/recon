import sys

class Recon:
    def __init__(self, recon_in):
        Recon.out = {} # build recon.out with d0-pos data
        Recon.input = recon_in
        Recon.index = 0
        i = 1
        d0_pos = Recon.input
        while not d0_pos[i].startswith("D1"):
            cur = d0_pos[i].split()
            if len(cur)==0 or d0_pos[i].startswith("D0"):
                i += 1
                continue
            stock = cur[0]
            shares = float(cur[1])
            Recon.out[stock] = shares
            i += 1
        Recon.index = i+1


    def update(self):
        # update with d1 transaction data
        i = Recon.index
        d1_trn = Recon.input
        while not d1_trn[i] == "D1-POS\n":
            cur = d1_trn[i].split()
            if len(cur) == 0:
                # check for blank line
                i += 1
                continue
            stock = cur[0]
            trn = cur[1]
            shares = float(cur[2])
            val = float(cur[3])

            #check the transaction
            if stock not in Recon.out:
                Recon.out[stock] = 0
            if (trn == "SELL"):
                Recon.out["Cash"] += val
                Recon.out[stock] -= shares
            elif (trn == "BUY"):
                Recon.out["Cash"] -= val
                Recon.out[stock] += shares
            elif (trn == "DEPOSIT"):
                Recon.out["Cash"] += val
            elif (trn == "FEE"):
                Recon.out["Cash"] -= val
            elif (trn == "DIVIDEND"):
                Recon.out["Cash"] += val
            i += 1
        Recon.index = i+1
    
    def compare(self, path, paths):
        # compare recon.out with d1-pos and create out file
        if len(paths) > 1:
            path += "/"
        path += "recon.out"
        out = open(path, "w+")
        d1_trn = Recon.input
        i = Recon.index
        length = len(Recon.input)

        # comparing shares in D1-POS
        while i < length:
            cur = d1_trn[i].split()
            stock = cur[0]
            shares = float(cur[1])
            if stock not in Recon.out:
                diff = shares
            else: 
                diff = shares - Recon.out[stock]
                del Recon.out[stock]
            if diff:
                out.write(stock + " " + str(diff) + "\n")
            i += 1
        
        # including shares not in D1-POS
        for stock in Recon.out:  
            diff = -1*Recon.out[stock]
            if diff:
                out.write(stock + " " + str(diff) + "\n")
        out.close() 
         



if __name__ == '__main__':
    if len(sys.argv) == 1:
        recon_in = input("Please input a file path to recon.in: ")
    else:
        recon_in = sys.argv[1]
    
    # retrieve the path to recon.in
    paths = recon_in.split("/")
    path = ""
    i=0
    while i < (len(paths) - 1):
        path += paths[i] + "/"
        i += 1
    print(path) 

    # open the file
    f = open(recon_in, 'r')
    lines = f.readlines()

    recon_out = Recon(lines)
    recon_out.update()
    recon_out.compare(path, paths)
    
