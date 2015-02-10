# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: CALEB KISSEL

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    matchings = {"A": 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return matchings[nucleotide]

    
def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    # return ''.join(L)
    rev_complement=""
    for i in range(len(dna)):
        rev_complement=rev_complement + get_complement(dna[-1-i])
    return rev_complement

    pass

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    """
    # amber="TAG"
    # ochre="TAA"
    # opal="TGA"

    codon=0
    for i in range(len(dna)/3):
        codon=dna[3*i:(3*i+3)]
        if aa_table[codon] == '|':
        # if codon==amber or codon==ochre or codon==opal:
            return dna[0:3*i]
    return dna

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    i=0
    n=0
    ORF = []
    while i<=(len(dna)/3):
        if dna[i*3:i*3+3] == 'ATG' or 'AUG':
            ORF+=[rest_of_ORF(dna[i*3:])]
            i=i+(len(ORF[n])/3)+1
            n=n+1
        else:
            i=i+1
    return ORF

def find_all_ORFs(dna):
    ALLORF=[]
    for i in range(0,3):
        ALLORF+=find_all_ORFs_oneframe(dna[i:])
    return ALLORF

    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """


def find_all_ORFs_both_strands(dna):
    answer=find_all_ORFs(dna)+find_all_ORFs(get_reverse_complement(dna))
    # answer[0]=find_all_ORFs(dna)
    # answer[1]=find_all_ORFs(get_reverse_complement(dna))
    return answer
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """


def longest_ORF(dna):
    listofORFs=find_all_ORFs_both_strands(dna)
    maxindex=0
    for i in range(len(listofORFs)):
        if len(listofORFs[i])>len(listofORFs[maxindex]):
            maxindex=i
    return listofORFs[maxindex]


    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    trials=[]
    for i in range(num_trials):
        trials+=[longest_ORF(shuffle_string(dna))]
    maxindex=0
    for i in range(len(trials)):
        if len(trials[i])>len(trials[maxindex]):
            maxindex=i
    return len(trials[maxindex])


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    protein=''
    for i in range(len(dna)/3):
        protein+=str(aa_table[dna[i*3:i*3+3]])
    return protein


def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna
        
        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    threshold = longest_ORF_noncoding(dna, 1500)
    print threshold
    allFrames=find_all_ORFs_both_strands(dna)
    proteins=[]
    for i in range(len(allFrames)):
        if len (allFrames[i])>threshold:
            proteins+=[coding_strand_to_AA(allFrames[i])]
    print coding_strand_to_AA(allFrames[0])
    return proteins


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    dna=load_seq("./data/X73525.fa")
    print gene_finder(dna)