def maxArea(height):
    x = len(height)
    a = 0
    b = x-1
    area = 0
    _area = 0
    while a!=b:
        if(height[a]<height[b]):
            _area = (b-a)*height[a]
            a+=1
        else:
            _area = (b-a)*height[b]
            b-=1
        if _area > area:
            area = _area
    return area