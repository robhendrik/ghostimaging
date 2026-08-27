# Who Needs a Double Slit Anyway?

**The double-slit experiment is the most famous demonstration in quantum physics. What happens when we remove the slits and add entanglement instead?**

---

<!--
ARC (four beats):
1. Everyone knows the two-slit experiment. Now: the photon making the fringes never went
   through any slit. And the familiar which-path rule still holds — nonlocally.
2. The Klyshko picture: the ghost unfolds into classical optics.
3. First reversal: you don't need entanglement. Classical correlations, then computation,
   reproduce the ghost.
4. Second reversal: but the ghost image was never the quantum test. The quantum–classical
   border depends on what you demand of the experiment. End on the open question.

MEDIUM OPTIMISATION NOTES:
- Sections ~300–500 words each. Total target: ~2400 words.
- Every section head works as a standalone question or provocation.
- Pull quotes designed as shareable standalone lines. Place at section transitions.
- Figures break scroll momentum — place after the reader has a reason to care.
- First 3 sentences must hook; Medium truncates the preview there.
- No equations. No jargon without immediate payoff.
-->

---
Every popular account of quantum mechanics reaches the same climax. Send photons one at a time toward a pair of slits. Each photon arrives as a single dot on a screen. But after thousands of them, an interference pattern builds up — bright and dark bands that should only appear if each photon passed through both slits simultaneously.

Now imagine removing the slits from the path of the photon that makes the pattern.

---
## The photon that was never there
In 1995, physicists performed a version of this experiment that seemed to break the story. Entangled photon pairs produced images in a detector whose photons had never seen the object [1]. Then researchers pushed the idea further. They replaced the object with perhaps the most famous object in quantum physics: a double slit [4].

Neither detector alone showed any pattern.

But when the researchers kept only those detections on the imaging side that coincided with a click behind the slits, an interference pattern emerged. Built entirely from photons that had never been anywhere near the double slit [4,5].

The fringes were real. The photon that made them was never there.

> **The photon that creates the interference pattern never passed through the slits. Its entangled partner did — and was detected by a device that recorded no image at all.**

<!-- FIGURE 1 -->
![ghost_imaging_far_field_schematic.png](ghost_imaging_far_field_schematic.png)
**Figure 1. The ghost double-slit experiment.** One photon passes through a double slit and reaches a detector with no spatial resolution (the bucket detector, which simply clicks). Its entangled partner travels to a scanning detector without ever encountering the slits. Neither detector shows fringes alone. The interference pattern appears only in the coincidences between them.

*Alt text: Schematic of a ghost interference experiment. A source produces entangled photon pairs. One path contains a double slit followed by a single-pixel bucket detector. The other path leads to a scanning detector. An arrow labelled "coincidences" connects the two detectors to a graph showing an interference pattern.*

---

## The oldest rule still applies

The reader who knows the two-slit experiment also knows its most famous caveat. Detect which slit the photon went through and the interference pattern disappears. Information about the path and the visibility of the fringes cannot coexist.

That rule carries over to the ghost — but now it operates across two photons.

If Alice places separate detectors behind each slit, so that her click reveals which path the photon took, Bob's ghost fringes vanish. His photon never went near the slits. His detector has not changed. But the which-path information exists somewhere in the joint record, and that is enough to kill the interference [4,5].

In the ordinary two-slit experiment, the photon and the fringes are the same object. In the ghost version, the knowledge is here and the fringes are there — and they still cannot coexist.

The ghost obeys the same quantum rule. It just enforces it nonlocally.

> **Which-path information kills interference — even when the path is here and the fringes are there.**

---

## How does the ghost know about the slits?

There is an elegant way to see why the ghost works, due to Klyshko [5,6].

Replace the crystal with a mirror and the bucket detector with a light source. Now trace the light: it leaves the "source," passes through the slits, bounces off the mirror, and reaches the scanning detector. You have unfolded the entangled two-photon experiment into an ordinary classical optical setup — and classical optics predicts exactly the pattern that the coincidences reveal.

The entangled photon pair behaves as if one photon were the time-reversed version of the other. The ghost fringes are the fringes you would see if light from the bucket detector could travel backward through the slits and forward to the camera.

This back-projection picture is not just a metaphor. It correctly predicts magnification, image location, resolution — every quantitative detail of the ghost experiment [5,6].

Which raises an uncomfortable question. If a classical optical picture explains the result so neatly, was entanglement really needed?

> **Unfold the entangled pair into a single classical light path and ordinary optics predicts every detail of the ghost.**

<!-- FIGURE 2 -->
![klyshko_ghost_imaging_schematic.png](klyshko_ghost_imaging_schematic.png)
**Figure 2. Top: the two-photon ghost experiment. Bottom: replace the bucket detector with a light source and the SPDC crystal with a mirror, and the two arms unfold into a single classical optical path from the source, through the double slit, to the camera. The ordinary optical system reproduces the geometry of the ghost experiment.**

Top: the two-photon ghost experiment. Bottom: replace the bucket detector with a light source and the SPDC crystal with a mirror, and the two arms unfold into a single classical optical path from the source, through the double slit, to the camera. The ordinary optical system reproduces the geometry of the ghost experiment.

*Alt text: Two vertically stacked diagrams. The upper diagram shows a UV laser pumping an SPDC crystal, producing two correlated photon paths: one passes through a double slit to a bucket detector while the other reaches a camera, with both detections sent to a coincidence correlator. The lower diagram shows the Klyshko equivalent: a light source replaces the bucket detector, a mirror replaces the SPDC crystal, and a single optical path runs backward through the double slit to the mirror and then forward to the camera.*

---

## Then the entanglement became optional

The answer arrived within a few years: no, entanglement is not required [2,3].

Shine a laser through a rotating ground-glass screen to create a random speckle pattern. Split the speckle into two copies with a beam splitter. Send one copy through the object to a bucket detector; record the other copy with a camera. Correlate the bucket signal with the recorded patterns and the ghost image appears — no entangled photons required.

Then researchers went further. If the illumination patterns are generated deliberately with a spatial light modulator, you already know what pattern you projected. There is nothing to record in the second arm. Replace it with a computer [7,8].

The apparatus is now stripped to its minimum: a projector, an object, a single-pixel detector and a laptop. The ghost image survives. The entanglement is gone. One entire optical arm is gone.

> **Remove the entanglement. Remove the second beam. Replace the camera with a calculation. The ghost image remains.**

<!-- FIGURE 3 -->
![ghost_imaging_three_stages.png](ghost_imaging_three_stages.png)
**Figure 3. Making the ghost classical. Three stages of ghost imaging. Left: entangled photon pairs and two detectors. Centre: classically correlated speckle beams and two detectors. Right: computational ghost imaging — a projector, one bucket detector, and a computer. The image survives as the quantum components are stripped away.**

*Alt-text: Three-panel diagram showing progressive simplification. Panel one uses entangled photon pairs with two detectors. Panel two replaces entanglement with a beam splitter creating classical speckle copies. Panel three removes the second beam entirely: structured illumination, a bucket detector, and a computer. All three panels produce the same reconstructed image.*

---

## But where did the quantum go?

So ghost imaging works without entanglement. Case closed?

Not quite.

The original experiment unquestionably used an entangled quantum state. Later experiments unquestionably produced ghost images with light that can be described classically. And computational ghost imaging showed that even a second physical beam is unnecessary.

What disappeared was not correlation. What changed was what kind of correlation was doing the work.

That distinction has kept the quantum-optics community busy for decades. Depending on what one asks — whether an image can be formed, how strong the correlations are, how sharply complementary quantities can be correlated, or how much information can be extracted — the line between a "quantum" and a "classical" ghost can appear in a different place.

D'Angelo and colleagues, for example, did not identify entanglement merely because they could produce both ghost images and ghost interference. They measured how sharply position and momentum were correlated simultaneously and showed that their photon pairs crossed a classical EPR-type bound [4].

Other work went in almost the opposite direction, showing just how much of ghost imaging can be understood using classical coherence and correlation theory [2,3,5,8].

The ghost image survived the transition from quantum to classical. What changed was the physics hiding inside the correlations.

---

## So was the ghost ever quantum?

Yes — and no.

The photons in the original experiments were quantum. Their entanglement was real. And suitably designed experiments can use ghost imaging and ghost interference to reveal correlations that cannot be explained by a corresponding classical model [4].

But the ghost image itself is not such a test.

That is the surprise the field discovered after the first experiments. An effect that looked almost like a demonstration of entanglement turned out to belong to a much larger family of correlation-based imaging techniques, extending from entangled photons to thermal speckle and ultimately to patterns generated inside a computer — where recent work treats the whole process as adaptive information acquisition, each illumination pattern asking the object a question, each detector reading narrowing what the object could be [9].

Thirty years after the first ghost image, the question has not disappeared. It has become harder to formulate.

Where exactly does classical imaging end and quantum imaging begin?

The answer depends on what we demand of the experiment.

And perhaps that is the real lesson of the ghost.

> **The border between classical and quantum physics is much easier to draw in a textbook than in the laboratory.**

---

## References

[1] T. B. Pittman, Y. H. Shih, D. V. Strekalov, and A. V. Sergienko, "Optical imaging by means of two-photon quantum entanglement," *Physical Review A* **52**, R3429 (1995).

[2] R. S. Bennink, S. J. Bentley, and R. W. Boyd, "'Two-photon' coincidence imaging with a classical source," *Physical Review Letters* **89**, 113601 (2002).

[3] A. Gatti, E. Brambilla, M. Bache, and L. A. Lugiato, "Ghost imaging with thermal light: comparing entanglement and classical correlation," *Physical Review Letters* **93**, 093602 (2004).

[4] M. D'Angelo, Y.-H. Kim, S. P. Kulik, and Y. Shih, "Identifying entanglement using quantum 'ghost' interference and imaging," *Physical Review Letters* **92**, 233601 (2004).

[5] M. J. Padgett and R. W. Boyd, "An introduction to ghost imaging: quantum and classical," *Philosophical Transactions of the Royal Society A* **375**, 20160233 (2017).

[6] T. B. Pittman, D. V. Strekalov, D. N. Klyshko, M. H. Rubin, A. V. Sergienko, and Y. H. Shih, "Two-photon geometric optics," *Physical Review A* **53**, 2804 (1996).

[7] J. H. Shapiro, "Computational ghost imaging," *Physical Review A* **78**, 061802(R) (2008).

[8] B. I. Erkmen and J. H. Shapiro, "Ghost imaging: from quantum to classical to computational," *Advances in Optics and Photonics* **2**, 405–450 (2010).

[9] J. Sun, C. Hu, Z. Bo, Z. Liu, M. Chen, L. Du, W. Liu, and S. Han, "Adaptive information-maximization encoding for ghost imaging," arXiv:2601.15604v2 (2026).
