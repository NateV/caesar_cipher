"""
Module contains a few functions for encrypting and decrypting text with a Caesar
Cipher
"""
from math import sqrt

def encrypt_one(k,c):
    """
    Input: a key, some integer > 0 and a single character
    Output: The character shifted by k spaces around the alphabet.  
    """
    if c==" ": return c
    base = ord("a")
    n = 26
    c = c.lower()
    return chr(  ((ord(c) - base + k) % n) + base) 


def encrypt(k, message):
    """
    Input: message, a message to encrypt, and k, the number of letters to shift
    the message by
    Output: the ciphertext of the message, where each letter is shifted by the
    key k letters.
    """
    return ''.join([encrypt_one(k,c) for c in message])


 
def decrypt(k, ciphertext):
    """
    Input: A ciphertext of a Caesar cipher-encrypted message and k, the number
    of letters the message was shifted by
    Output: the original message
    """
    modified_k = 26 - k
    return "".join([encrypt_one(modified_k,c) for c in ciphertext])



def english_letter_distribution():
    """
    Output: A dictionary of the probability distribution of letters in English
    text. I'll hard code it at first, but I'd like to figure it out from sample
    texts. 
    """
    return {
    'e': .12702,
    't': .09056,
    'a': .08167,
    'o': .07507,
    'i': .06966,
    'n': .06749,
    's': .06327,
    'h': .06094,
    'r': .05987,
    'd': .04253,
    'l': .04025,
    'c': .02782,
    'u': .02758,
    'm': .02406,
    'w': .02361,
    'f': .02228,
    'g': .02015,
    'y': .01974,
    'p': .01929,
    'b': .01492,
    'v': .00978,
    'k': .00772,
    'j': .00153,
    'x': .00150,
    'q': .00095,
    'z': .00074}







def generate_distribution(text):
    """
    Calculate and normalize the distribution of letters in a text
    """
    dist = dict()
    #get counts of letters
    for c in text:
        if c==" ": pass
        if c in dist.keys():
            dist[c] += 1
        else:
            dist[c] = 1
    # normalize
    total = len(text)
    for k,v in dist.items():
        dist[k] = dist[k]/total
    return dist

def compare_distributions(dist1, dist2):
    """
    Compare how similar two normalized distributions are.
    """
    domain = set(dist1.keys()) | set(dist2.keys()) # all the possible letters in 
                                                     # our two distributions

    distance = 0
    for d in domain:
        d1 = dist1[d] if d in dist1 else 0
        d2 = dist2[d] if d in dist2 else 0
        distance += (d1 - d2)**2
    return sqrt(distance)

def attack(ciphertext):
    """
    Input: The ciphertext of a Caesar cipher-encrypted message
    The function uses a statistical method to attack the ciphertext and predict
    what the original message was. 
    Output: The original message on which the ciphertext was based.
    """
    print("ATTACKING: {}".format(ciphertext))
    c_dist = generate_distribution(ciphertext)
    print("dist for the ciphertext: {}".format(c_dist))
    compare_dists = dict() # an empty dict for the differences between possible
                            # k values and the english distribution 

    #what value for k gives the closest match to the real English distribution? 

    for possible_k in range(0,26):
        #for this k, shift the ciphertext back by k
        modified_ct = decrypt(possible_k, ciphertext)
        #compare the letter distribution of this k to the English distribution
        test_distribution = generate_distribution(modified_ct)
        diff = compare_distributions(test_distribution,
                                     english_letter_distribution())

        #and save the resulting value to a dict
        compare_dists[possible_k] = diff

    print("Distances:")
    for k, v in compare_dists.items():
        print("k: {}, d: {}".format(k,v))


    # the right k value should be the possible_k where its distribution was
    # smallest
    correct_k = min(compare_dists, key=compare_dists.get)
    return (correct_k, decrypt(correct_k, ciphertext))






