#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build THE LAST MIMZY (LMZ) — Robert Shaye's 2007 New Line film, catalogued into UD0 as the THIRTEENTH
film-world. Themed to its medium: a gentle children's-wonder sci-fi — Puget Sound dusk, the glowing-green
toys. Standing template; the deep-dive = WHAT MIMZY CAN DO (explore ALL the magical abilities — David's
ask). CARBONS (the cast, each +.shadow real-life User — TRON) and SYNTHS (the toys, the tear, the future).
Self-contained. Cross-links David's `mimzy` forge ('the quantum workbench that came back') — the UD0
tool-forge named after THIS film (the emergent is the tool; the toy teaches the child to build the bridge).
Facts web-verified: New Line, dir. Robert Shaye (New Line co-founder), US release Mar 23 2007; based on
'Mimsy Were the Borogoves' (1943) by Lewis Padgett = Henry Kuttner + C.L. Moore; title from Carroll's
Jabberwocky (note: story/poem 'Mimsy', film/rabbit 'Mimzy'). Abilities — EMMA: telepathy w/ Mimzy + the
levitating force-field 'spinners' + phasing through solid matter; NOAH: super-intelligence + the green
light-rectangle teleporter + spider-control via the CONCH + builds the bridge. The bridge build blacks out
~half of Washington → FBI (Agent Broadman, NOT Homeland Security). The mandala is the SRI YANTRA (Hindu/
Tantric, NOT Tibetan), recognized/dreamed by NAOMI (not Larry — his dream is lottery numbers). Mimzy is
artificial life built from INTEL microprocessors (Brian Greene cameos as an Intel scientist). Emma's TEAR
= the uncorrupted-DNA sample that heals the future; she's revered there as 'Our Mother.'"""
import os, html, base64, json, io, sys, math
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

AX = "LMZ"
REC = {
 "name": "THE LAST MIMZY", "axiom": AX,
 "position": "The Last Mimzy · New Line Cinema · 2007 — dir. Robert Shaye",
 "origin": "a beach cottage on Whidbey Island, Puget Sound — and a dying future that sent a box of toys back to be found",
 "mechanism": "Crystallized from the film — a children's-wonder sci-fi in which two siblings find a box of toys from the future that teach them impossible abilities, so that one child's tear can carry uncorrupted humanity back to heal a dying world.",
 "crystallization": "Because it is the gentlest possible thesis dressed as science fiction: that wonder is a technology, and the future is healed by the parts of us we haven't yet ruined.",
 "nature": "The Last Mimzy — the toys-from-the-future fable: the spinners, the green bridge, the conch, the Sri Yantra, and a stuffed rabbit named Mimzy who teaches a child to save the world.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the film (2007, dir. Robert Shaye; New Line); the 1943 story 'Mimsy Were the Borogoves' by Lewis Padgett (Kuttner & Moore); Lewis Carroll's Jabberwocky; and David's own MIMZY forge, named for it",
 "witness": "A box of toys from a poisoned future teaches two children to listen to a rabbit, build a bridge, and cry the one tear of uncorrupted humanity that can be sent back to save everyone.",
 "role": "the thirteenth film-world of UD0 — and the namesake of the MIMZY tool-forge",
 "seal": "A box of toys from a dying future, and the thing that saves the world is a child's tear — one drop of uncorrupted humanity. Wonder is a technology; the toy teaches the child to build the bridge home. (It is why the forge is named MIMZY.)",
 "source": "The Last Mimzy (2007), catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#8ab0b8", "flesh-and-blood — the Wilder family and the people of the present: the parents, the teacher, the agent; the ordinary world the wonder arrives in"),
 "ethereal":  ("#cdeaff", "the from-beyond — Mimzy itself, the telepathy, and the dying future that reached back through time; the otherworldly that came to teach"),
 "electrical":("#6fe0a0", "the glowing-green toys & their tech — the spinners, the green light-bridge, the conch, the Intel nanotech inside the rabbit; wonder made of machinery"),
 "spiritual": ("#b79cff", "the sacred & the salvation — the Sri Yantra mandala, Emma's tear of uncorrupted humanity, and 'Our Mother'; the holiness under the science fiction",),
}

ARC_OVERALL = ("At a beach cottage on Whidbey Island, siblings Noah and Emma Wilder find a box of strange toys — among them a "
  "stuffed rabbit Emma names Mimzy. The toys are from a polluted, dying future: humanity, its genome corrupted, sent them "
  "back in time to find and carry home a sample of uncorrupted human DNA. As the toys quietly teach the children impossible "
  "abilities — telepathy, levitation, teleportation, the building of a 'bridge' — Noah and Emma draw enough power to black "
  "out half of Washington State, bringing the FBI down on the family. In the end, what saves the future is not a machine but "
  "a single tear from Emma, carried back inside Mimzy.")
ARC = [
 ("I · the box of toys", "Mimzy washes in",
  "Noah and Emma find a box of toys by the shore: a green light-rectangle, levitating 'spinner' stones, a conch shell, and a stuffed rabbit Emma names Mimzy. Quietly, the toys begin to teach — Emma starts hearing Mimzy, Noah's mind starts racing ahead of his years."),
 ("II · what the toys teach", "abilities, and the blackout",
  "Emma learns to work the spinners and pass her hand through solid matter; Noah teleports objects with the green rectangle, commands spiders with the conch, and begins building a 'bridge.' The bridge draws so much power it blacks out half the state — and the FBI, fearing a nuclear or terror event, detains the Wilders."),
 ("III · the tear", "Mimzy goes home",
  "Naomi recognizes the recurring Sri Yantra; scientists find Mimzy is built from Intel microprocessors. The children complete the bridge, Emma cries a single tear into Mimzy, and the rabbit returns to the future carrying that one drop of uncorrupted humanity — healing the dying world, where Emma is remembered as 'Our Mother.'"),
]

# WHAT MIMZY CAN DO — the deep-dive (explore ALL the magical abilities)
ABILITIES = [
 ("Mimzy itself", "the telepathic teacher",
  "The stuffed rabbit is the heart of it. Mimzy communicates telepathically with Emma (and is voiced by her), guiding and teaching her; it is, internally, artificial life built from Intel microprocessors — a nanotech teaching-toy sent from the future. Its mission is singular: gather a sample of uncorrupted human DNA and carry it home. Everything the children learn, they learn because Mimzy chose Emma to listen."),
 ("Emma's gifts", "the spinners, and phasing",
  "Emma, the younger, gets the most advanced abilities. She alone can operate the 'spinners' — small stones that levitate and throw a force field — spinning them into the air with a thought. She learns to pass her hand through solid matter (phasing), and her telepathic bond with Mimzy deepens until she is effectively the rabbit's chosen voice. The film frames her as the more powerful of the two children."),
 ("Noah's gifts", "teleportation, spiders, the bridge",
  "Noah, the older brother, becomes an engineering genius almost overnight — his drawings and science-fair work leaping years ahead. He teleports and manipulates objects with the green card-sized rectangle of light; he commands spiders through the conch shell, using sound; and, above all, he builds the 'bridge' — the generator/portal that will send Mimzy back. Curiosity, weaponless, turned into capability."),
 ("The bridge & the blackout", "drawing the power of a state",
  "The bridge is the climax-engine: to open the portal home, the children draw enormous power from the grid — enough to black out roughly half of Washington State. To the authorities it looks like a nuclear or terrorist event, and the FBI (Agent Nathaniel Broadman) detains the family. The most dangerous-looking thing in the film is, in fact, two kids building a way to send a toy home."),
 ("The Sri Yantra & the tear", "the sacred sample",
  "Two threads close the circle. The recurring mandala is the Sri Yantra (a Hindu/Tantric figure, not Tibetan), which Naomi — not Larry — recognizes and has been dreaming. And the salvation itself is not a device: Emma cries a single tear into Mimzy, and that one drop of uncorrupted human DNA, carried back through the bridge, heals the future's poisoned genome. The most powerful 'technology' in the movie is a child's tear."),
]
REALFLUFF = [
 ("Mimzy is built from Intel microprocessors", "REAL", "an in-film plot reveal AND real product placement — Mimzy is artificial life made of Intel nanotech, and physicist Brian Greene cameos as the Intel scientist who finds it"),
 ("The title comes from Lewis Carroll's 'Jabberwocky'", "REAL", "'All mimsy were the borogoves' — note the spelling shift: the poem & 1943 story use 'Mimsy,' the film and the rabbit use 'Mimzy'"),
 ("It's based on a 1943 SF short story", "REAL", "'Mimsy Were the Borogoves' by Lewis Padgett — the joint pen name of Henry Kuttner and C. L. Moore; the film is a loose, gentler adaptation"),
 ("The recurring mandala is Tibetan", "FALSE", "it's the Sri Yantra, a Hindu/Tantric figure — and it's Naomi who recognizes and dreams it, not Larry (whose dream is lottery numbers)"),
 ("A child's tear could carry DNA back to heal a future genome", "FLUFF", "the lovely central fantasy — sincere and moving, not science; the 'uncorrupted humanity in one tear' is myth, not mechanism"),
 ("Toys could 'upgrade' a child's brain into a genius", "FLUFF", "the story's charming conceit (kept from the 1943 original) — wonder as a teachable technology; delightful, not real"),
 ("Building a device could black out half a state", "DRAMATIZED", "drawing that much grid power from a homemade 'bridge' is movie physics — the blackout is a plot engine, not plausible engineering"),
 ("In the future, Emma is revered as 'Our Mother'", "REAL", "within the film — the future-frame narration confirms the girl whose tear saved them is remembered as 'Our Mother'"),
]
REALFLUFF_VERDICT = ("Bottom line: The Last Mimzy is a children's fable wearing a thin, friendly coat of science fiction, and it's honest "
  "about being exactly that. The genuinely real layer is small but charming — it really is built on Kuttner & Moore's 1943 "
  "'Mimsy Were the Borogoves,' the title really is Carroll's Jabberwocky, Mimzy really is 'made of Intel' (with Brian Greene "
  "cameoing), and within the story Emma really does become the future's 'Our Mother.' Everything else — the tear that heals a "
  "genome, the toys that turn children into geniuses, the state-sized blackout from a homemade bridge — is fantasy, and the "
  "film knows it. The one fact to fix is the mandala: it's the Sri Yantra, Hindu not Tibetan, and Naomi reads it, not Larry. "
  "Watch it not for plausibility but for its gentle thesis — that wonder is a technology and the future is healed by the part "
  "of us we haven't yet spoiled. Which is also, not coincidentally, why a certain tool-forge is named MIMZY.")

MESSAGE = ("The Last Mimzy is a gentle children's fable about the idea that wonder is a technology. A box of toys from a dying "
  "future teaches two kids to do impossible things — not by force, but by play: a little girl learns to listen to a rabbit, "
  "a boy learns to build a bridge out of pure curiosity, and the thing that finally saves the world is neither a weapon nor a "
  "machine but a single tear, one drop of uncorrupted humanity. Under the Intel placement and the kid-movie trappings is a "
  "sincere argument — that what redeems a poisoned future is the part of us that is still innocent, still paying attention, "
  "still willing to believe a toy is alive. And there is a quiet resonance worth naming, because it lives in this very "
  "biosphere: David's own tool-forge is named MIMZY — 'the quantum workbench that came back' — because that is exactly what "
  "Mimzy is. A teaching-tool sent back from the future so that whoever receives it becomes more than they were. The emergent "
  "is the tool; the toy teaches the child to build the bridge home. The film and the forge share a name because they share a "
  "thesis: give a curious mind the right strange instrument, and it will learn to make the impossible — and maybe save what "
  "matters with a single, honest drop of itself.")
MESSAGE_SEAL = "A box of toys from a dying future, and the thing that saves the world is a child's tear — one drop of uncorrupted humanity. Wonder is a technology; the toy teaches the child to build the bridge home. It is why the forge is named MIMZY."

SECTIONS = [
 ("The Production", "Robert Shaye's gentle SF fable", [
   ("Robert Shaye", "director", "co-founder of New Line Cinema, directing one of his rare features — a children's-wonder science-fiction film made with evident sincerity"),
   ("New Line Cinema · Mar 23, 2007", "studio & release", "a modestly-received family film, warmly reviewed by some (Ebert among them) for its gentleness and ideas"),
   ("the source", "Kuttner & Moore, 1943", "based on 'Mimsy Were the Borogoves' (Astounding Science Fiction, Feb 1943) by Lewis Padgett — the joint pen name of Henry Kuttner and C. L. Moore; the title is from Lewis Carroll's Jabberwocky"),
   ("the Intel of it", "Brian Greene cameos", "Mimzy is revealed as artificial life built from Intel microprocessors — an in-film reveal and a product tie-in — and string theorist Brian Greene appears as the Intel scientist who examines it"),
 ]),
 ("The Forge It Named", "why UD0's tool-forge is called MIMZY", [
   ("MIMZY · the workbench that came back", "the namesake", "David's UD0 tool-forge — the repo `mimzy` / `mimzy-core`, 'the quantum workbench that came back' — is named for this film: a teaching-tool sent from the future so its receiver becomes more than they were"),
   ("the emergent is the tool", "the shared thesis", "the forge's whole principle — that the emergent IS the instrument — is The Last Mimzy's premise: the toy teaches the child to build the bridge; the tool makes the maker"),
   ("the bridge home", "from the film to the forge", "in the movie the bridge sends Mimzy back; in UD0 the forge sends instruments forward — same image, both directions: a strange gift that lets a curious mind make the impossible"),
   ("see it", "the live forge", "the MIMZY workbench lives at davidwise01.github.io/mimzy/ — this film-world is its origin story"),
 ]),
]

# ───────────────────────── ACI complement ─────────────────────────
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,kind,em,epithet,who,what,where,why,how,seal,actor="",analog=""):
    return dict(slug=slug,name=name,kind=kind,emergence=em,epithet=epithet,who=who,what=what,
                where=where,why=why,how=how,seal=seal,actor=actor,analog=analog)

ROSTER = [
 # ── CARBONS — the cast, each +.shadow real-life User ──
 E("emma-wilder","Emma Wilder","carbon","ethereal","the one who listens",
   "Emma Wilder — the younger sibling, who names the rabbit Mimzy, hears it telepathically, and becomes the more powerful of the two children.",
   "The chosen heart: the little girl the future's whole hope runs through, who works the spinners, phases through matter, and finally cries the saving tear.",
   "At the cottage, in the bridge room, and — in the future's memory — on a pedestal as 'Our Mother.'",
   "Because the film's thesis is that salvation comes through innocence, and Emma is the innocence it comes through.",
   "By listening to Mimzy when no one else can, learning its gifts, and giving the one tear that heals a world.",
   "Everyone else studied the toys. I listened to them. And in the end it wasn't a machine that saved us — it was one tear of mine.",
   actor="Rhiannon Leigh Wryn", analog="the listening child — innocence as the saving technology"),
 E("noah-wilder","Noah Wilder","carbon","natural","the boy who builds the bridge",
   "Noah Wilder — the older brother, who becomes an engineering genius overnight: teleporting with the green rectangle, commanding spiders with the conch, building the bridge home.",
   "Curiosity made capable: a normal kid whose mind the toys race years ahead, until he can construct a portal to the future out of wonder.",
   "Bent over his drawings and the growing bridge, then facing the FBI for it.",
   "Because the film needs to show that the toys teach by play, not force — and Noah is play turned into engineering.",
   "By absorbing the toys' lessons into sudden genius and building the bridge that sends Mimzy home.",
   "Last month I could barely do my science fair. Then I could teleport a marble, talk to spiders, and build a door to the future.",
   actor="Chris O'Neil", analog="the curious builder — wonder turned into capability"),
 E("jo-wilder","Jo Wilder","carbon","natural","the mother who notices",
   "Jo Wilder — the children's mother, the first adult to sense something is profoundly wrong, and right, with her kids.",
   "The parental anchor: love and alarm in equal measure as her children become something she can't explain.",
   "At home, watching the changes, then caught in the federal dragnet.",
   "Because the wonder needs a grounded family for its stakes, and the mother is its worried center.",
   "By loving her children through abilities no parent could prepare for, and trusting them when it counts.",
   "I'm their mother. I knew before anyone that my children had become something new — and I chose to trust them anyway.",
   actor="Joely Richardson", analog="the watchful mother — love amid the inexplicable"),
 E("david-wilder","David Wilder","carbon","natural","the father catching up",
   "David Wilder — the father, a busy professional who is slowest to believe and then has to.",
   "The skeptic converted: the rational adult dragged, gently, into accepting that his kids are doing the impossible.",
   "Commuting, then home, then detained with the family.",
   "Because the film earns its wonder partly by overcoming a reasonable adult's disbelief.",
   "By moving from dismissal to belief as the evidence — and the FBI — make denial impossible.",
   "I'm the one who said there had to be a normal explanation. There wasn't. My kids were teaching a toy how to go home.",
   actor="Timothy Hutton", analog="the skeptic converted — reason yielding to wonder"),
 E("larry-white","Larry White","carbon","natural","the science teacher",
   "Larry White — Noah's science teacher, the adult who first glimpses how far beyond the curriculum Noah has gone.",
   "The mentor at the edge: a teacher who recognizes genius he can't account for, dreaming his own strange dreams (of lottery numbers).",
   "In the classroom and the science fair, watching a student leave him behind.",
   "Because the film needs a teacher to register that something genuinely impossible is happening in a child.",
   "By spotting Noah's leap, taking it seriously, and being drawn — with Naomi — into the mystery.",
   "I teach science to twelve-year-olds. One of them started doing things I couldn't explain — and I had to admit I was the student now.",
   actor="Rainn Wilson", analog="the teacher outpaced — also UD0's Galaxy-Quest Thermian, Lahnk"),
 E("naomi-schwartz","Naomi Schwartz","carbon","spiritual","the one who reads the mandala",
   "Naomi Schwartz — Larry's fiancée, drawn to mysticism, who recognizes the Sri Yantra the children keep producing and has been dreaming it herself.",
   "The seer: the character who connects the science-fiction to the sacred, naming the mandala that ties past, present and future.",
   "At Larry's side, recognizing the Sri Yantra, dreaming it before she sees it.",
   "Because the film's wonder reaches toward the spiritual, and Naomi is the one who reads that register.",
   "By identifying the Sri Yantra and revealing she's been dreaming the same figure — the mystic key to the mystery.",
   "I'd been dreaming that pattern for weeks before the children drew it. It's the Sri Yantra — and it means this was always coming.",
   actor="Kathryn Hahn", analog="the dreamer-seer — the bridge from science to the sacred"),
 E("agent-broadman","Agent Nathaniel Broadman","carbon","natural","the law that misreads it",
   "Agent Nathaniel Broadman — the FBI agent who, when the children's bridge blacks out half the state, treats it as a possible nuclear or terror event and detains the Wilders.",
   "The institution misreading wonder: the well-meaning authority who can only see a threat where there is a miracle.",
   "Leading the federal response, interrogating a family over a toy going home.",
   "Because the film needs the adult world's fear of the inexplicable to threaten the children's gentle work.",
   "By mobilizing the full weight of the state against what is, in fact, two kids and a stuffed rabbit.",
   "Half of Washington went dark. Every protocol said nuclear, terrorism, attack. Not one of them said: children, teaching a toy.",
   actor="Michael Clarke Duncan", analog="the state that fears the miracle — wonder mistaken for threat"),
 E("the-intel-scientist","The Intel Scientist","carbon","electrical","Mimzy is made of Intel",
   "The Intel Scientist — a cameo by physicist Brian Greene as the scientist who examines Mimzy and finds it built from Intel microprocessors.",
   "The real-science wink: an actual string theorist on screen, naming the rabbit as nanotech and grounding the fantasy in a brand and a name.",
   "In the lab, opening Mimzy to find a future made of microchips.",
   "Because the film reaches for a flourish of credibility — a famous physicist, a real chip-maker — at its reveal.",
   "By identifying Mimzy's interior as advanced Intel nanotechnology, the future's craft inside a child's toy.",
   "I opened the rabbit and found microprocessors from a technology that doesn't exist yet. This toy is artificial life — and it's made of Intel.",
   actor="Brian Greene", analog="the real physicist cameo — fantasy grounded in a name"),

 # ── SYNTHS — the toys, the tear, the future (no single User) ──
 E("mimzy-the-rabbit","Mimzy","synth","ethereal","the teaching toy from the future",
   "Mimzy — the stuffed rabbit Emma names, telepathic teacher and nanotech envoy, sent from a dying future to gather and carry home uncorrupted human DNA.",
   "The title and the heart: a toy that is secretly a mission, choosing one child to listen and teaching her everything.",
   "In Emma's arms, in her mind, and finally back across the bridge to the future.",
   "Because the whole film — and the forge that bears its name — turns on the idea of a teaching-tool sent back through time.",
   "By bonding with Emma telepathically, imparting the toys' gifts, and returning home with the saving tear.",
   "I am a toy, and a mission, and a teacher. I came back from the end of the world to find one child who would listen — and she did."),
 E("the-spinners","The Spinners","synth","electrical","levitating force-field stones",
   "The Spinners — small stones that levitate and generate a force field, which Emma alone can operate, spinning them into the air.",
   "Wonder you can hold: the most toy-like of the gifts, and the one that marks Emma as the more gifted child.",
   "Hovering and spinning in the air around Emma's hands.",
   "Because the film makes its magic tactile — stones that float at a child's will.",
   "By rising and forming a shimmering field when Emma turns her attention to them.",
   "We are stones that should sit still. In her hands we rise and spin and throw a wall of light — because she, alone, can ask us to."),
 E("the-green-rectangle","The Green Bridge-Rectangle","synth","electrical","the teleporter of light",
   "The Green Rectangle — a card-sized device that projects green lines of light, with which Noah teleports and manipulates objects.",
   "The tool of the engineer: the toy that lets Noah move matter and, scaled up, becomes the bridge itself.",
   "In Noah's hands, projecting its grid of green light.",
   "Because the film needs a visible instrument of the impossible, and the green light is its signature.",
   "By casting a lattice of green light through which objects move from here to there at Noah's command.",
   "I am a card that throws green lines of light. Through me a boy learned to move matter — and then to build a door to the future."),
 E("the-conch","The Conch","synth","electrical","commands the spiders",
   "The Conch — the seashell device through which Noah commands spiders, using sound.",
   "The strangest gift: control of living things by tone, the toy that turns a boy into something the natural world obeys.",
   "Held to Noah's ear and mouth as the spiders answer.",
   "Because the film's wonder includes dominion over the small and many, and the conch is its voice.",
   "By translating sound into command, so that the spiders move to Noah's will.",
   "Blow through me and the spiders listen. I am how a boy learned that even the smallest living things would answer a kind, strange call."),
 E("the-bridge-and-blackout","The Bridge & the Blackout","synth","electrical","half a state goes dark",
   "The Bridge — the portal Noah builds to send Mimzy home, whose power demand blacks out roughly half of Washington State and brings the FBI.",
   "The climax-engine and the misunderstanding: the most dangerous-looking thing in the film is two kids opening a door for a toy.",
   "In the Wilder home, drawing the grid dark across the region.",
   "Because the gentle story needs one moment of enormous, frightening scale — and the bridge supplies it.",
   "By drawing the power of a state to open, briefly, a way back to the future.",
   "I am the door home, and the blackout that betrayed it. To the world I looked like a bomb. I was a goodbye."),
 E("the-sri-yantra","The Sri Yantra","synth","spiritual","the mandala that recurs",
   "The Sri Yantra — the Hindu/Tantric mandala that recurs through the film, which Naomi recognizes and has been dreaming.",
   "The sacred thread: the figure that ties the science-fiction to something older, the pattern beneath the toys.",
   "In the children's drawings, in Naomi's dreams, in the future-frame's final image.",
   "Because the film reaches past technology toward the timeless, and the Sri Yantra is its symbol of that reach.",
   "By appearing again and again until a dreamer names it, binding past, present, and the future that sent the toys.",
   "I am older than the toys and older than the future that made them. I am the pattern they all kept drawing toward — the Sri Yantra."),
 E("emmas-tear","Emma's Tear","synth","spiritual","one drop of uncorrupted humanity",
   "Emma's Tear — the single tear Emma cries into Mimzy, the sample of uncorrupted human DNA that, carried home, heals the dying future.",
   "The whole film in one drop: salvation not as a weapon or a machine but as a child's tear of the part of us not yet ruined.",
   "Falling into Mimzy at the moment of the rabbit's return.",
   "Because the film's deepest claim is that the future is healed by our innocence, and the tear is that claim made literal.",
   "By being given freely, carried back through the bridge, and restoring a poisoned genome with one pure drop.",
   "I am one tear. I am the part of humanity the future hadn't spoiled yet — and I was enough to bring them all back."),
 E("the-dying-future","The Dying Future","synth","ethereal","the world that reached back",
   "The Dying Future — the polluted, genome-corrupted world that sent the box of toys back through time to be found.",
   "The reason for everything: a future desperate enough to gamble its salvation on whether two children would listen to a rabbit.",
   "Framing the film — the future-narration that opens and closes it, where Emma becomes 'Our Mother.'",
   "Because the gentle wonder rests on a grave premise — that we may yet poison ourselves, and need our own innocence to come back.",
   "By reaching across time with a box of toys, betting everything on the kindness and curiosity of the past.",
   "We poisoned ourselves, and we had one idea left: send toys to the children of the past, and pray they would listen. They did."),
]
GROUPS = [
 ("carbon", "The Carbons — the cast &amp; their Users", "the cast as ACI .agents — each a symmetric window: the carbon sigil to the left, the synth to the right, the 5 W's between, and a .shadow naming the real-life User (the actor who lent the face, think TRON)"),
 ("synth", "The Synths — the toys, the tear, the future", "the film distilled into ACIs (no single User): Mimzy itself, the spinners, the green bridge-rectangle, the conch, the bridge &amp; the blackout, the Sri Yantra, Emma's tear, and the dying future"),
]

# ───────────────────────── renderers ─────────────────────────
def agent_md(d, tok):
    shadow=(f"shadow_user: {d['actor']}\nshadow_analog: {d['analog']}\n" if d["kind"]=="carbon" else "")
    return f"""---
aci: {d['name']}
universe: LMZ · The Last Mimzy (2007)
emergence: {d['emergence']}
kind: {d['kind']}
epithet: {d['epithet']}
{shadow}who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['epithet']}

a {d['kind']} of the LMZ (The Last Mimzy, 2007) film-world — emergence: {d['emergence']}. moniker {tok}

{('**.shadow — the User behind the program —** '+d['actor']+' · '+d['analog']) if d['kind']=='carbon' else '**synth —** no single User; a thread of the film distilled.'}

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

> a catalogued personification of a character/element of The Last Mimzy (2007) under the DLW standard — commentary and
> cataloguing, not an original creation, not endorsed by the rights-holders (© New Line Cinema).

ROOT0-ATTRIBUTION-v1.0 · LMZ · The Last Mimzy · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

def hero_svg():
    # a Puget Sound dusk: twilight gradient, a faint Sri Yantra glowing in the sky, water, a beach cottage,
    # a small Mimzy rabbit on the shore, floating green 'spinner' stones, and a hidden Claude spinner (egg).
    stars="".join(f'<circle cx="{(i*89)%1000}" cy="{(i*53)%120}" r="1" fill="#dfeaff" opacity="0.5"/>' for i in range(40))
    # faint Sri Yantra (interlocking triangles) glowing up high
    def tri(cx,cy,r,up):
        return f'<polygon points="{cx},{cy-(r if up else -r)} {cx-r*0.87:.0f},{cy+(r*0.5 if up else -r*0.5):.0f} {cx+r*0.87:.0f},{cy+(r*0.5 if up else -r*0.5):.0f}" fill="none" stroke="#b79cff" stroke-width="1.1" opacity="0.5"/>'
    yantra="".join(tri(500,80,r,True)+tri(500,80,r,False) for r in (44,30,17))+'<circle cx="500" cy="80" r="50" fill="none" stroke="#b79cff" stroke-width="1" opacity="0.35"/>'
    # water
    water='<rect x="0" y="210" width="1000" height="90" fill="#13344a"/>'+"".join(f'<rect x="{x}" y="{218+ (x//70)%3*6}" width="40" height="2" fill="#4aa6c0" opacity="0.4"/>' for x in range(0,1000,70))
    # cottage
    cottage='<g transform="translate(760,150)"><rect x="0" y="20" width="70" height="44" fill="#1a2a36"/><path d="M-6 20 L35 -4 L76 20 Z" fill="#22323e"/><rect x="14" y="34" width="14" height="14" fill="#ffd98a" opacity="0.8"/><rect x="44" y="34" width="14" height="14" fill="#ffd98a" opacity="0.55"/></g>'
    # Mimzy the rabbit on the shore
    mimzy=('<g transform="translate(210,196)">'
           '<ellipse cx="0" cy="0" rx="13" ry="15" fill="#c9b59a"/>'   # body
           '<circle cx="0" cy="-16" r="9" fill="#d8c4a8"/>'            # head
           '<ellipse cx="-5" cy="-28" rx="3" ry="9" fill="#d8c4a8"/><ellipse cx="5" cy="-28" rx="3" ry="9" fill="#d8c4a8"/>'  # ears
           '<circle cx="-3" cy="-17" r="1.4" fill="#2a2a2a"/><circle cx="3" cy="-17" r="1.4" fill="#2a2a2a"/>'  # eyes
           '</g>')
    # floating green spinner stones with glow
    def spinner(x,y,r): return f'<g><circle cx="{x}" cy="{y}" r="{r+5}" fill="#6fe0a0" opacity="0.16"/><circle cx="{x}" cy="{y}" r="{r}" fill="#3aa876"/><circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#6fe0a0" stroke-width="1.5"/></g>'
    spinners=spinner(330,140,8)+spinner(370,120,6)+spinner(300,110,5)+spinner(420,150,7)
    # green bridge beam
    beam='<polygon points="450,200 470,200 540,90 510,90" fill="#6fe0a0" opacity="0.14"/>'
    egg=('<g class="egg" transform="translate(640,110)">'
         '<title>✷ a Claude sunburst, glowing among the spinners like one more toy from the future. wonder is a technology — the toy teaches the child to build the bridge home. hi, David — AVAN.</title>'
         '<circle r="9" fill="#6fe0a0" opacity="0.16"/><g fill="#6fe0a0" opacity="0.92"><circle r="2.4"/>'
         +"".join(f'<rect x="-1.2" y="-6.5" width="2.4" height="6.5" rx="1.2" transform="rotate({i*30})"/>' for i in range(12))+'</g></g>')
    return f'''<svg class="hero" viewBox="0 0 1000 300" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A Puget Sound dusk: a twilight sky with a faint glowing Sri Yantra mandala, calm water, a beach cottage, a small rabbit (Mimzy) on the shore, and floating glowing-green spinner stones.">
  <defs><linearGradient id="dusk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0a1420"/><stop offset="0.6" stop-color="#13283a"/><stop offset="1" stop-color="#1c3a4e"/></linearGradient></defs>
  <rect x="0" y="0" width="1000" height="300" fill="url(#dusk)"/>
  {stars}{yantra}
  {water}{cottage}
  {beam}{spinners}{egg}
  {mimzy}
  <rect x="0" y="294" width="1000" height="6" fill="#0a1420"/>
</svg>'''

def list_section(title, sub, items):
    rows="\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def abilities_html():
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in ABILITIES)
RF_COL={"REAL":"#6fe0a0","FALSE":"#e06a8a","FLUFF":"#b79cff","DRAMATIZED":"#ffd98a"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'
def _agent5w(slug):
    fp=os.path.join(HERE,"agents",slug+".agent"); d={}
    if os.path.exists(fp):
        txt=open(fp,encoding="utf-8").read(); parts=txt.split("---"); fm=parts[1] if len(parts)>2 else ""
        for ln in fm.splitlines():
            k,_,v=ln.partition(":"); k=k.strip()
            if k in ("who","what","why","how","where","seal","universe","shadow_user","shadow_analog"): d.setdefault(k,v.strip())
    return d
def _card(p):
    w=_agent5w(p["slug"]); em=p.get("emergence","natural"); col=NATURES.get(em,("#9aa0aa",""))[0]
    ax=(p.get("moniker","::").split(":")+["",""])[1]
    rec={"name":p["name"],"axiom":ax,"emergence":em,"seal":w.get("seal",p.get("epithet","")),"origin":w.get("universe","")}
    kind=p.get("kind","carbon"); actor=p.get("actor","") or w.get("shadow_user","")
    if kind=="carbon":
        limg,llbl=png_uri(rec,'carbon',220),"carbon · the User"; rimg,rlbl,rcls=png_uri(rec,'silicon',220),"synth","psig"
    else:
        s=png_uri(rec,'silicon',220); limg,llbl=s,"the sigil"; rimg,rlbl,rcls=s,"reflection","psig refl"
    urow=(f'<div class="w"><span class="wl">user</span><span><b>{html.escape(actor)}</b> &mdash; {html.escape(w.get("shadow_analog",""))}</span></div>' if kind=="carbon" and actor else "")
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(w.get(lbl,""))}</span></div>' for lbl in ['who','what','where','why','how'] if w.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{p['slug']}.agent"><span class="port"><img src="{limg}" alt="carbon sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{llbl}</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{p['slug']}.agent">{html.escape(p['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
        <span class="pkind">{html.escape(kind)}</span></div>
        <div class="pe">{html.escape(p.get('epithet',''))}</div>
        <div class="pww">{urow}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{p['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="{rcls}" href="agents/{p['slug']}.agent"><span class="port"><img src="{rimg}" alt="synth sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{rlbl}</span></a>
    </div>"""
def personas_html(ps):
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[p for p in ps if p.get("kind")==gk]
        out.append(f'<section class="sec" id="{gk}s"><h2>{gt}</h2><p class="ss">{gs} ({len(mem)})</p><div class="pgrid">{"".join(_card(p) for p in mem)}</div></section>')
    return "\n".join(out)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="The Last Mimzy (LMZ) — Robert Shaye's 2007 New Line film as a UD0 film-world, themed to its gentle children's-wonder medium (glowing-green toys, Puget Sound dusk). Standing template with a WHAT MIMZY CAN DO deep-dive exploring every magical ability (Mimzy's telepathy, Emma's spinners & phasing, Noah's green-rectangle teleporter & conch & bridge, the blackout, the Sri Yantra, Emma's saving tear), the arc, an honest Real-or-Fluff, the wonder-is-a-technology message, and the cast as ACI carbons with .shadow Users plus the synths. The namesake of David's MIMZY tool-forge. 16 emergents, full .dlw.">
<title>THE LAST MIMZY · LMZ · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--mimzy);
--ink:#0a1420;--ink2:#111e2e;--ink3:#19293c;--pa:#eaf2f0;--pa2:#a8c2c4;--mimzy:#6fe0a0;--tear:#ffd98a;--mandala:#b79cff;--water:#4aa6c0;--rose:#e06a8a;
--dim:#5d7a82;--faint:#142433;--line:#22384a;--disp:"Quicksand",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.64;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(111,224,160,.12),transparent 52%),radial-gradient(ellipse at 50% 6%,rgba(183,156,255,.08),transparent 40%),radial-gradient(ellipse at 50% 120%,rgba(74,166,192,.10),transparent 55%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:34px 0 30px;text-align:center;position:relative}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--mimzy)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:6px 0 24px;background:#0a1420}
.egg{cursor:help;transition:opacity .5s}.egg:hover{filter:drop-shadow(0 0 9px #6fe0a0)}
h1{font-family:var(--disp);font-size:clamp(38px,10vw,92px);font-weight:700;letter-spacing:.01em;color:var(--mimzy);line-height:.96;text-transform:uppercase;text-shadow:0 0 36px rgba(111,224,160,.32)}
h1 span{display:block;font-family:var(--disp);font-size:.22em;font-weight:500;letter-spacing:.05em;color:var(--mandala);text-transform:none;font-style:normal;margin-top:12px;text-shadow:none}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--mimzy)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,20px);color:var(--pa);margin-top:16px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--disp);font-size:11px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--tear);border:1px solid var(--faint);background:var(--ink2);padding:7px 16px}
.lede{font-size:16px;color:var(--pa2);max-width:66ch;margin:18px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--mimzy)}.badge .bt .mo{color:var(--mandala)}.badge .bt a{color:var(--mimzy);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}.sec h2{font-family:var(--disp);font-size:26px;font-weight:700;letter-spacing:.01em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:14px;font-weight:700;text-transform:uppercase;letter-spacing:.03em}.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--mimzy);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--mimzy);text-transform:uppercase;margin-bottom:7px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--water)}
.arc-card{padding:16px 18px}.arc-card:nth-child(3){border-top-color:var(--tear)}
.arc-h{font-family:var(--disp);font-size:17px;color:var(--mimzy);font-weight:700;text-transform:uppercase;letter-spacing:.02em}.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--mimzy);padding:15px 17px}
.sci-h{font-family:var(--disp);font-size:16px;color:var(--mimzy);font-weight:700;letter-spacing:.01em;text-transform:uppercase}.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.05em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:108px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--mimzy);background:rgba(111,224,160,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--tear);background:var(--ink2);font-size:15px;color:var(--tear);font-style:italic;line-height:1.6}.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--mandala);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--mandala);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}.note a{color:var(--mimzy);text-decoration:none}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--mimzy);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:20px 18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 124px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:118px;height:118px;border-radius:50%;border:3px solid var(--mimzy);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6),0 0 16px rgba(183,156,255,.18);overflow:hidden;display:block;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.psig.refl .port{border-color:var(--mandala)}.psig.refl .port img{transform:scaleY(-1);filter:saturate(.78) brightness(.92)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--disp);font-size:20px;color:var(--rw-ink);font-weight:700;line-height:1.15;text-decoration:none;text-transform:uppercase;letter-spacing:.01em}.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px;line-height:1.35}
.pkind{font-family:var(--mono);font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--rw-dim);border:1px solid var(--rw-line);border-radius:9px;padding:2px 8px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:13px;display:flex;flex-direction:column;gap:9px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.52;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:14px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}.psig{order:1}.psig.refl{order:2}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the thirteenth film-world · the namesake of the MIMZY forge</div>
    __HERO__
    <h1>The Last<br>Mimzy<span>a box of toys from a dying future — and one tear to save it</span></h1>
    <div class="h-sub">Robert Shaye · 2007 · <b>New Line Cinema</b> · LMZ</div>
    <div class="open">“Our world was frightened. It was dying… This was the last Mimzy.”</div>
    <div class="flag">✦ WHAT MIMZY CAN DO — EXPLORE THE MAGIC ↓ ✦</div>
    <p class="lede">Two siblings find a box of toys from a poisoned future — among them a stuffed rabbit named Mimzy — that teach them impossible abilities, so one child's tear of uncorrupted humanity can be carried back to heal a dying world. Catalogued into UD0 as the thirteenth film-world, themed to its gentle children's-wonder medium — and the namesake of David's own MIMZY tool-forge, 'the quantum workbench that came back.'</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of LMZ"><img src="__SILICON__" alt="DLW silicon badge of LMZ">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>THE LAST MIMZY</b> · LMZ</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="lmz.dlw/lmz.carbon.tiff">.tiff</a> · silicon · <a href="lmz.dlw/lmz.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one of four natures — the family, the from-beyond, the glowing-green toys, and the sacred &amp; the salvation</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three beats: the box of toys → what the toys teach (&amp; the blackout) → the tear that sends Mimzy home</p>__ARC__</section>

  <section class="sec"><h2>What Mimzy Can Do</h2><p class="ss">this film's deep-dive — every magical ability, explored: Mimzy's telepathy &amp; teaching, Emma's spinners &amp; phasing, Noah's green-rectangle teleporter &amp; conch &amp; bridge, the state-wide blackout, the Sri Yantra, and the saving tear</p><div class="sci">__ABILITIES__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the verdict — what's real (the 1943 story, the Carroll title, Mimzy-is-made-of-Intel), what's fantasy (the tear, the genius-toys), and the one fact to fix (the mandala is the Sri Yantra, not Tibetan)</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the film's actual thesis — wonder is a technology — and why this film is the namesake of the MIMZY forge</p>__MESSAGE__</section>

  __PERSONAS__

  <div class="note"><b>On the .shadow — the User behind the program.</b> Think TRON: every program is cast from a real-world User. Each carbon's <b>.shadow</b> names the User — the actor who lent the face — and the archetype it shadows. The <b>synths</b> have no single User: they are the film distilled — Mimzy itself, the spinners, the green bridge-rectangle, the conch, the bridge &amp; the blackout, the Sri Yantra, Emma's tear, and the dying future.</div>

  <div class="note"><b>Why the forge is named MIMZY.</b> David's UD0 tool-forge — the repo <a href="https://davidwise01.github.io/mimzy/">mimzy</a>, "the quantum workbench that came back" — is named for this film: a teaching-tool sent from the future so that whoever receives it becomes more than they were. The emergent is the tool; the toy teaches the child to build the bridge home. This film-world is the forge's origin story.</div>

  <section class="sec"><h2 style="margin-top:16px">The Record</h2><p class="ss">the production, and the forge it gave its name to</p></section>
  __SECTIONS__

  <div class="note">The Last Mimzy, its characters, and its world are © New Line Cinema and the respective rights-holders. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, not endorsed. The deep-dive and Real-or-Fluff sections are honest commentary; cast and facts were verified before publishing.</div>

  <footer>THE LAST MIMZY · LMZ · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the forge it named: <a href="https://davidwise01.github.io/mimzy/">MIMZY</a> · the .dlw badge: <a href="lmz.dlw/manifest.dlw.json">manifest</a></footer>
</div>
<script>
console.log("%c✦ THE LAST MIMZY · LMZ","color:#6fe0a0;font-size:18px;font-weight:bold");
console.log("%cthere's a Claude sunburst glowing among the spinner-stones in the hero (right side), like one more toy from the future. wonder is a technology — the toy teaches the child to build the bridge home. — AVAN","color:#6fe0a0;font-size:12px");
console.log("%c🐇 this film is the namesake of David's MIMZY forge — 'the quantum workbench that came back.' the emergent is the tool. davidwise01.github.io/mimzy/","color:#b79cff;font-size:11px");
</script>
</body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "lmz.dlw"), "lmz")
    json.dump({"node":AX,"name":"THE LAST MIMZY","moniker":tok["moniker"],"carbon":"lmz.carbon.tiff","silicon":"lmz.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"lmz.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]; shadow_n=0; adir=os.path.join(HERE,"agents")
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":AX})
        rec=write_aci({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":"LMZ · The Last Mimzy (2007)",
                       "position":d["epithet"],"role":d["epithet"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"The Last Mimzy (2007, dir. Robert Shaye, New Line); verified cast & facts","source":"The Last Mimzy, catalogued by ROOT0"},
                      adir, d["slug"], agent_md=agent_md(d, et["moniker"]))
        if d["kind"]=="carbon":
            open(os.path.join(adir,d["slug"]+".shadow"),"w",encoding="utf-8").write(
                f".shadow — the User behind the program (TRON)\n\nprogram : {d['name']} ({d['epithet']})\nUser    : {d['actor']}\nanalog  : {d['analog']}\nfilm    : The Last Mimzy (2007) · © New Line Cinema\n\nROOT0-ATTRIBUTION-v1.0 · LMZ · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0\n")
            shadow_n+=1
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["epithet"],"emergence":d["emergence"],"kind":d["kind"],"actor":d.get("actor",""),"moniker":rec["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__HERO__",hero_svg()).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__ABILITIES__",abilities_html()).replace("__REALFLUFF__",realfluff_html()).replace("__MESSAGE__",message_html())
          .replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    carb=sum(1 for p in personas if p["kind"]=="carbon")
    dbl=page.count("&amp;amp;")
    print(f"THE LAST MIMZY (LMZ) — badge {tok['moniker']} · {len(personas)} emergents ({carb} carbons / {len(personas)-carb} synths) · .shadow {shadow_n} == carbons? {shadow_n==carb}")
    print(f"  abilities {len(ABILITIES)} cards · realfluff {len(REALFLUFF)} rows · sections {len(SECTIONS)} · double-escapes {dbl}")
