from typing import List
import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        order_index = {b: i for i, b in enumerate(order)}
        pattern = re.compile(r'^[A-Za-z0-9_]+$')
        
        valid = []
        for c, b, a in zip(code, businessLine, isActive):
            if not a:
                continue
            if not c or not pattern.match(c):
                continue
            if b not in order_index:
                continue
            valid.append((order_index[b], c))
        
        valid.sort()
        return [c for _, c in valid]
