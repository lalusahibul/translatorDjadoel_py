kalimat = input('Masukkan kalimat jadul! ')

karakter_jadul = [
    ('OE','U'),
    ('Oe',' U'),
    ('oE','u'),
    ('oe', 'u'),
    ('DJ', '#xwgzx#'),
    ('Dj', '#xwgzxx#'),
    ('dJ', '#xwgzxxx#'),
    ('dj', '#xwgzxxxx#'),
    ('TJ', 'C'),
    ('Tj', 'C'),
    ('tJ', 'c'),
    ('tj', 'c'),
    ('NJ', 'NY'),
    ('Nj', 'Ny'),
    ('nJ', 'nY'),
    ('nj', 'ny'),
    ('SJ', 'SY'),
    ('Sj', 'Sy'),
    ('sJ', 'sY'),
    ('sj', 'sy'),
    ('CH', 'KH'),
    ('Ch', 'Kh'),
    ('cH', 'kH'),
    ('ch', 'kh'),
    ('J', 'Y'),
    ('j', 'y'),
    ('#xwgzx#', 'J'),
    ('#xwgzxx#', 'J'),
    ('#xwgzxxx#', 'j'),
    ('#xwgzxxxx#', 'j')
]

for karakter_asli, karakter_baru in karakter_jadul:
    kalimat = kalimat.replace(karakter_asli, karakter_baru)

print('============================================')
print(kalimat)
print('============================================')
