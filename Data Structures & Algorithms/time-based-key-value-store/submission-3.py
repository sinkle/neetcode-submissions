class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.d:
            self.d[key] = {timestamp: value, 'c': [timestamp]}
        else:
            if timestamp in self.d[key]:
                self.d[key][timestamp] = value
            else:
                self.d[key][timestamp] = value
                self.d[key]['c'].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        
        if timestamp not in self.d[key]:
            i = len(self.d[key]['c']) - 1
            while i > -1:
                if self.d[key]['c'][i] < timestamp:
                    return self.d[key][self.d[key]['c'][i]]
                else:
                    i -= 1
            return ""
        return self.d[key][timestamp]