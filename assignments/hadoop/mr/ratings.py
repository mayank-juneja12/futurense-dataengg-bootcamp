from mrjob.job import MRJob

class Rating(MRJob):
    def mapper(self, _, line):
        rating = line.split(',')[2]
        # print(ratings[0])
        if not rating.isalpha():
            yield(rating, 1)

    
    def reducer(self, rating, counts):
        yield(rating, sum(counts))


if __name__ == '__main__':
        Rating.run()