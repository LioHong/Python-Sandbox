# -*- coding: utf-8 -*-
"""
Filename: breeding_game_02.py
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
naming_components = {0b00000000:'si', 
                     0b00000001:'ni', 0b00000010:'ga', 0b00000011:'po',
                     0b00000100:'lu', 0b00001000:'la', 0b00001100:'li',
                     0b00010000:'ra', 0b00100000:'go', 0b00110000:'va',
                     0b01000000:'to', 0b10000000:'pa', 0b11000000:'ri',
                     }

# Let's make worms. The phenotype will be their body segments.
# But worms disgust me. Still their linear body plan is somewhat elegant.
# And I'll never forget Shai'Hulud.
# Let's try hex.
body_segments = {0x0:'-', 0x1:'=', 0x2:'~', 0x3:'>',
                 0x4:'@', 0x5:'#', 0x6:'$', 0x7:'+',
                 0x8:'b', 0x9:'o', 0xA:'p', 0xB:'s',
                 0xC:'v', 0xD:'/\\', 0xE:'[]', 0xF:'{}'}
head_segments = {0x0:'(>_<)', 0x1:'(-_-)', 0x2:'(^_-)', 0x3:'(°_°)',
                 0x4:'(o|o)', 0x5:'(｀^´)', 0x6:'(^_^)', 0x7:'(T_T)',
                 0x8:'(?_?)', 0x9:'(*_*)', 0xA:'(・∀・)', 0xB:'(°◇°)',
                 0xC:'(UwU)', 0xD:'(OwO)', 0xE:'( ͡° ͜ʖ ͡°)', 0xF:'(╬ ಠ益ಠ)'}

class geneCarrier:
    def __init__(self, parent):
        self.birthdate = dt.datetime.now()
        self.parent = parent
        self.genome = self.inherit_asexually()
        self.child = None
        self.body = self.grow_body()   
    
    def intro(self):
        print('I am the geneCarrier who looks like ' + self.body)
        
    def announce_age(self):
        age = dt.datetime.now() - self.birthdate
        print('I am now ' + str(age) + ' old')
        
    def reveal_genome(self):
        print('My genome is ' + "0x{:08x}".format(self.genome) + '. Please handle it with care.')
        
    def grow_body(self):
        # Phenotype
        masks = [0xF0000000, 0x0F000000, 0x00F00000, 0x000F0000, 0x0000F000, 0x00000F00, 0x000000F0, 0x0000000F]
        # Isolate each byte
        body_genes = [mask & self.genome for mask in masks]
#        print("0x{:08x}".format(self.genome))
#        print(["0x{:08x}".format(gene) for gene in body_genes])
        # Then shift it to the rightmost bit
        body_proteins = [gene >> 4 * (7 - body_genes.index(gene)) for gene in body_genes]
#        print(["0x{:08x}".format(protein) for protein in body_proteins])
        body_parts = [body_segments[protein] for protein in body_proteins]
        worm_body = ''.join(body_parts)
        
        # Add a clearly recognisable head segment
        head_protein = sum(body_proteins) % 16
        head_part = head_segments[head_protein]
        worm_body = worm_body + head_part
        
        return worm_body
    
    def inherit_asexually(self):
        if self.parent == 'LIO':
            # If I created this instance, randomly generate its genome
            seed(dt.datetime.now())
            genome = randint(0,16**8)
        else:
            # Otherwise it will inherit its genome from its parent
            genome = self.parent.genome
            # Introduce random mutations
            mutation_rate = randint(1,64)
#            threshold = 32
            threshold = 0
#            threshold = 100
            mutated_bit = 0
            if mutation_rate > threshold:
                mutated_bit = 2 ** (mutation_rate % 8)
                # There is a 1/16 chance that no mutation will occur: When mutated_bit = 0
            # Flip the chosen bit around
            genome = mutated_bit ^ genome
        return genome
    
    def show_ancestry(self):
        # Recursive function that stops once it hits the creator
        gc_instance = self
        ancestors = []
        while gc_instance.parent != 'LIO':
            ancestors.append(gc_instance.parent.body)
            gc_instance = gc_instance.parent
        ancestry_line = ' --> '.join(ancestors)
        print('LIO --> ' + ancestry_line)
        


















        
        