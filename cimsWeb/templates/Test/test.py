
class SocialDistanceLevel:
    
    level = 0
    filePath =""
    
    def __init__(self, level):
        self.level = level
        if level == 2:
            self.filePath = "./level2.txt"
    
    def readDistanceCriterion(self):
        f = open(self.filePath,'r')
        data = f.readlines()
        for line in data:
            if 0 <= data.index(line) <= 2 :
                print(line)
        f.close()
        

level2 = SocialDistanceLevel(2);

level2.readDistanceCriterion();

        


