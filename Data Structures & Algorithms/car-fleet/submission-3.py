class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []

        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        for pos, spd in cars:
            time = (target - pos) / spd
            if fleets and time <= fleets[-1]:
                continue
            if time not in fleets:
                fleets.append(time)
        
        return len(fleets)





        