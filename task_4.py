class Unit:
    # ...
    def move(self, field, x_coord: int, y_coord: int, direction, is_fly: bool, crawl: bool, speed: int = 1):

        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            match(direction):
                case 'UP':
                    new_y = y_coord + speed
                    new_x = x_coord
                case 'DOWN':
                    new_y = y_coord - speed
                    new_x = x_coord
                case 'LEFT':
                    new_y = y_coord
                    new_x = x_coord - speed
                case 'RIGTH':
                    new_y = y_coord
                    new_x = x_coord + speed
        if crawl:
            speed *= 0.5
            match(direction):
                case 'UP':
                    new_y = y_coord + speed
                    new_x = x_coord
                case 'DOWN':
                    new_y = y_coord - speed
                    new_x = x_coord
                case 'LEFT':
                    new_y = y_coord
                    new_x = x_coord - speed
                case 'RIGTH':
                    new_y = y_coord
                    new_x = x_coord + speed

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
