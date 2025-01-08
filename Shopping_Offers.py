class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        n = len(price)
        
        filtered_special = []
        for offer in special:
            if sum(offer[i] * price[i] for i in range(n)) > offer[-1]:
                filtered_special.append(offer)
        
        def directPurchase(needs):
            return sum(needs[i] * price[i] for i in range(n))
        
      
        def dfs(needs):
            min_cost = directPurchase(needs)
            for offer in filtered_special:
                new_needs = []
                valid = True
                for i in range(n):
                    if needs[i] < offer[i]:
                        valid = False
                        break
                    new_needs.append(needs[i] - offer[i])
                if valid:
                    min_cost = min(min_cost, offer[-1] + dfs(tuple(new_needs)))
            return min_cost
        
        return dfs(tuple(needs))
