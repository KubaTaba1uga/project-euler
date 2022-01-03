THE_NUMBER = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450""".replace(
    "\n", ""
)


class BiggestAdjacentProduct:
    def __init__(self, number: str, how_many_digits: int = 4):
        self.number = number
        self.how_many_digits = how_many_digits
        self.biggest_product_digits = None

    def find_adjacent_digits(self):
        for i in range(len(self.number) - self.how_many_digits + 1):
            yield self.number[i : i + self.how_many_digits]

    @classmethod
    def calc_product(cls, number: str):
        product = 1
        for digit in (int(i) for i in number):
            product *= digit
        return product

    def calc_adjacent_products(self):
        for adjacent_digits in self.find_adjacent_digits():
            yield self.calc_product(adjacent_digits), adjacent_digits

    def find_biggest_adjacent_product(self):
        maximum = 0, "non exsisting"

        for digits_repr in self.calc_adjacent_products():

            if digits_repr[0] > maximum[0]:
                maximum = digits_repr

        self.biggest_product_digits = maximum[1]
        return maximum[0]


my_number = BiggestAdjacentProduct(THE_NUMBER, 13)
biggest_adjascent_value = my_number.find_biggest_adjacent_product()

print(f"{biggest_adjascent_value=}")
