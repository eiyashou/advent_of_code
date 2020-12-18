
def one(R):
    return sum(len(F)==8or(len(F)==7and'cid'not in F)for f in R.split("\n\n")if(F:=f.replace("\n"," ").split(" ")))