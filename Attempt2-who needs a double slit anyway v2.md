# Who Needs a Double Slit Anyway?

**The double-slit experiment is the most famous demonstration in quantum physics. What happens when the photon making the fringes never passes through either slit?**

---

A photon makes an interference pattern. It never went near the slits.

That's not a trick question — it's a real experiment, and it still obeys the rules of the ordinary double-slit setup you already know. Just not in the way you'd expect.

---

## The photon that was never there

In 1995, physicists showed something that looked impossible. Entangled photon pairs could build an image on a detector whose own photons had never touched the object at all [1].

They called it ‘ghost imaging’, and the name fits. The light that touches the object gets detected without ever forming an image. The detector that *does* form the image receives light that never touched the object. Neither side holds the picture on its own — it only exists in the correlation between the two.

That same year, a separate group pushed the idea somewhere more familiar: they swapped the object for a double slit [2].

One photon passed through the slits and landed on a detector with no spatial resolution — just a click, nothing more. Its entangled partner travelled a separate path to a detector that could actually record position.

Neither detector shows a pattern on its own.

Compare the two records, keep only the coincident events, and fringes appear.

The photon that built up the pattern never went through either slit.

> **The photon that creates the interference pattern never passed through the slits. Its entangled partner did — and landed on a detector that recorded no image at all.**

![ghost_imaging_far_field_schematic.png](ghost_imaging_far_field_schematic.png)
**Figure 1. The ghost double-slit experiment. One photon passes through a double slit and reaches a fixed detector with no spatial resolution. Its entangled partner travels directly to a position-sensitive detector. Neither detector reveals an interference pattern by itself. The fringes only appear once the two detection records are correlated.**

*Alt text: Schematic of a ghost interference experiment. A source produces entangled photon pairs. One path contains a double slit followed by a single-pixel fixed detector. The other path leads to a scanning detector. An arrow labelled "coincidences" connects the two detectors to a graph showing an interference pattern.*

---

## The oldest rule still applies

Here's the part that should feel familiar: find out which slit a photon went through, and the interference disappears. Everyone who knows the double-slit experiment knows that rule.

The ghost version obeys it too — just split across two photons instead of one.

Change the detector behind the slits so its click reveals which slit the first photon used, and the fringes in the coincidence pattern vanish [3]. Nothing changes in the other arm. That photon still never comes near the slits.

So what changed? Only the information available once we compare the two records.

Which-path information kills interference even when the path is measured on one side of the lab and the fringes show up on the other. Same old rule. It's just enforced nonlocally now.

> **Which-path information kills interference — even when the path is here and the fringes are over there.**

---

## How does the ghost know about the slits?

There's a neat way to see why this works, and we owe it to Klyshko [4,5].

Run one arm of the experiment backwards, on paper. Replace the fixed detector with a light source. Replace the crystal with a mirror. Light now travels from the detector side, back through the slit, off the mirror, and along the second arm to the camera.

The strange two-photon experiment unfolds into an ordinary optical system — and that ordinary system predicts the same image geometry and the same fringes we actually measure in coincidence [4,5].

Note that this doesn't mean a photon literally travels backwards in time. It's a calculational trick. But a genuinely useful one — magnification, image position, diffraction, it all turns back into plain optics.

Which raises the obvious next question. If an ordinary optical picture predicts the ghost this well, how much of this was ever quantum?

> **Unfold the entangled pair into a single classical light path, and ordinary optics predicts every detail of the ghost.**

<!-- FIGURE 2 -->
![klyshko_ghost_imaging_schematic.png](klyshko_ghost_imaging_schematic.png)
**Figure 2. The Klyshko picture. Top: the two-photon ghost experiment. Bottom: replace the fixed detector with a light source and the SPDC crystal with a mirror. The two arms then unfold into a single classical optical path through the double slit to the camera.**

*Alt text: Top: the two-photon ghost experiment. Bottom: replace the fixed detector with a light source and the SPDC crystal with a mirror, and the two arms unfold into a single classical optical path from the source, through the double slit, to the camera. The ordinary optical system reproduces the geometry of the ghost experiment.*

---

## Then the entanglement became optional

Turns out the ghost image doesn't need entanglement at all.

Take a laser, pass it through a rotating ground-glass screen, and you get a constantly shifting speckle pattern. Split it into two copies with a beam splitter. Send one copy through the object to a fixed detector. Record the other with a camera.

Neither measurement means anything alone.

Correlate the signal with the recorded speckle patterns, and the image shows up anyway [6,7]. No entangled photons required.

So classical correlations alone reproduce ghost images and ghost interference. Researchers then stripped the apparatus down further: generate the illumination patterns deliberately with a spatial light modulator, and the second beam doesn't even need to be measured [8,9].

At that point the setup has collapsed to its bare essentials — structured light, the object, a single-pixel detector, a computer. Nothing more.

The ghost image survives anyway.

> **Remove the entanglement. Remove the second beam. Replace the camera with a calculation. The ghost image remains.**

<!-- FIGURE 3 -->
![ghost_imaging_three_stages.png](ghost_imaging_three_stages.png)
**Figure 3. Making the ghost classical. Three stages of ghost imaging. Left: entangled photon pairs are measured in two arms. Centre: a beam splitter creates two classically correlated copies of a changing speckle pattern. Right: the second arm disappears entirely — known illumination patterns are projected onto the object, measured with a fixed, non-imaging detector and reconstructed by a computer.**

*Alt text: Three-panel diagram showing the progression from quantum to computational ghost imaging. In the left panel, an SPDC source produces entangled photon pairs; one photon passes through the object to a fixed, non-imaging detector while the other is detected spatially. In the centre panel, a beam splitter divides a random speckle field into two classically correlated beams, again using a fixed detector and a spatial detector. In the right panel, a projector sends known structured illumination patterns onto the object, a single fixed detector measures the transmitted light, and a computer reconstructs the image without a second optical arm.*

---

## But where did the quantum go?

So ghost imaging works without entanglement. Case closed?

Not quite.

The original experiments genuinely used entangled photons. Later ones genuinely worked with light we can describe entirely classically. Computational ghost imaging showed even the second physical beam can go away.

The ghost image, it turns out, was never the quantum test to begin with.

The real distinction only shows up once you ask more of the experiment. D'Angelo and colleagues didn't claim entanglement just because they could produce a ghost image — that bar, we now know, is far too low. Instead, they used the same photon pairs to measure correlations in both position *and* momentum at once, and showed those correlations were simultaneously stronger than any classical source could produce [10].

That's a much harder thing to fake.

A classical system can reproduce a ghost image. It can reproduce ghost interference. But a quantum state can carry unusually sharp correlations in two complementary descriptions at the same time — the spatial cousin of the EPR correlations that made entanglement famous in the first place [4,10].

So was the ghost ever quantum? The photons could be. The correlations could be. A ghost image on its own proves neither.

That distinction matters more now than it used to. Ghost imaging has moved from entangled photon pairs, through thermal speckle, to computational systems that interrogate an object one measurement at a time [8,9]. Recent work pushes this further still — treating the whole thing as information acquisition, choosing each next pattern so the result tells you as much as possible about what you don't yet know [11].

So the original mystery has quietly changed shape. It's no longer just *how does a camera image something its photons never touched?* It's closer to: *what kinds of correlations, and what kinds of information, is an imaging system actually allowed to use?*

> **The ghost image is not the quantum test. The physics lives in what the correlations allow us to learn.**

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
