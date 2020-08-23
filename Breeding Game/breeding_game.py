# -*- coding: utf-8 -*-
"""
Filename: breeding_game.py
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
import pandas as pd
from pprint import pprint
from collections import OrderedDict
from itertools import combinations

# Let's make worms. The phenotype will be their body segments.
# But worms disgust me. Still their linear body plan is somewhat elegant.
# And I'll never forget Shai'Hulud.
# Let's try hex.
# For a 2D creature maybe we could use pandas? Kind of like storing each creature in a box.
# Arguable whether it's easier to compare worm bodies or text sequences
# But it was good practice for simulating the Central Dogma: Gene > Protein > Phenotype
# Difference: Single-stranded, two bases, four-base codon, no degeneracy, 1 codon = 1 gene
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
        self.num_of_genes = 8
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
        masks = [15 * 16 ** x for x in reversed(range(self.num_of_genes))]
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
            genome = randint(0, 16 ** self.num_of_genes)
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
                mutated_hexbit = flip_value << (4 * (mutation_rate % self.num_of_genes))

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

    def show_ancestry_asexually(self):
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

    def inherit_sexually(self):
        # Inherit half the genes from one parent and the other half from the other
        # Or 1/4 the genes from each of 4 parents
        # Or 1/8 the genes from each of 8 parents...
        # Of course the below code is excessive for two parents
        # Can deal with uneven divisions by randomly allocating inheritance counts to each parent?
        num_of_parents = len(self.parents)
        length_of_inheritance_set = round(self.num_of_genes / num_of_parents)
        order_of_inheritance = sample(range(0, self.num_of_genes), self.num_of_genes)
        # Mutation could actually happen at this stage with 15 * factor
        masks = [15 * 16 ** x for x in reversed(range(self.num_of_genes))]
        # Decide the order to inherit gene_masks
        reordered_masks = [masks[x] for x in order_of_inheritance]
        new_genome = []

        # Copy the selected number of genes from each parent
        # I can't use a dict because I don't have a UUID for each GC
        for parent in self.parents:
            for mask in reordered_masks[:length_of_inheritance_set]:
                new_genome.append(mask & parent.genome)
            for entry in range(length_of_inheritance_set):
                reordered_masks.pop(0)
        # new_genome_hex = ["0x{:08X}".format(gene) for gene in new_genome]
        # print(new_genome_hex)
        new_combined_genome = sum(new_genome)
        # print("0x{:08X}".format(new_combined_genome))
        return new_combined_genome

# Show each generation as a line I guess
# And how to handle siblings?
# Cursed thought: Can we have multiple parents?... But only in powers of 2
# That would be a terrifying family tree.


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
    num_of_genes = round(gc_baseline.genome.bit_length() / 4)
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

def pop_genosphere_breakdown(num_of_allelles, num_of_genes):
    #different_alleles ** (#different_genes - #identical_genes) * (#different_genes C #identical_genes)
    breakdown_table = pd.DataFrame(data=None, index=range(num_of_genes+1), columns=['num_possibilites', 'chance']) 
    breakdown_table.index.name = 'num_identical_genes'
    for val in range(num_of_genes+1):
        breakdown_table.loc[val, 'num_possibilites'] = (num_of_allelles-1) ** (num_of_genes - val) * len(list(combinations(range(num_of_genes),val)))
    genosphere_size = num_of_allelles ** num_of_genes
    if genosphere_size - breakdown_table['num_possibilites'].sum() != 0:
        print('WARNING! Check the sum of possible genetic combinations!')
        print('Deviation of ' + str(genosphere_size - breakdown_table['num_possibilites'].sum()))
        return breakdown_table
    else:
        breakdown_table['chance'] = breakdown_table['num_possibilites'] / genosphere_size * 100
#        breakdown_table['chance'] = 
        # Find a way to present the values as 3sig fig? Seems hard
        # Find expected number of identical genes 90% of the time
        target_pct = 90
        breakdown_table['cum_chance'] = breakdown_table['chance'].cumsum()
        
        return breakdown_table







