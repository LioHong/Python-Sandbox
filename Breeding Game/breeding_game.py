# -*- coding: utf-8 -*-
"""
Filename: breeding_game_01.py
Date created: Thu Aug  6 00:44:32 2020
@author: Julio Hong
Purpose: I want to breed computer programs for some reason.
Steps: Create a base creature that can inherit genes from both parents
I guess asexual reproduction is easiest to start with? Just change identity and birthdate.
Then can add mutations.
"""
# Start with a simple 8-bit genome
import datetime as dt
from random import seed
from random import randint

# I probably should have done 16 bits, so 4 name_parts * 4 possiblities
naming_components = {0b00000000: 'si',
                     0b00000001: 'ni', 0b00000010: 'ga', 0b00000011: 'po',
                     0b00000100: 'lu', 0b00001000: 'la', 0b00001100: 'li',
                     0b00010000: 'ra', 0b00100000: 'go', 0b00110000: 'va',
                     0b01000000: 'to', 0b10000000: 'pa', 0b11000000: 'ri',
                     }


class geneCarrier:
    def __init__(self, parent):
        self.birthdate = dt.datetime.now()
        self.parent = parent
        self.genome = self.inherit_asexually()
        self.child = None
        self.name = self.christen_name()

    def intro(self):
        print('I am the geneCarrier called ' + self.name)

    def announce_age(self):
        age = dt.datetime.now() - self.birthdate
        print('I am now ' + str(age) + ' old')

    def reveal_genome(self):
        print('My genome is ' + str(format(self.genome, '08b')) + '. Please handle it with care.')

    def christen_name(self):
        # This makes the name the phenotype. Maybe I'll call it true_name next time?
        mask_01 = 0b11000000
        mask_02 = 0b00110000
        mask_03 = 0b00001100
        mask_04 = 0b00000011
        name_part_01 = mask_01 & self.genome
        name_part_02 = mask_02 & self.genome
        name_part_03 = mask_03 & self.genome
        name_part_04 = mask_04 & self.genome

        name = naming_components[name_part_01] + \
               naming_components[name_part_02] + \
               naming_components[name_part_03] + \
               naming_components[name_part_04]
        return name.capitalize()

    def inherit_asexually(self):
        if self.parent == 'LIO':
            # If I created this instance, randomly generate its genome
            seed(dt.datetime.now())
            genome = randint(0, 255)
        else:
            # Otherwise it will inherit its genome from its parent
            genome = self.parent.genome
            # Introduce random mutations
            mutation_rate = randint(1, 64)
            #            threshold = 32
            threshold = 0
            #            threshold = 100
            mutated_bit = 0
            if mutation_rate > threshold:
                mutated_bit = 2 ** (mutation_rate % 8)
                # There is a 1/8 chance that no mutation will occur: When mutated_bit = 0
            # Flip the chosen bit around
            genome = mutated_bit ^ genome
        return genome

    def show_ancestry(self):
        # Recursive function that stops once it hits the creator
        gc_instance = self
        ancestors = []
        while gc_instance.parent != 'LIO':
            ancestors.append(gc_instance.parent.name)
            gc_instance = gc_instance.parent
        ancestry_line = ' --> '.join(ancestors)
        print('LIO --> ' + ancestry_line)




