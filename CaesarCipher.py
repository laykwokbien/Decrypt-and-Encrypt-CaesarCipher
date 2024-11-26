kataoriginal = input('Masukkan Kata yang mau diEncrypt atau diDecrypt: ').upper()

# Membuat Alphabet dari A - Z
alphabet = []

for word in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    alphabet.append(word)

def encryptCaesar(kata):
    # Variable Index digunakan untuk meletakkan Index dari alphabet
    index = []

    # Variable Reset Index digunakan untuk mereset index 
    resetindex = []
    
    # Mengambil Index dari setiap kata aslinya / kata yang sebelum encrypt
    for word in kata:
        for i in range(len(alphabet)):
            if word == alphabet[i]:
                index.append(i)

    # Hasil dari gesersan ke-n / n = 1 - 25
    resultencrypt = {
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: '',
        10: '',
        11: '',
        12: '',
        13: '',
        14: '',
        15: '',
        16: '',
        17: '',
        18: '',
        19: '',
        20: '',
        21: '',
        22: '',
        23: '',
        24: '',
        25: '',
    }

    # Mengisi Variable resetIndex
    for i in range(len(index)):
        resetindex.append(index[i])

    for i in resultencrypt:
        for id in range(len(index)):
            # Melakukan Pergeseran ke kanan / ditambahkan sebanyak n atau sesuai dengan variable i
            index[id] = (index[id] + i)
            # Melakukan sisa bagi agar index tidak melebihi 26 dan kembali ke index 0/sesuai dengan hasil sisa bagi
            if index[id] >= 26:
                index[id] = index[id] % 26
            # Menambahkan alphabet berdasarkan index yang telah digeser
            resultencrypt[i] += alphabet[index[id]]
        # Mereset Index menjadi Index awalnya / Index Kata Aslinya
        for id in range(len(resetindex)):
            index[id] = resetindex[id]

    # Mengembalikan Hasil Encrypt
    return(resultencrypt)

def decryptCaesar(kata):
    # Variable untuk meletakkan index dari setiap alphabet
    index = []

    # Variable yang digunakan untuk mereset variable index pada nantinya
    resetindex = []

    # Manambahkan Index yang sesuai dengan kata aslinyua / kata sebelum decrypt
    for word in kata:
        for i in range(len(alphabet)):
            if word == alphabet[i]:
                index.append(i)

    # Hasil dari gesersan ke-n / n = 1 - 25
    resultdecrypt = {
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: '',
        10: '',
        11: '',
        12: '',
        13: '',
        14: '',
        15: '',
        16: '',
        17: '',
        18: '',
        19: '',
        20: '',
        21: '',
        22: '',
        23: '',
        24: '',
        25: '',
    }

    # Mengisi Variable Reset Index untuk menjadi 
    for i in range(len(index)):
        resetindex.append(index[i])

    for i in resultdecrypt:
        for id in range(len(index)):
            # Melakukan Pergeseran ke kiri / dikurangi sebanyak n atau sesuai dengan variable i
            index[id] = (index[id] - i)
            # Melakukan sisa bagi agar index tidak melebihi 0 dan kembali ke index 25/sesuai dengan hasil sisa bagi
            if index[id] < 0:
                index[id] = index[id] % 26
            # Menambahkan alphabet berdasarkan index yang telah digeser
            resultdecrypt[i] += alphabet[index[id]]
        # Mereset Index menjadi Index awalnya / Index Kata Aslinya
        for id in range(len(resetindex)):
            index[id] = resetindex[id]

    # Mengembalikan Hasil Decrypt
    return(resultdecrypt)

hasilencrypt = encryptCaesar(kataoriginal)

print('Hasil Encrypt:', kataoriginal)
print('Hasil')
print(hasilencrypt)
print('\n')

hasildecrypt = decryptCaesar(hasilencrypt[5])

print('Hasil Decrypt:', hasilencrypt[5])
print('Hasil')
print(hasildecrypt)
print('\n')

# ======== Array Type Encrypter and Decrypter =========
# def encryptMultiCaesar(kata):
#     resultencrypt = {
#             1: '',
#             2: '',
#             3: '',
#             4: '',
#             5: '',
#             6: '',
#             7: '',
#             8: '',
#             9: '',
#             10: '',
#             11: '',
#             12: '',
#             13: '',
#             14: '',
#             15: '',
#             16: '',
#             17: '',
#             18: '',
#             19: '',
#             20: '',
#             21: '',
#             22: '',
#             23: '',
#             24: '',
#             25: '',
#         }
#     for i in kata:
#         index = []
#         resetindex = []

#         for word in kata[i]:
#             for id in range(len(alphabet)):
#                 if word == alphabet[id]:
#                     index.append(id)
        
#         for id in range(len(index)):
#             resetindex.append(index[id])

#         for id in range(len(index)):
#             index[id] = (index[id] + i)
#             if index[id] > 25:
#                 index[id] = index[id] % 26
#             resultencrypt[i] += alphabet[index[id]]
#         for id in range(len(resetindex)):
#             index[id] = resetindex[id]

#     return resultencrypt

# def decryptMultiCaesar(kata):
#     resultdecrypt = {
#             1: '',
#             2: '',
#             3: '',
#             4: '',
#             5: '',
#             6: '',
#             7: '',
#             8: '',
#             9: '',
#             10: '',
#             11: '',
#             12: '',
#             13: '',
#             14: '',
#             15: '',
#             16: '',
#             17: '',
#             18: '',
#             19: '',
#             20: '',
#             21: '',
#             22: '',
#             23: '',
#             24: '',
#             25: '',
#         }

#     for i in kata:
#         index = []
#         resetindex = []

#         for word in kata[i]:
#             for id in range(len(alphabet)):
#                 if word == alphabet[id]:
#                     index.append(id)
        
#         for id in range(len(index)):
#             resetindex.append(index[id])

#         for id in range(len(index)):
#             index[id] = (index[id] - i)
#             if index[id] < 0:
#                 index[id] = index[id] % 26
#             resultdecrypt[i] += alphabet[index[id]]
#         for id in range(len(resetindex)):
#             index[id] = resetindex[id]

#     return resultdecrypt