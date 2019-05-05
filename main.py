class RiotShop:
    def __init__(self, rp, price, wallet=0):
        self.rp = rp
        self.rps = {310: 2.5, 650: 5, 1380: 10, 2800: 20, 5000: 35, 7200: 50}
        self.price = price
        self.wallet = wallet

    def caluclate_price(self):
        quantity =  round((self.price - self.wallet) / self.rp) if round((self.price - self.wallet) / self.rp) > 1 else 1
        cost = self.rps[self.rp] * quantity
        leftover = self.price - self.wallet - (self.rp * quantity)
        if leftover > 0:
            cost = self.rps[self.rp] * quantity + self.rps[self.caluclate_leftover(leftover)]
            return cost
        else:
          return cost

    def caluclate_leftover(self, leftover):
        for k, v in self.rps.items():
            if leftover - k <= 0:
              return k
            else:
              continue
              


def iter():
  l = [310, 650, 1380, 2800, 5000, 7200]
  li =[]
  i = 0

  for k in l:
    li.append(RiotShop(k, 3000, 240))
    print(li[i].caluclate_price())
    i += 1


iter()
