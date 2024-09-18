#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sat_interface

def tt2():
    clauses = ["~A C","~B ~C","C B","~C B ~A","~B C","A C"]
    kb = sat_interface.KB(clauses)
    a = kb.test_literal("A")
    b = kb.test_literal("B")
    c = kb.test_literal("C")
    return (a, b, c)

def tt3():
    clauses = ["~A ~C","C A","~C B","B ~A ~C","~B A","~B C"]
    kb = sat_interface.KB(clauses)
    a = kb.test_literal("A")
    b = kb.test_literal("B")
    c = kb.test_literal("C")
    return (a, b, c)

import sat_interface

def salt():
    clauses = ["~A SB","~SB A", "~B SB","~SB B","~C ~SC", "SC C","A B C","~A ~B ~C","~SB ~SC","~SA ~SC","~SA ~SB"]
    kb = sat_interface.KB(clauses)
    
    # Infer truth values
    a = kb.test_literal("A")
    b = kb.test_literal("B")
    c = kb.test_literal("C")
    sa = kb.test_literal("SA")
    sb = kb.test_literal("SB")
    sc = kb.test_literal("SC")

    return {"Caterpillar": a, "Bill the Lizard": b, "Cheshire Cat": c, "Caterpillar Stole": sa, "Bill the Lizard Stole": sb, "Cheshire Cat Stole": sc}

def golf():
    clauses = ["~FT MH", "~FH ~MH", "~MT MD", "~MH ~MD", "~LT MT", "~LH ~MT", "~FT ~FD","~FT ~FH","~MT ~MD", "~MT ~MH",
    "~LT ~LH", "~LT LD", "~FD ~FH", "~MD ~MH","~LD ~LH", "~FT ~MT", "~MT ~LT","~FT ~LT","~FD ~MD","~MD ~LD","~FD ~LD",
    "~FH ~MH","~MH ~LH", "~FH ~LH", "FT MT LT","FH MH LH","FD MD LD"
    ]

    kb = sat_interface.KB(clauses)

    # Infer truth values
    ft = kb.test_literal("FT")
    fd = kb.test_literal("FD")
    fh = kb.test_literal("FH")
    mt = kb.test_literal("MT")
    md = kb.test_literal("MD")
    mh = kb.test_literal("MH")
    lt = kb.test_literal("LT")
    ld = kb.test_literal("LD")
    lh = kb.test_literal("LH")
    

    return {
        "Front Tom": ft,
        "Front Dick":fd,
        "Front Harry":fh,
        "Middle Tom": mt,
        "Middle Dick": md,
        "Middle Harry": mh,
        "Last Tom": lt,
        "Last Dick": ld,
        "Last Harry": lh
    }


print("Liars and Truth-tellers II:", tt2())
print("Liars and Truth-tellers III:", tt3())
print("Robbery and a Salt:", salt())
print("An honest name:", golf())


# In[ ]:




