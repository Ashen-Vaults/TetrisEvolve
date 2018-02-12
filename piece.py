import config as cfg

rotation = {
    0: lambda x, y: y * cfg.tetromino_width + x,
    90: lambda x, y: 12 + y - (x * cfg.tetromino_width),
    180: lambda x, y: 15 - (y * cfg.tetromino_width) - x,
    270: lambda x, y: 3 - y + (x * cfg.tetromino_width)
}


def rotate(x, y, degrees):
    return rotation.get(degrees, 0)(x, y);


print(rotate(1, 2, 270))
