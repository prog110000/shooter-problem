class Shooter:
    def __init__(self) -> None:
        self.guns = {
            'Submachine Gun':(100, 10, 0.5),
            'Assault Rifle': (200, 20, 1),
            'Pistol': (80,8,0.5),
            'Shotgun': (50,40,4),
            'Sniper Rifle': (1000,30,3)
            }
        self.bullets = {
            'A':(0.5, 1),
            'B':(1, 1.5),
            'C':(3,3),
            'D':(4,2)
        }
        self.sizes = (0.5,1,3,4)
        self.gun, self.bullet, self.count = 0,0,0

    def set_gun_by_name(self, name: str) -> None:
        if name in self.guns:
            self.gun = self.guns[name]
        else:
            raise ValueError()

    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:
        self.count = count
        if self.gun:
            if count >= 0:
                if size in self.sizes:
                    for i in self.bullets:
                        if self.bullets[i][0] == size:
                            if size == self.gun[2]:
                                self.bullet = self.bullets[i]
                                break
                            else:
                                raise ValueError()
                else:
                    raise ValueError()
            else:
                raise ValueError()
        else:
            raise ValueError()

    def shoot_to_target(self, target_x: int,  target_y: int,  target_distance: int,  aim_x: int,  aim_y: int) -> float:
        if self.count > 0:
            if self.bullet:
                if target_x <= aim_x <= target_x + 10 and target_y <= aim_y <= target_y + 10:
                    if target_distance <= self.gun[0]:
                        self.count -= 1
                        return self.gun[1] * self.bullet[1]
                    else:
                        self.count
                        return 0
                else:
                    return 0
            else:
                raise ValueError()
        else:
            raise ValueError()