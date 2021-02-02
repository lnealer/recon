import sys

class Recon:
    def __init__(self, recon_in):
        Recon.out = {}
        Recon.input = recon_in
        Recon.index = 0
        i = 1
        d0_pos = Recon.input
        while not d0_pos[i].startswith("D1"):
            cur = d0_pos[i].split()
            if not cur or d0_pos[i].startswith("D0"):
                i += 1
                continue
            stock = cur[0]
            shares = float(cur[1])
            Recon.out[stock] = shares
            i += 1
        Recon.index = i+1


    def update(self):
        i = Recon.index
        d1_trn = Recon.input
        while not d1_trn[i].endswith("POS"):
            cur = d1_trn[i].split()
            if not cur :
                i += 1
                break
            stock = cur[0]
            trn = cur[1]
            shares = float(cur[2])
            val = float(cur[3])
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
    
    def compare(self):
        out = open("recon.out", "w+")
        d1_trn = Recon.input
        i = Recon.index
        length = len(Recon.input)
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
        for stock in Recon.out:  
            diff = -1*Recon.out[stock]
            if diff:
                out.write(stock + " " + str(diff) + "\n")
        out.close() 
         



if __name__ == '__main__':
    recon_in = sys.argv[1]
    f = open(recon_in, 'r')
    lines = f.readlines()
    recon_out = Recon(lines)
    recon_out.update()
    recon_out.compare()
    