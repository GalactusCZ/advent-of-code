class Robots():
    def __init__(self, height: int, width: int, robots: list[tuple[int, int, int, int]]) -> None:
        self.height = height
        self.width = width
        self.robots = robots
        
    def move(self, amount: int) -> None:
        for i, (x, y, m_x, m_y) in enumerate(self.robots):
            x = (x + m_x * amount)
            y = (y + m_y * amount)
            
            if x < 0:
                x = (((-x) // self.width + 1) * self.width + x) % self.width
            else:
                x %= self.width
            if y < 0:
                y = (((-y) // self.height + 1) * self.height + y) % self.height
            else:
                y %= self.height
                
            self.robots[i] = (x, y, m_x, m_y)

    def draw(self) -> None:
        coords = [(x, y) for x, y, _, _ in self.robots]

        for y in range(self.height):
            new_line = ''
            for x in range(self.width):
                if (x, y) in coords:
                    new_line += '1'

                else:
                    new_line += ' '

            print(new_line)
        
    def count_quadrants(self) -> int:
        results = [0, 0, 0, 0]
        mid_x = self.width // 2
        mid_y = self.height // 2
        
        for x, y, _, _ in self.robots:
            if x != mid_x and y != mid_y:
                x_higher = x > mid_x
                y_higher = y > mid_y
                
                if not x_higher and not y_higher:
                    results[0] += 1
                    
                elif x_higher and not y_higher:
                    results[1] += 1
                    
                elif not x_higher and y_higher:
                    results[2] += 1
                    
                elif x_higher and y_higher:
                    results[3] += 1
        print(results)
        return results[0] * results[1] * results[2] * results[3]
        
with open("day_14.txt") as f:
        robots: list[tuple[int, int, int, int]] = []
        
        for line in f:
           line = line.replace("\n", "").split(' ')
           
           pos = line[0].split('=')
           pos = pos[1].split(',')
           vec = line[1].split('=')
           vec = vec[1].split(',')
           
           robots.append((int(pos[0]), int(pos[1]), int(vec[0]), int(vec[1])))
       
robots_o = Robots(103, 101, robots)

# 1286
# 2757
# robots_o.move(85000)
for i in range(0, 100000000000, 1):
    print(i + 1)
    robots_o.move(1)
    nineteen = set([(x, y) for x, y, _, _ in robots_o.robots if y == 19])
    if len(nineteen) > 10:
        robots_o.draw()
    print(' ')