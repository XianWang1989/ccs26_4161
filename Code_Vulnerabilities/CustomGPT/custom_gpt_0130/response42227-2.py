
conditions = {
    (True, True, True): 'first',
    (True, True, False): 'second',
    (True, False, True): 'third',
    (True, False, False): 'fourth',
    (False, True, True): 'fifth',
    (False, True, False): 'sixth',
    (False, False, True): 'seventh',
    (False, False, False): 'eighth',
}

name = conditions[(a, b, c)]
