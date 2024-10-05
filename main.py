def old_new(teks):
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
        teks = teks.replace(karakter_asli, karakter_baru)

    return teks
def new_old(teks):
    karakter_baru = [
    ('U','Oe'),
    ('u','oe'),
    ('J', '#xwgzx#'),
    ('j', '#xwgzxx#'),
    ('C', 'Tj'),
    ('c', 'tj'),
    ('NY', 'NJ'),
    ('Ny', 'Nj'),
    ('nY', 'nJ'),
    ('ny', 'nj'),
    ('SY', 'SJ'),
    ('Sy', 'Sj'),
    ('sY', 'sJ'),
    ('sy', 'sj'),
    ('KH', 'CH'),
    ('Kh', 'Ch'),
    ('kH', 'cH'),
    ('kh', 'ch'),
    ('Y', 'J'),
    ('y', 'j'),
    ('#xwgzx#', 'Dj'), 
    ('#xwgzxx#', 'dj'), 
]

    for karakter_asli, karakter_jadul in karakter_baru:
        teks = teks.replace(karakter_asli, karakter_jadul)

    return teks

pilihan = True
while(pilihan): 
    pilih_mode = input('1. Translate ejaan jadul ke modern\n2. Ejaan modern ke jadul\nPilih (1/2): ')
    if pilih_mode == '1':
        teks_input = input('Masukkan teks ejaan jadul! ')
        teks_hasil =  old_new(teks_input)
        pilihan = False
    elif pilih_mode == '2':
        teks_input = input('Masukkan teks ejaan modern! ')
        teks_hasil =  new_old(teks_input)
        pilihan = False
    else:
        print('Pilihan tidak valid. Silakan pilih 1 atau 2.')
        
print('============================================')
print(teks_hasil)
print('============================================')
