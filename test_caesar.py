"""
Module tests the caesar.py module.
"""
from caesar import encrypt, encrypt_one, decrypt, compare_distributions, generate_distribution, attack


def test_pytest():
    assert 4==4

def test_encrpyt():
    #regl'r cipher
    k = 3
    m = "Hello"
    assert encrypt(k, m) == "khoor"
    
    #What if k is big?
    k = 14
    m = "Hello"
    assert encrypt(k,m) == "vszzc"
    
    #handles spaces by leaving spaces alone.
    k=3
    m = "Hello hello"
    assert encrypt(k,m) == "khoor khoor"

    #What about non ascii characters?


def test_encrypt_one():
    k=3
    c="H"
    assert encrypt_one(k,c) == "k"

    k=40
    c="H"
    assert encrypt_one(k,c) == "v"



def test_decrpyt():
    k = 3
    c = "khoor"
    assert decrypt(k,c)=="hello"

    k=3
    c="khoor khoor"
    assert decrypt(k,c)=="hello hello"

    k = 40
    c = "V"
    assert decrypt(k,c)=="h"

def test_generate_distribution():
    text = "hi"
    assert generate_distribution(text) == {'h': 0.5, 'i':0.5}

    text = "hih"
    assert generate_distribution(text) == {'h': 2/3, 'i':1/3}


def test_compare_distributions():
    d1 = {'a':1,'b':2}
    d2 = {'a':1,'b':2}
    assert compare_distributions(d1,d2)==0

    d1 = {'x':0,'y': 15}
    d2 = {'x':0,'y':0}
    assert compare_distributions(d1,d2)==15

def test_attack():
    ciphertext = "khoor khoor"
#   Interestingly, but it makes sense, a short message is harder to decrypt
#   because its too short to have a distribution that matches English. 
#   So this fails:
#    assert attack(ciphertext)=="hello hello" 

#   But this succeeds!
    ciphertext = """
zhovk klvwrub lv d sxccoh wr prvw hqjolvkphqr dffruglqjob l kdyh pdgh dq udwwhpsw wr vlpsolib lw vxiilflhqwob iru wkh ylvlwru wr judvs lwv rxwolqhve uzlwkrxw d nqrzohgjh ri wkh klvwrub ri d frxqwub lq zklfk rqh wudyhov pruh wkdq ukdoi lwv lqwhuhvw lv orvweul kdyh wr uhwxuq pb zduphvw wkdqnv wr nlqg iulhqgv zkr kdyh khoshg ph zlwkulqirupdwlrqc qrwdeob wkh uhye me ilvkhuc eegec ri fhiqc ve dvdskr pue me heujuliilwkc ri eubq glqdvc edqjrur wkh uhye he hydqvc ri oodqvdgzuqr pue fe keumrqhvc ri wkh sxeolf oleudubc zhovksrror pue de irxonhvdurehuwvc ri ghqeljkr pueuge ue gdqlhoc ri irxu furvvhvcxylz fkzlorjr dqg pue ue zlooldpvc ri fhobqrjcuqhzwrzqe l dp dovr pxfk lqghewhg wr pue ue me oorbg sulfhc ri uklzodvc iruunlqgob doorzlqj ph wr uhsurgxfh wkh sruwudlw ri fdwkhulqh ri ehudlq lq klvusrvvhvvlrqr dqg wr pue subvdmrqhvc ri eubqdwhjlgc srqwbsulggc iru vhqglqj ph duskrwrjudsk ri wkh sdlqwlqje exwc lqghhgc hyhubzkhuh lq zdohv l kdyh phw zlwkujhqhudo nlqgqhvv dqg krvslwdolwbr dqg li l kdyh idlohg wr lqwhuhvw uhdghuv lquwkh frxqwub dqg shrsoh wkh idxow lv doo plqhe lw lv d jorulrxv frxqwubc dqg lwvushrsoh gholjkwixoe"""
    assert attack(ciphertext)[0] == 3

#TODO:
#1. handle capital letters properly
