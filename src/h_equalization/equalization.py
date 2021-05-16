from PIL import Image
import os

NIVEIS_DE_CINZA = 256 #rk

def to_gray_scale(img: Image, img_lines: int, img_columns: int) -> list:
    img_gray = Image.open(img.filename).convert('L')
    img_gray.save('./gray_scale/' + img.filename.split('/')[-1])

    return Image.open('./gray_scale/' + img.filename.split('/')[-1])

def get_histogram(gray_img_matrix: list, img_lines: int, img_columns: int) -> list:
    histogram = [0] * NIVEIS_DE_CINZA
    for l in range (img_lines):
        for c in range (img_columns):
            histogram[ gray_img_matrix[l][c] ] += 1

    print('\n---------------------')
    print('HISTOGRAM')
    print(histogram)
    return histogram

def get_pr_rk(nk: list) -> list:
    pr_rk = []
    sum_rk = sum(nk)
    for value in nk:
        pr_rk.append( value/sum_rk )

    print('\n---------------------')
    print('PRRK')
    print(pr_rk)

    return  pr_rk
        
def get_freq(pr_rk: list) -> list:
    freq = []
    freq.append( pr_rk[0] )
    for rk in range (1, NIVEIS_DE_CINZA):
        freq.append( pr_rk[rk] + pr_rk[rk - 1] )

    print('\n---------------------')
    print('freq')
    print(freq)

    return freq
        
def get_eq(freq: list) -> list:
    eq = []
    for value in freq:
        eq.append( (NIVEIS_DE_CINZA-1)*value )

    print('\n---------------------')
    print('eq')
    print(eq)

    return eq
        
def get_new_rk(eq: list) -> list:
    new_rk = []
    for value in eq:
        new_rk.append( int(value) )

    print('\n---------------------')
    print('new_rk')
    print(new_rk)

    return new_rk

def equalize(original_img: list, new_rk: list, img_lines: int, img_columns: int):

    print('antes')
    print(original_img)
    
    new_img = []

    for line in original_img:
        for pixel_value in line:
            new_img.append( new_rk[ pixel_value ] )
        
    # converte a lista anterior para uma lista 2D:
    new_img = [new_img[offset: offset + img_columns] for offset in range(0, img_columns*img_lines, img_columns)]
    

    print('\n---------------------')
    print('newimg22')
    print(new_img)
    return new_img
