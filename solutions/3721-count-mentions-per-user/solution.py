from collections import defaultdict
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        time_map = defaultdict(list)
        for ev in events:
            typ, ts, arg = ev
            t = int(ts)
            time_map[t].append((typ, arg))
        mentions = [0] * numberOfUsers
        offline_until = [0] * numberOfUsers
        for t in sorted(time_map):
            offs = []
            msgs = []
            for typ, arg in time_map[t]:
                if typ == "OFFLINE":
                    offs.append(arg)
                else:
                    msgs.append(arg)
            for arg in offs:
                uid = int(arg)
                offline_until[uid] = t + 60
            for arg in msgs:
                s = arg.strip()
                if s == "ALL":
                    for u in range(numberOfUsers):
                        mentions[u] += 1
                elif s == "HERE":
                    for u in range(numberOfUsers):
                        if offline_until[u] <= t:
                            mentions[u] += 1
                else:
                    for token in s.split():
                        if token.startswith("id"):
                            uid = int(token[2:])
                            mentions[uid] += 1
        return mentions
