import re
import numpy as np

class Map:
    ## 读入地图，速度·角动量等在路径规划中合并
    def __init__(self, map_dir:str) -> None:
        self.wkstation = dict()
        self.rob = list()
        self._latter_width = 0.5
        self._latter_bias = 0.25
        
        
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
                    self.rob = [pos] if  not self.rob else self.rob + [pos]
                else:
                    self.wkstation[l] = [pos] if l not in self.wkstation.keys() else self.wkstation[l] + [pos]
    
    ## 目的是每帧赚的钱越多越好                    
    def iter_opt_path():
        pass
    
    def command_submit(self) -> None:
        pass
    
    
    
        
        
