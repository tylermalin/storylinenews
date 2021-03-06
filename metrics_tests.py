import unittest
import os
import metrics

class SentimentTest(unittest.TestCase):

    def setUp(self):
        self.reviewdir = 'data/tests/reviews/'
        self.negdir = 'neg/'
        self.posdir = 'pos/'
        self.threshold = 0 #beneath which score is considered negative
        self.minimum = 0.55 #at least slightly better than chance

    def dir_sentiment(self, directory):
        positive, negative = [], []

        join = os.path.join
        sentiment = metrics.sentiment

        directory = join(self.reviewdir, directory)

        for dirpath, dirnames, filenames in os.walk(directory):
            for name in filenames:
                f = open(join(directory, name))
                review = f.read()
                f.close()

                score = sentiment(review)

                if score < self.threshold:
                    negative.append(name)
                else:
                    positive.append(name)

        pos_count = len(positive)
        neg_count = len(negative)
        total = pos_count + neg_count
        return (pos_count, neg_count, total)

    def test_positive(self):
        results = self.dir_sentiment(self.posdir)
        pos, neg, total = results
        print 'positive results: ', pos, neg, total
        self.assertTrue(pos > neg)
        self.assertTrue(pos / float(total) > self.minimum)

    
    def test_negative(self):
        results = self.dir_sentiment(self.negdir)
        pos, neg, total = results
        print 'negative results: ', pos, neg, total
        self.assertTrue(neg > pos)
        self.assertTrue(neg / float(total) > self.minimum)
                
                
if __name__ == '__main__':
    unittest.main()
