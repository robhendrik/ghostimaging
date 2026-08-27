# How Do You Photograph Something Your Camera Never Saw?

### *Ghost imaging began as a quantum mystery. Then it worked without entanglement. Now information theory is changing the question again.*

```{=html}
<!--
SCIENCE SPECTRUM / MEDIUM OUTLINE

Narrative arc:
Impossible image → quantum explanation → classical reversal → an even more surprising
classical capability → information lens → open quantum/classical question.

Editorial goal:
Keep the first half visual and descriptive. Do not front-load equations or the technical
entanglement criteria. Each section should answer one question and create the next one.

Target: three figures, three pull quotes. The post should NOT force a final 'quantum reveal'.
Near-field and far-field reconstruction can both be reproduced classically in suitable schemes.
D'Angelo's genuinely quantum result concerns the simultaneous correlation widths / EPR
criterion, which is scientifically important but too technical to carry this Medium post.
The information section should therefore end with the modern question rather than a new claim.
-->
```
A camera works because light from an object reaches its detector. Block
that light, and there is nothing to photograph.

At least, that seems obvious.

In 1995, physicists demonstrated an experiment that appeared to break
this simple rule. One photon passed through an object but ended up at a
detector incapable of taking a picture. Its partner travelled to a
position-sensitive detector---but never encountered the object at all.

Neither detector could see the image.

**Yet when the two sets of measurements were compared, the image
appeared.**

They called it 'ghost imaging'. And there seemed to be a natural
explanation for how the ghost performed its trick: the two photons were
quantum mechanically entangled \[1\].

That explanation did not last.

Researchers subsequently produced ghost images using correlations that
could be described classically. Eventually, one of the two optical arms
could even be replaced by a computer \[2--4\].

So, was there ever anything quantum about the ghost?

**Perhaps that is the wrong question.**

Because if we stop asking where the *image* travelled and ask where the
*information needed to reconstruct it* was hiding, ghost imaging starts
to look like something quite different.

```{=html}
<!-- FIGURE 1 HERE -->
```
*Figure 1. The camera that never saw the object. One photon encounters
the object but is recorded by a bucket detector with no spatial
resolution. Its correlated partner reaches a spatial detector without
ever encountering the object. Neither detector contains the image on its
own; the image appears in their correlations.*

**Alt text:** Diagram of a ghost-imaging experiment. A source produces
two correlated light paths. One path passes through an object to a
single-pixel bucket detector; the other goes directly to a spatial
detector. The two detector outputs are correlated to reconstruct an
image of the object.

> **Neither detector can see the image. Together, they can.**

## The Ghost Was Quantum

```{=html}
<!--
GOAL:
Give the reader the satisfying first explanation. Keep SPDC intuitive.
Introduce entanglement only as much as needed: photon pairs have strong spatial correlations.
End the section by making the explanation feel complete before overturning it.
-->
```
The original experiment used photon pairs produced by spontaneous
parametric down-conversion (SPDC). The two photons are strongly
correlated in their spatial properties. If one photon is detected at a
particular position, that tells us something about where its partner can
be found \[1,4\].

Now place an object in one path. We no longer record *where* that photon
arrives; the bucket detector tells us only whether light made it
through. In the other path we do record position, but that photon has
never seen the object.

Individually, both records are useless as an image. We keep the spatial
detections that coincide with detections behind the object and, after
repeating this many times, the object emerges \[4\].

It was tempting to attribute this strange image to entanglement. After
all, the source really was quantum and the image lived in correlations
between photons.

Then physicists made the same kind of ghost with classical light.

## Then the Quantum Disappeared

```{=html}
<!--
GOAL:
First major reversal. Explain pseudothermal GI descriptively, then computational GI.
The hardware should progressively disappear. This should be the most visually satisfying section.
Avoid implying that ALL quantum advantages in GI disappear—only that ghost-image formation
itself does not require entanglement.
-->
```
A laser scattered from a rotating diffuser produces a changing speckle
pattern. Split that pattern into two copies. One copy illuminates the
object and ends at the bucket detector; the other is recorded by a
camera. Correlate the bucket signal with the changing reference patterns
and, again, the image appears \[2,3\].

No entangled photon pairs are required.

And once the reference patterns are deliberately generated rather than
random, something even stranger happens. We already know what pattern
was projected. So why build a second optical arm just to measure it?

We can calculate it.

Computational ghost imaging therefore reduces the experiment to
structured illumination, an object, a single-pixel detector and a
computer. The computer correlates each known illumination pattern with
the bucket-detector signal and reconstructs the image \[2,3\].

The 'ghost' survives even after one of its optical arms has disappeared.

```{=html}
<!-- FIGURE 2 HERE -->
```
*Figure 2. Making the quantum disappear. Ghost imaging progressed from
entangled photon pairs, to classically correlated speckle patterns, to
computational ghost imaging in which the reference arm is replaced by
patterns already known to a computer. The image survives as physical
components disappear.*

**Alt text:** Three-stage diagram showing the evolution of ghost
imaging. The first setup uses entangled photon pairs and two detectors,
the second uses classically correlated speckle beams, and the third uses
computer-controlled illumination with only a bucket detector. All three
reconstruct an image.

> **Remove the entanglement. Remove the second beam. The ghost
> remains.**

So, if a classical system can produce the image, what was quantum about
the original experiment?

## And Then It Gets Stranger

```{=html}
<!--
GOAL:
Give the reader a second surprise without forcing a quantum victory.
Near-field and far-field measurements smell quantum because they involve complementary
spatial variables, but the ability to reconstruct both kinds of information is not by itself
a uniquely quantum capability.

Do not derive the full D'Angelo EPR inequalities here. Mention only that genuinely quantum
tests exist and depend on how sharply the correlations can be localized simultaneously.
-->
```

There is one more twist.

The original entangled-photon experiments were not limited to making a ghost image in the
image plane. By changing the optical configuration, one could also look in the far field and
recover the corresponding diffraction or interference structure [4,9].

At first sight, this feels like the place where the quantum nature must finally reappear. In the
near field we ask about position. In the far field we ask about transverse momentum. These are
complementary spatial variables.

But even that intuition has to be handled carefully.

Classical correlated light can reproduce near-field and far-field ghost-imaging behaviour as
well. Computational ghost imaging pushes the point even further: once the illumination patterns
are known, the same recorded data can be processed in different spatial representations. The
ability to reconstruct an image here, or a diffraction pattern there, is therefore not by itself a
proof of entanglement [2–4].

This is where the historical quantum-versus-classical debate became more subtle. D'Angelo
*et al.* used ghost imaging and ghost interference not simply to show that both patterns exist,
but to measure how *narrow* the position and momentum correlations are simultaneously. That
quantitative EPR test can distinguish entangled photon pairs from classical correlations [9].

For this post, however, we do not need to follow that technical route. The more interesting
lesson is simpler:

> **The further we push ghost imaging, the harder it becomes to point at the image itself and say: that part is quantum.**

<!-- FIGURE 3 HERE -->

*Figure 3. Near field or far field? Ghost-imaging systems can be configured to reconstruct
position-space information or diffraction/Fourier-space information. The important caveat is
that the existence of both reconstructions is not, by itself, a uniquely quantum signature;
classical correlated and computational schemes can reproduce these imaging functions too.*

**Alt text:** Two-panel schematic of ghost imaging. One panel shows a near-field reconstruction
of an object, the other a far-field diffraction pattern. A central note states that both kinds of
reconstruction can also be achieved with appropriate classical correlated or computational
ghost-imaging schemes.

## Where Was the Information?

```{=html}
<!--
GOAL:
Pivot from the historical quantum/classical debate to information.
This is the conceptual payoff, not another technical tutorial.
Use computational GI to make encoding/decoding intuitive before introducing MI/Fisher information.
-->
```
There is another way of looking at the whole experiment.

Suppose the object is simply a row of pixels with unknown transmissions,

`t = 1 0 1 1 0 0 1 0 ...`

Our task is no longer mysterious: we want to learn this unknown string.

In computational ghost imaging, each illumination pattern probes a
particular combination of those pixels. The bucket detector returns only
one number. We repeat the experiment with different patterns and combine
the answers until we can estimate the object.

In fact, recent work describes ghost imaging explicitly as an
**encoding-decoding** problem. The illumination field encodes the object
into the detected signal; reconstruction decodes the information again
\[7\].

This triggers the question: if every measurement gives us some
information about the unknown object, can we choose the next
illumination pattern so that it gives us as much *new* information as
possible?

That is exactly the direction taken in recent information-theoretic
work. Sun *et al.* use the measurements already obtained to update a
probability distribution for the unknown image, then choose subsequent
illumination patterns by maximizing expected information gain. Mutual
information and Fisher-information-related criteria become tools for
deciding what to measure next \[7\].

So, the strange camera from the beginning has turned into something
rather different: a machine for asking an unknown object a sequence of
questions.

## How Much Can We Learn?

```{=html}
<!--
GOAL:
Bring in the July 2026 metrology paper as the contemporary endpoint.
Keep equations minimal. The key conceptual shift is image → unknown parameters → precision bounds.
Do NOT claim this paper proves a quantum advantage for the near/far-field choice discussed above.
-->
```
We can push this one step further.

Instead of judging an imaging system by whether the final picture looks
sharp, we can describe the object by a set of unknown transmission
coefficients,

τ₁, τ₂, ..., τₙ,

and ask how precisely any experiment could estimate them.

Brambila and Sorelli recently applied exactly this quantum-metrology
perspective to ghost imaging and related quantum-imaging schemes. They
formulate imaging as a multiparameter estimation problem and use Fisher
information and quantum Fisher information to calculate precision limits
for recovering the object's transmission parameters \[8\].

This is a subtle change of perspective. We are no longer asking only,
*Can we reconstruct an image?* We are asking, *How much information
about the object is available in this physical state, which measurement
extracts it, and how accurately can we possibly know the parameters we
care about?*

And there is an important complication. In quantum multiparameter
estimation, one measurement need not be optimal for all parameters
simultaneously \[8\]. Measurement choice itself becomes part of the
information problem.

That does not turn ghost imaging into a random-access code, nor does it
mean that position and momentum are two independent messages. But it
places the old ghost-imaging puzzle in a much broader question---one
that quantum information theory knows very well.

## The Ghost in the Information

```{=html}
<!--
GOAL:
Return explicitly to the opening image. Do not force a 'quantum wins after all' ending.
The ending should reflect where the literature actually is: image formation can be classical,
quantum correlations remain physically distinct, and current work increasingly asks about
information acquisition, estimation precision and optimal encoding.

Leave the reader with an open question.
-->
```

We started with a camera receiving light that never touched the object. At first, entanglement
seemed to explain the trick. Then classical light reproduced it, and computational ghost imaging
removed an entire optical arm.

Even some features that *feel* very quantum turn out not to settle the argument. Near-field and
far-field information can both be reconstructed in classical ghost-imaging schemes. The image
itself is therefore a poor place to draw a sharp border between the classical and quantum worlds
[2–4].

That does not mean that entanglement is irrelevant. Experiments such as D'Angelo's show that
quantum light can possess position and momentum correlations whose simultaneous sharpness
violates a classical EPR-type bound [9]. But that is a statement about the *strength and structure
of the correlations*, not about whether a ghost image can be made at all.

And perhaps this is why the modern information-theoretic view is useful.

Recent work increasingly describes ghost imaging as an encoding-and-decoding problem. The
object is probed by structured light, measurements reduce our uncertainty about it, and the
question becomes how much useful information each measurement acquires and how efficiently
we can extract it [5–8].

So, possibly the most interesting question is no longer:

**Is ghost imaging quantum or classical?**

It is:

**Given an object, a physical source and a measurement strategy, how much information can we
recover—and under which constraints does using genuinely quantum correlations actually help?**

That question is still being worked on. Which is perhaps a more satisfying ending than finding
the ghost hiding in one particular piece of optical hardware.

The camera never saw the object. The harder question turned out to be deciding what, exactly,
made the experiment quantum.


------------------------------------------------------------------------

## References

[1] T. B. Pittman, Y. H. Shih, D. V. Strekalov, and A. V. Sergienko,
"Optical imaging by means of two-photon quantum entanglement," *Physical
Review A* **52**, R3429–R3432 (1995).

[2] J. H. Shapiro, "Computational ghost imaging," *Physical Review A*
**78**, 061802(R) (2008).

[3] B. I. Erkmen and J. H. Shapiro, "Ghost imaging: from quantum to
classical to computational," *Advances in Optics and Photonics* **2**,
405–450 (2010). https://doi.org/10.1364/AOP.2.000405

[4] M. J. Padgett and R. W. Boyd, "An introduction to ghost imaging:
quantum and classical," *Philosophical Transactions of the Royal Society
A* **375**, 20160233 (2017). https://doi.org/10.1098/rsta.2016.0233

[5] S. Ragy and G. Adesso, "Nature of light correlations in ghost
imaging," *Scientific Reports* **2**, 651 (2012).
https://doi.org/10.1038/srep00651

[6] J. Li, B. Luo, D. Yang, L. Yin, G. Wu, and H. Guo, "Negative
exponential behavior of image mutual information for pseudo-thermal
light ghost imaging: observation, modeling, and verification," *Science
Bulletin* **62**, 717–723 (2017).
https://doi.org/10.1016/j.scib.2017.04.008

[7] J. Sun, C. Hu, Z. Bo, Z. Liu, M. Chen, L. Du, W. Liu, and S. Han,
"Adaptive information-maximization encoding for ghost imaging—A
general Bayesian framework under experimental physical constraints,"
arXiv:2601.15604v2 (2026).

[8] E. Brambila and G. Sorelli, "Metrology of quantum imaging
schemes," arXiv:2607.22373v1 (2026).

[9] M. D'Angelo, Y.-H. Kim, S. P. Kulik, and Y. Shih,
"Identifying entanglement using quantum 'ghost' interference and imaging,"
*Physical Review Letters* **92**, 233601 (2004).
https://doi.org/10.1103/PhysRevLett.92.233601
