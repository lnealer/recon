import sys

class Recon:
    def __init__(self, recon_in):
        Recon.out = {}
        Recon.input = recon_in
        Recon.index = 0
        i = 1
        d0_pos = Recon.input
        while not d0_pos[i].startswith("D1"):
            if d0_pos[i].startswith("D0") or not recon_in[i].split():
                i = i + 1
                continue
            cur = d0_pos[i].split()
            stock = cur[0]
            shares = cur[1]
            Recon.out[stock] = shares
            i = i+1
        Recon.index = i+1

    def update(self, recon_in):
        i = Recon.index
        while (d1_trn[i] != "D1_POS"):
            cur = d1_trn[i].split()
            stock = cur[0]
            trn = cur[1]
            shares = cur[2]
            val = cur[3]
    
    #def compare(self, recon_in) 



if __name__ == '__main__':
    recon_in = sys.argv[1]
    f = open(recon_in, 'r')
    lines = f.readlines()
    recon_out = Recon(lines)
    
