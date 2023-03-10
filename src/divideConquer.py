import numpy as np
from dataType import point, couple

def isNeed(p1: point, p2: point, d:float):
    """
    return False if there is distance between p1 and p2 
    in the same axis that greater than d
    """
    for i in range(p1.dimensi):
        if (abs(p1.value[i] - p2.value[i]) >= d):
            return False
    return True

def quicksort(points: list[point]):
    if len(points) <= 1:
        return points
    else:
        pivot = points[0]
        left_part = np.empty((0), dtype=point)
        right_part = np.empty((0), dtype=point)
        for i in range(1, len(points)):
            if points[i] < pivot:
                left_part = np.append(left_part, points[i])
            else:
                right_part = np.append(right_part, points[i])
        res = np.concatenate((quicksort(left_part), np.array([pivot]) , quicksort(right_part)))
        return res

def divideConquer(points : list[point]) -> couple:
    """
    Initial State : points was sorted by x1
    return 2 closest point as a couple in points 
    and number of euclidean distance calculation
    using divide and conquer algorithm
    """
    n : int  = len(points)
    numEuclidean:int = 0
    if (n <= 2):
        numEuclidean += 1
        return couple(points[0], points[1]), numEuclidean
    
    elif (n == 3):
        numEuclidean += 3
        Couple1 = couple(points[0], points[1])
        Couple2 = couple(points[1], points[2])
        Couple3 = couple(points[0], points[2])
        return min(Couple1, Couple2, Couple3), numEuclidean

    else:
        left_part = points[:n//2]
        right_part = points[n//2:]

        closest_left, tempNumLeft = divideConquer(left_part)
        closest_right, tempNumRight = divideConquer(right_part)
        numEuclidean += (tempNumLeft + tempNumRight)

        closestTemp:couple = min(closest_left, closest_right)
        mid:float = (left_part[-1].value[0] + right_part[0].value[0]) / 2
        dist:float = abs(left_part[-1].value[0] - right_part[0].value[0])
        if (dist < closestTemp.distance):
            for left_point in left_part:
                if (abs(mid-left_point.value[0]) <= closestTemp.distance-(dist/2)) :
                    for right_point in right_part :
                        if (abs(mid-right_point.value[0]) <= closestTemp.distance-(dist/2)) :
                            if isNeed(left_point, right_point, closestTemp.distance):
                                numEuclidean += 1
                                newClosestTemp: couple = couple(left_point, right_point)
                                if (newClosestTemp < closestTemp) :
                                    closestTemp = newClosestTemp

        return closestTemp, numEuclidean

def isNeed(p1: point, p2: point, d:float):
    """
    return False if there is distance between p1 and p2 
    in the same axis that greater than d
    """
    for i in range(p1.dimensi):
        if (abs(p1.value[i] - p2.value[i]) > d):
            return False
    return True

def driver() :
    A1 = point(3,[1,3,6])
    A2 = point(3,[8,1,2])
    A3 = point(3,[8,1,1])

    List = [A1, A2, A3]

    for titik in List:
        print(titik)
    
    sorted(List)
    nearestCouple = divideConquer(List)
    print("nearest by Divide n Conquer : ", nearestCouple)

