import os

class Encrypt:
    def __init__(self):
        pass

    def letter_number_cipher(self, letters, offset):
        total = ''
        for letter in letters:

            if letter == ' ':
                total += str(ord(letter) - 32 + offset)
            elif letter == '!':
                total += str(ord(letter) + 20 + offset)
            elif letter.capitalize() == letter:
                total += str(ord(letter) - 38 + offset) 
            else:
                total += str(ord(letter) - 96 + offset)
                
        return int(total)   
    
    def advanced_letter_number_cipher(self, letters, offset):
        cipher = self.__get_cipher_details("character_set1.txt")
        total = ''
        cipher_letter = ''
        encrypted_number = 0
        
        for letter in letters:
            encrypted_number = cipher[letter]
            
            for x in range (0, offset):
                encrypted_number += 1
                if encrypted_number >= 99:
                    encrypted_number = 0
                print(f"{encrypted_number} : {x}")        
                
            if encrypted_number > 9:
                total += str(encrypted_number)
            else:
                total += '0' + str(encrypted_number)
        return int(total)

    def __get_cipher_details(self, filename):
        dir = "/Users/liamcoles/Projects/skills_workshops/practicals/adventures/cipher-world/char_sets"
        os.chdir(dir)
        f = open(filename)
        results_dict = {}
        for line in f:
            if 'character' not in line:
                results_dict[line[0]] = int(line.replace('\n','')[3:5])
        f.close()
        return results_dict



