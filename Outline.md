# Who Needs a Double Slit Anyway?

**The double-slit experiment is the most famous demonstration in quantum physics. What happens when the photon making the fringes never passes through either slit?**

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





Every popular account of quantum mechanics eventually reaches the same climax. Send photons one at a time toward a pair of slits. Each photon arrives as a single dot on a screen. But after thousands of them, an interference pattern builds up — bright and dark bands that seem to require each photon to have somehow explored both paths. 

Now imagine removing the slits from the path of the photon that makes the pattern.

---
## The photon that was never there
In 1995, physicists demonstrated something that looked almost impossible. Entangled photon pairs could produce an image in a detector whose photons had never interacted with the object at all [1]. 

The effect was named ‘ghost imaging’, based on the strange division of labour. The light that touches the object is detected without forming an image, while the detector that does form the image receives light that never touched the object. The image exists only in the correlations between the two detection records.

That same year, a separate team pushed the idea into more familiar territory: they replaced the object with a double slit [2].

One photon passed through the slits and was collected by a detector with no spatial resolution — a fixed detector that merely registered whether a photon arrived without making an image. Its entangled partner travelled along a separate path to a position-sensitive detector.

Neither detector showed an interference pattern on its own.

But when the two detection records were compared, and only coincident events were kept, fringes appeared.

The photon whose position built up the interference pattern had never gone through either slit.

> **The photon that creates the interference pattern never passed through the slits. Its entangled partner did — and was detected by a device that recorded no image at all.**

![ghost_imaging_far_field_schematic.png](ghost_imaging_far_field_schematic.png)
**Figure 1. The ghost double-slit experiment. One photon passes through a double slit and reaches a fixed detector with no spatial resolution. Its entangled partner travels directly to a position-sensitive detector. Neither detector reveals an interference pattern by itself. The fringes appear only when the two detection records are correlated.**



*Alt text: Schematic of a ghost interference experiment. A source produces entangled photon pairs. One path contains a double slit followed by a single-pixel fixed detector. The other path leads to a scanning detector. An arrow labelled "coincidences" connects the two detectors to a graph showing an interference pattern.*

---

## The oldest rule still applies

Anyone who knows the double-slit experiment also knows its most famous rule: find out which slit the photon went through, and the interference disappears.

The ghost version obeys the same rule — but now across two photons.

If the detector behind the slits is changed so that its click reveals which slit the first photon passed through, the fringes in the coincidence pattern disappear [3]. Nothing has changed in the other arm. The photon recorded there still never encounters the slits.

What changed is the information available in the joint measurement.

In the ordinary double-slit experiment, the path information and the fringes belong to the same photon. In the ghost experiment, the path information is recorded on one side and the interference pattern appears on the other — yet the same trade-off survives.

The old quantum rule is still valid, it is just enforced nonlocally.

> **Which-path information kills interference — even when the path is here and the fringes are there.**

---

## How does the ghost know about the slits?

There is an elegant way to see why the experiment works, due to Klyshko [4,5].

Imagine running one arm of the experiment backwards. Replace the fixed detector with a light source and the nonlinear crystal with a mirror. Light now travels from the detector side, back through the double slit, reflects from the mirror, and continues along the second arm to the camera.

The strange two-photon experiment has unfolded into an ordinary optical system.

And that ordinary system predicts the same image geometry and the same interference pattern as the coincidence measurements in the ghost experiment [4,5].

The Klyshko picture does not mean that a photon literally travels backwards in time. It is a calculational picture — but a remarkably useful one. Magnification, image position and diffraction all become ordinary optics again.

Which makes the next question difficult to avoid.

If a classical optical picture predicts the ghost so well, how much of the effect is really quantum?

> **Unfold the entangled pair into a single classical light path and ordinary optics predicts every detail of the ghost.**

<!-- FIGURE 2 -->
![klyshko_ghost_imaging_schematic.png](klyshko_ghost_imaging_schematic.png)
**Figure 2. The Klyshko picture. Top: the two-photon ghost experiment. Bottom: replace the fixed detector with a light source and the SPDC crystal with a mirror. The two arms then unfold into a single classical optical path through the double slit to the camera.**

*Alt text: Top: the two-photon ghost experiment. Bottom: replace the fixed detector with a light source and the SPDC crystal with a mirror, and the two arms unfold into a single classical optical path from the source, through the double slit, to the camera. The ordinary optical system reproduces the geometry of the ghost experiment.*

---

## Then the entanglement became optional

It turns out that the ghost image itself does not require entanglement.

Take a laser and pass it through a rotating ground-glass screen. The result is a constantly changing speckle pattern. Split that pattern into two copies with a beam splitter. Send one copy through the object to a fixed detector, and record the other with a camera.

Neither measurement is useful on its own.

But correlate the signal with the recorded speckle patterns, and the image appears [6,7].

No entangled photons are involved.

Classical correlations can reproduce both ghost images and ghost interference. Then researchers removed even more of the apparatus. If the illumination patterns are generated deliberately with a spatial light modulator, the second beam no longer has to be measured at all [8,9].

Now the setup has collapsed to its essentials: a structured light source, the object, a single-pixel detector and a computer.

The ghost image survives.

> **Remove the entanglement. Remove the second beam. Replace the camera with a calculation. The ghost image remains.**

<!-- FIGURE 3 -->
![ghost_imaging_three_stages.png](ghost_imaging_three_stages.png)
**Figure 3. Making the ghost classical. Three stages of ghost imaging. Left: entangled photon pairs are measured in two arms. Centre: a beam splitter creates two classically correlated copies of a changing speckle pattern. Right: the second arm disappears entirely — known illumination patterns are projected onto the object, measured with a fixed, non imaging detector and reconstructed by a computer.**

*Alt text: Three-panel diagram showing the progression from quantum to computational ghost imaging. In the left panel, an SPDC source produces entangled photon pairs; one photon passes through the object to a fixed, non-imaging detector while the other is detected spatially. In the centre panel, a beam splitter divides a random speckle field into two classically correlated beams, again using a fixed detector and a spatial detector. In the right panel, a projector sends known structured illumination patterns onto the object, a single fixed detector measures the transmitted light, and a computer reconstructs the image without a second optical arm.*

---

## But where did the quantum go?
So ghost imaging works without entanglement. Case closed?

Not quite.

The original experiments unquestionably used entangled photons. Later experiments unquestionably produced ghost images with light that can be described classically. And computational ghost imaging showed that even the second physical beam can disappear.

What this tells us is that the ghost image itself is not the quantum test.

The distinction appears when we ask more of the experiment. D'Angelo and colleagues, for example, did not identify entanglement simply because they could produce a ghost image or an interference pattern. They used the same photon pairs to measure correlations in both position and momentum, and showed that these correlations were simultaneously stronger than a corresponding classical source could provide [10].

That is a much more demanding statement.

A classical system can reproduce a ghost image. It can reproduce ghost interference. But the quantum state can carry exceptionally sharp correlations in two complementary descriptions at once — the spatial analogue of the EPR correlations that made entanglement famous in the first place [4,10].

So was the ghost ever quantum?

The photons could be. The correlations could be. But seeing a ghost image is not enough to prove it.

And that distinction matters even more today. Ghost imaging has evolved from entangled photon pairs, through thermal speckle, to computational systems in which known illumination patterns interrogate an object one measurement at a time [8,9]. Recent work goes further still, treating the problem explicitly as information acquisition: choose the next pattern so that the detector result tells you as much as possible about what remains unknown [11].

The original mystery has therefore changed.

The question is no longer simply How can a camera image something its photons never touched?

It is: *What kinds of correlations, and what kinds of information, can an imaging system exploit?*

As a student, the boundary between classical and quantum physics looked much cleaner in the textbook. Ghost imaging is a good reminder of why.

> **The ghost image is not the quantum test. The physics lies in what the correlations allow us to learn.
---

## References

[1] T. B. Pittman, Y. H. Shih, D. V. Strekalov, and A. V. Sergienko, "Optical imaging by means of two-photon quantum entanglement," *Physical Review A* **52**, R3429 (1995).

[2] D. V. Strekalov, A. V. Sergienko, D. N. Klyshko, and Y. H. Shih, "Observation of two-photon 'ghost' interference and diffraction," *Physical Review Letters* **74**, 3600 (1995).

[3] P. Chingangbam and T. Qureshi, "Ghost interference and quantum erasure," *Progress of Theoretical Physics* **127**, 383–392 (2012).

[4] M. J. Padgett and R. W. Boyd, "An introduction to ghost imaging: quantum and classical," *Philosophical Transactions of the Royal Society A* **375**, 20160233 (2017).

[5] T. B. Pittman, D. V. Strekalov, D. N. Klyshko, M. H. Rubin, A. V. Sergienko, and Y. H. Shih, "Two-photon geometric optics," *Physical Review A* **53**, 2804 (1996).

[6] R. S. Bennink, S. J. Bentley, and R. W. Boyd, "'Two-photon' coincidence imaging with a classical source," *Physical Review Letters* **89**, 113601 (2002).

[7] A. Gatti, E. Brambilla, M. Bache, and L. A. Lugiato, "Ghost imaging with thermal light: comparing entanglement and classical correlation," *Physical Review Letters* **93**, 093602 (2004).

[8] J. H. Shapiro, "Computational ghost imaging," *Physical Review A* **78**, 061802(R) (2008).

[9] B. I. Erkmen and J. H. Shapiro, "Ghost imaging: from quantum to classical to computational," *Advances in Optics and Photonics* **2**, 405–450 (2010).

[10] M. D'Angelo, Y.-H. Kim, S. P. Kulik, and Y. Shih, "Identifying entanglement using quantum 'ghost' interference and imaging," *Physical Review Letters* **92**, 233601 (2004).

[11] J. Sun, C. Hu, Z. Bo, Z. Liu, M. Chen, L. Du, W. Liu, and S. Han, "Adaptive information-maximization encoding for ghost imaging," arXiv:2601.15604v2 (2026).
