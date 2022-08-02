import numpy


def multiplicative_utilitarian(rating):
    return numpy.prod(rating)


def additive_utilitarian(rating):
    return sum(rating)


def least_misery(rating):
    return min(rating)


def most_pleasure(rating):
    return max(rating)


def average_without_misery(rating):
    threshold = 3
    return sum(rating) if min(rating) > threshold else 0


def approval_voting(rating: list) -> int:
    threshold = 5
    return len([1 for rate in rating if rate > threshold])
