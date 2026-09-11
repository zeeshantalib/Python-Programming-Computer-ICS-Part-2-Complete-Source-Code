class Bill:

    def calculate_bill(self, *prices):
        total = sum(prices)
        print("Total Bill:", total)


bill = Bill()

bill.calculate_bill(500)
bill.calculate_bill(500, 300)
bill.calculate_bill(500, 300, 200)
bill.calculate_bill(500, 300, 200, 100)