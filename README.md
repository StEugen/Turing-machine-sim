# Turing-machine-sim

Simulation of turing machine made for my algorithm classes in university


## Definitions

A deterministic Turing machine can be defined as a 7-tuple <br>

M = (Q, Σ, Γ, δ, b, q0, qf)<br>
<ul>
<li>Q is a finite, non-empty set of states</li>
<li>Γ is a finite, non-empty set of the tape alphabet</li>
<li>Σ is the set of input symbols with Σ ⊂ Γ</li>
<li>δ is a partially defined function, the transition function:<
δ : (Q \ {qf}) x Γ → Q x Γ x {L,N,R} </li>
<li>b ∈ &Gamma \ Σ is the blank symbol</li>
<li>q0 ∈ Q is the initial state</li>
<li>qf ∈ Q is the set of accepting or final states</li>
</ul>

## Stack
- Python

