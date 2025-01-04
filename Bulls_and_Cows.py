class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = sum(s == g for s, g in zip(secret, guess))
        secret_counter = Counter(secret)
        guess_counter = Counter(guess)
        cows = sum((secret_counter & guess_counter).values()) - bulls
        return "{}A{}B".format(bulls, cows)
        
