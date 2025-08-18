class Solutionl:
    def numJewelsInStones(self,jewels,stones):
        count = 0
        jewelset=set(jewels)
        for stone in stones:
            if stone in jewelset:
                count += 1
        return print(count)

jewels = 'aB'
stones='AsdaabBBaAaA'
sol = Solutionl()
sol.numJewelsInStones(jewels, stones)