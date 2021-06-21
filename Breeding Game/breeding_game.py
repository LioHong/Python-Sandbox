# -*- coding: utf-8 -*-
"""
Filename: breeding_game_05.py
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
from random import sample
import numpy as np
from pprint import pprint
from collections import OrderedDict

# Let's make worms. The phenotype will be their body segments.
# But worms disgust me. Still their linear body plan is somewhat elegant.
# And I'll never forget Shai'Hulud.
# Let's try hex.
# For a 2D creature maybe we could use pandas? Kind of like storing each creature in a box.
# Arguable whether it's easier to compare worm bodies or text sequences
# But it was good practice for simulating the Central Dogma: Gene > Protein > Phenotype
# Difference: Single-stranded, two bases, four-base codon, no degeneracy
# No need to reproduce DNA rules though, we're looking at this from a genetic POV
body_segments = {0x0: '-', 0x1: '—', 0x2: '=', 0x3: '○',
                 0x4: '~', 0x5: '≈', 0x6: '¤', 0x7: '∞',
                 0x8: 'c', 0x9: 'g', 0xA: 'o', 0xB: '÷',
                 0xC: '→', 0xD: '↔', 0xE: '◄', 0xF: '☼'}
head_segments = {0x0: '(>_<)', 0x1: '(-_-)', 0x2: '(^_-)', 0x3: '(°_°)',
                 0x4: '(o|o)', 0x5: '(｀^´)', 0x6: '(^_^)', 0x7: '(T_T)',
                 0x8: '(?_?)', 0x9: '(*_*)', 0xA: '(・∀・)', 0xB: '(°◇°)',
                 0xC: '(UwU)', 0xD: '(OwO)', 0xE: '( ͡° ͜ʖ ͡°)', 0xF: '(╬ ಠ益ಠ)'}


class geneCarrier:
    # How do I distinguish between instances?
    # Genome and birthdate aren't enough are they?
    # Identical twins are not the same persons
    # Maybe give them an instance number. Can track for only child, but siblings?
    # Own number + number of children? Or need a global count
    # Eventually add an alive/dead tag as well, so can track living population as all those with the alive tag
    def __init__(self, parents):
        self.birthdate = dt.datetime.now()
        self.parents = parents
        # Number of parents determines if reproduction is asexual or sexual
        if type(parents) == list:
            self.genome = self.inherit_sexually()
        else:
            self.genome = self.inherit_asexually()
        self.body = self.grow_body()
        self.children = []

    def intro(self):
        print('I am the geneCarrier of gen ' + str(self.generation) + ' who looks like:    ' + self.body)

    def announce_age(self):
        age = dt.datetime.now() - self.birthdate
        print('I am now ' + str(age) + ' old')

    def reveal_genome(self):
        print('My genome is ' + "0x{:08X}".format(self.genome) + '. Please handle it with care.')

    def grow_body(self):
        # Phenotype
        # I could actually generate masks up to an arbitrary number of hexbits
        num_of_genes = 8
        masks = [15 * 16 ** x for x in reversed(range(num_of_genes))]
        #        masks = [0xF0000000, 0x0F000000, 0x00F00000, 0x000F0000, 0x0000F000, 0x00000F00, 0x000000F0, 0x0000000F]
        # Isolate each byte
        body_genes = [mask & self.genome for mask in masks]
        #        print("0x{:08X}".format(self.genome))
        #        print(["0x{:08X}".format(gene) for gene in body_genes])
        # Then shift it to the rightmost bit
        body_proteins = [gene >> 4 * (7 - body_genes.index(gene)) for gene in body_genes]
        #        print(["0x{:08X}".format(protein) for protein in body_proteins])
        body_parts = [body_segments[protein] for protein in body_proteins]
        worm_body = ''.join(body_parts)

        # Add a clearly recognisable head segment
        head_protein = sum(body_proteins) % 16
        head_part = head_segments[head_protein]
        # Add a standardised tail for clarity
        #        worm_body = '—=≡' + worm_body + head_part
        worm_body = '—=' + worm_body + head_part

        return worm_body

    def inherit_asexually(self):
        if self.parents == 'LIO':
            # If I created this instance, randomly generate its genome
            seed(dt.datetime.now())
            genome = randint(0, 16 ** 8)
            # Include a generation parameter
            self.generation = 0
        else:
            # Otherwise it will inherit its genome from its parent
            genome = self.parents.genome
            # Assume generation is from parent + 1
            # But what if parents are from different generations?
            self.generation = self.parents.generation + 1
            # Introduce random mutations
            mutation_rate = randint(1, 64)
            #            threshold = 32
            threshold = 0
            #            threshold = 100
            mutated_hexbit = 0
            # If flip_value is constant then there would only be 2^8 possible deviations from the first worm's genome
            flip_value = randint(0, 15)
            # Number of bits to mutate could also be modular
            if mutation_rate > threshold:
                mutated_hexbit = flip_value << (4 * (mutation_rate % 8))

            # Flip the chosen bit around with bitwise XOR
            #            print("0x{:08X}".format(mutated_hexbit))
            #            print("0x{:08X}".format(genome) + ' ^ ' + "0X{:08X}".format(mutated_hexbit))
            genome = mutated_hexbit ^ genome
        #            print("0x{:08X}".format(genome) + '____')
        return genome

    def birth_daughter_asexually(self):
        daughter = geneCarrier(parents=self)
        self.children.append(daughter)
        return daughter

    def show_ancestry(self):
        # Recursive function that stops once it hits the creator
        gc_instance = self
        # Start with self
        ancestors = [self.body]
        while isinstance(gc_instance.parents, geneCarrier):
            ancestors.append(gc_instance.parents.body)
            gc_instance = gc_instance.parents
        # Latest gen is entry 0, first ancestor is final entry so reverse it
        ancestors.reverse()
        ancestry_line = '  —►  '.join(ancestors)
        print('LIO  —►  ' + ancestry_line)

    def show_children(self):
        print(self.body)
        print('| BEGET')
        for child in self.children:
            print('↳ ' + child.body)


#    def show_siblings(self):
#        self.parents.children

#    def inherit_sexually(self):
#        # Show each generation as a line I guess
#        # And how to handle siblings?
#        # Cursed thought: Can we have multiple parents?... But only in powers of 2
#        # That would be a terrifying family tree.

# I've heard that automatically generating variables is a bad idea but let's find out why
number_of_variables = 10000
population = [0 for num in range(number_of_variables)]
# This automatically generates a family tree up to a desired number of generations
population[0] = geneCarrier('LIO')
latest_generation = 1000
for num in range(1, latest_generation):
    # This creates a sequence of descendants
    population[num] = population[num - 1].birth_daughter_asexually()


#    # This creates siblings
#    population[num] = population[0].birth_daughter_asexually()
# population[latest_generation-1].show_ancestry()
# population[0].intro()
# population[latest_generation-1].intro()

def compare_genomes(gc_baseline, gc_others: list):
    # Find out which hexbits have changed
    # I guess it'll also see how much they've changed
    # Maybe I can compare multiple geneCarriers against a single baseline
    # Is there a way to extract the number of genes from the length of the genome?
    num_of_genes = 8
    masks = [15 * 16 ** x for x in reversed(range(num_of_genes))]
    gc_baseline_genes = [mask & gc_baseline.genome for mask in masks]
    gcbase_hexgenes = ["0x{:08X}".format(mask & gc_baseline.genome) for mask in masks]
    #    print(gcbase_hexgenes)
    # Printing in a hex format takes up a lot of effort actually
    gc_others_genes = OrderedDict()
    gcs_deltas = OrderedDict()
    gcs_deltas_hex = OrderedDict()
    for gc in gc_others:
        gcgenome_hex = "0x{:08X}".format(gc.genome)
        gc_others_genes[gcgenome_hex] = [mask & gc.genome for mask in masks]
        gcs_deltas[gcgenome_hex] = np.array(gc_others_genes[gcgenome_hex]) - np.array(gc_baseline_genes)
        # Maybe I remove all the zero values
        gcs_deltas_hex[gcgenome_hex] = [delta for delta in gcs_deltas[gcgenome_hex] if delta != 0]
        #        gcs_deltas_hex[gcgenome_hex] = ["0x{:08X}".format(delta) for delta in gcs_deltas[gcgenome_hex]]
        gcs_deltas_hex[gcgenome_hex] = ["0x{:08X}".format(delta) for delta in gcs_deltas_hex[gcgenome_hex]]

    # Negative values have '-' taking up the leftmost bit
    print("0x{:08X}".format(gc_baseline.genome))
    pprint(gcs_deltas_hex)

#    print('The genomes have changed by these values: ' + "0x{:08X}".format(delta_genome))











