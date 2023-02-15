from mrjob.job import MRJob

class Min_Max(MRJob):

    def mapper(self, _, line):
        
        yield('Max_Temp', float(line.split()[5]))
        yield('Min_Temp', float(line.split()[6]))

    def reducer(self, word, temp):
        if word == 'Max_Temp':
            yield(word, max(temp))
        if word == 'Min_Temp':
            yield(word, min(temp))

if __name__ == '__main__':
        Min_Max.run()