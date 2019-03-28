# -*- coding: utf-8 -*-

def genPrimes():
    _Primes = []

    while True:
        if len(_Primes) == 0:
            _number = 2
            _Primes.append(_number)
            yield _number
            _number += 1

        _notPrime = False
        for _prime in _Primes:
            if _number % _prime == 0:
                _notPrime = True
                break

        if _notPrime:
            _number += 1
            continue
        else:
            _Primes.append(_number)
            yield _number
            _number += 1
