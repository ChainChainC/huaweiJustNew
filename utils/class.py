import re
import numpy as np


class Rob:
    def __init__(self, pos:tuple) -> None:
        self.pos = pos # inside map
        self.av = 0 # [-pi, pi] angular velocity
        self.v = 0 # [-2, 6] velocity
        self.cargo = -1 # [0, 7] cargo type 
        self.wks = -1 # [0, #wks-1] 
        self.dir = (0, 0)
        pass

    def update(self, **param:dict) -> None:
        self.pos = param.pos

class Map:
    ## 读入地图，速度·角动量等在路径规划中合并
    def __init__(self, map_dir:str) -> list:
        self.wkstation = dict()
        self._latter_width = 0.5
        self._latter_bias = 0.25
        
        
        rob = list()
        re_matcher = re.compile(r"(A|[1-9])") 
        f = open(map_dir, "r", encoding = "utf8")
        line = f.readline()
        row_num = 0
        while line:
            for reg in re_matcher.finditer(line.strip()):
                
                pos = (row_num * self._latter_width + self._latter_bias,
                    reg.start() * self._latter_width + self._latter_bias)
                
                l = reg.group()
                if l == "A":
                    rob = [pos] if not rob else rob + [pos]
                else:
                    self.wkstation[l] = [pos] if l not in self.wkstation.keys() else self.wkstation[l] + [pos]
            row_num += 1
        
        f.close()
        return rob
         
    ## 目的是每帧赚的钱越多越好                    
    def iter_opt_path():
        pass
    
    def command_submit(self) -> None:
        pass
    
    
    
        
        
