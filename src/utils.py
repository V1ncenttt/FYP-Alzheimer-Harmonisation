class DKDict:
    def __init__(self) -> None:
        self.regions ={}
        self.adni = {}
        self.loadRegions()
        
    
    def loadRegions(self):
        with open("adni_regions.csv") as fp:
            lines = fp.readlines()
            for line in lines[1:]:
                row=line.split(',')
                adni_name = row[0]
                
                side = row[1].split("-")[0]
                region = row[1].split("-")[1]
                
                actual_region = region.lower().strip() + "_" + side.lower()
                
                self.regions[adni_name] = actual_region
                self.adni[actual_region] = adni_name

    def toDKName(self, adni_name):
        return self.regions[adni_name]

    def toAdniName(self, dk_name):
        return self.ani[dk_name]
    

dkDict = DKDict()
print(dkDict.toDKName("ST102TA"))