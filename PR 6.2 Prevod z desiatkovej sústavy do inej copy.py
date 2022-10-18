print(
    cislo := [], 
    [(prevod := lambda c, r: [cislo.append(c%r), (prevod(c//r, r) if c//r != 0 else cislo.append((orig, r)))])(c, r) 
        for [((c, orig),), r] in [[[(i, i) for i in (int(input('cislo v desiatkovej sustave: ')),)], 
                                              int(input('radix v desiatkovej sustave: '))]]
    ]
    )