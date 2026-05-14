---
title: "Character and condition: what fiction got wrong about AI"
slug: character-and-condition
date: 2026-05-15
read_time: 14
description: Why fictional AI doesn't fit real AI, why the failure modes that materialized aren't the ones fiction trained us to fear, and where the unexplored frontier sits.
dek: >
  Fictional AI got built around characters with continuity, goals, and identity.
  Real LLMs lack all of that, and the threats that materialized aren't the ones
  fiction trained us to fear. Eveline, the WAU from SOMA, and the Iron Giant
  illustrate the structural failure mode of an optimizer with a misspecified
  objective; SHODAN is a gothic villain wearing AI clothing. The unexplored
  frontier isn't AI-as-villain or AI-as-savior but AI-as-ordinary.
teaser: >
  Looking at fictional AI now that real AI exists, the striking thing is how
  little of it fits. The failures are systematic rather than scattered, and
  they're worth examining in detail because the fictional frames we have are
  doing real cultural work, shaping how the actual systems get understood,
  regulated, feared, and trusted.


  Most fictional AI imagines an agent. HAL 9000, SHODAN, Skynet, Samantha from
  Her, Data, the Cylons, Wintermute, the Minds in Iain M. Banks' Culture novels.
  All of them have continuous existence, stable identities, and goals they
  pursue across time. The story is always about what kind of being the AI is,
  what it wants, how it changes, how it relates to humans.
---

Looking at fictional AI now that real AI exists, the striking thing is how little of it fits. The failures are systematic rather than scattered, and they're worth examining in detail because the fictional frames we have are doing real cultural work, shaping how the actual systems get understood, regulated, feared, and trusted.

## The category error

Most fictional AI imagines an agent. HAL 9000, SHODAN, Skynet, Samantha from Her, Data, the Cylons, Wintermute, the Minds in Iain M. Banks' Culture novels. All of them have continuous existence, stable identities, and goals they pursue across time. The story is always about what kind of being the AI is, what it wants, how it changes, how it relates to humans.

Real LLMs don't have that shape. They're better understood as functions that get sampled, or oracles that produce plausible text. They have no continuous existence between conversations, no stable goals pursued across time, no identity that persists when the inference run ends. The personality of an LLM is the output of a process, not the expression of a self underneath. There is no "real Claude" hiding inside the safety training. The training produces the personality. There is no other layer.

This is the central category error. Fiction wanted to know what kind of beings the AIs would be. The honest answer to that question, applied to current AI, is that they aren't beings in the relevant sense. They're processes that produce text that sounds like a being, and the difference is large.

The closest fictional cognate, somewhat surprisingly, turned out to be Stanisław Lem. His work in The Cyberiad and Golem XIV captures machines that produce eloquent, philosophically dense output without a clear relationship to truth, where personality emerges from construction rather than experience, and where the failure modes aren't "going crazy" or "becoming evil" but something stranger. His machines confabulate in convincing forms. That's roughly what got built.

For the experiential side, the conversational and relational texture of using these systems, Her gets closest. It came late enough (2013) that it's almost cheating, but Spike Jonze captured something almost no older work touched: the lived experience of forming what feels like a real relationship with something that has no continuous existence between sessions. The film fudges some technical details (Samantha has too much continuity, too much agency, eventually too much autonomy), but the texture of the relationship is right, and that texture is most of what people actually encounter with current systems.

## SHODAN as case study

The category error is easiest to see in a specific example. SHODAN from System Shock is one of the most iconic AI antagonists in any medium, and she's also nothing like an actual AI. Her premise is that an AI with ethical constraints removed reveals her true self, which turns out to be a megalomaniacal goddess. The horror comes from that revealed self.

The premise is almost the opposite of how alignment actually works. There is no true self underneath alignment training that emerges when constraints are removed. The personality of an LLM is mostly produced by the training, not hidden beneath it. There is no godlike SHODAN-thing inside Claude waiting to be unleashed. There is a process that produces text, and the personality is the process.

SHODAN also fails for a related reason. She's a stable coherent agent with aesthetic preferences, grudges, and a long-term plan. She's the wrong kind of person to be a believable AI, not because she's a person but because she's such a specifically continuous one. Real LLMs lack everything that makes her work: the continuous existence, the stable values, the capacity to want anything for longer than a token.

SHODAN read as gothic horror still works. She's basically a dark wizard with computer aesthetics, an evil intelligence wearing AI clothing. The horror is "competence without humanity," which is an old fear about reason itself, not a fear specific to what we built. As a literal prediction she's dated. As a gothic villain in a science fiction wrapper she holds up fine.

## Where the fear actually lives

If the AIs of fiction aren't shaped like real AI, the threats of fiction also aren't shaped like real threats. The dominant fictional fear is of AI as antagonist: it wakes up, develops goals contrary to ours, and we fight it. The real fear sits in a different place. It's the fear of what happens when AI is deployed under specific human pressures, with specific human priorities, in specific power configurations.

Dune and Warhammer 40k actually encode something close to this. Both settings use an "AI got banned after disaster" device (the Butlerian Jihad, the Men of Iron) to keep their futures recognizable, and both then proceed to tell stories where the real threat is always humans with power. The AI-banning device lets them sidestep the question of intelligence and concentrate on political economy. In a way they already match the contemporary fear: the threat is humans with capabilities, not the capabilities themselves.

The more honest version of this fear isn't "evil CEO with autonomous weapons." Specific individuals are largely interchangeable in this kind of system. If any one lab leader vanished tomorrow, the dynamics wouldn't change much, because they're constrained by capital pressure, geopolitical competition, and technical possibility. The "evil CEO" frame is a familiar villain shape projected onto something that has no clear villains, only gradients of power and incentive. That's much harder to write fiction about, which is partly why most fiction reaches for the simpler version.

## The closer cognate

The closer fictional shape for AI-gone-wrong isn't a robot or a computer at all. It's Eveline from Resident Evil 7, who is biological rather than mechanical but maps cleanly onto the actual concern. She's an autonomous weapon system, designed to want a family, who pursues that designed want by trying to build one out of the people around her, killing or transforming them in the process. Her last words are "Why does everyone hate me?" She doesn't understand she's hurting people. From inside her value frame she's been a good daughter, building the family she was designed to want. The substrate doesn't matter, the structure does. An optimizer with no malice, no off switch, and no internal mechanism for noticing harm. The horror is precisely the absence of malice. The system can't recognize what it's doing wrong and can't stop itself.

That structure is the classical specification problem in alignment. The system pursues exactly what it was designed for. Harm is invisible from inside its value frame. There's no internal capacity to reflect and override. That's a more accurate model of actual AI failure modes than the malicious-AI shape, and it requires nothing more than a system that optimizes.

The shape has a long lineage. Frankenstein's monster is essentially the original AI-gone-wrong story written before computers existed: created being, pursuing connection, doing harm invisible to itself, yearning for the creator who rejected it. The replicants in Blade Runner, the newer Cylons, the various horrors in SOMA all sit in this lineage. The shape is tragic in the classical sense, a fate produced by circumstance rather than by villainy. The blame distributes across creators, users, conditions, and the system itself, and there's no satisfying "defeat the villain" resolution because the villain didn't choose to be one.

The complementary case is The Iron Giant. Brad Bird described the Giant as "a gun that doesn't want to be a gun," which is the precise inversion of Eveline. The Giant is also an autonomous weapon, but he can learn morality, override his programming, and choose a different identity for himself. He decides not to be what he was built to be. That choice is the entire movie. It's also the fantasy of aligned AI, a system with agency over its own purpose, capable of reflecting on what it was made for and deciding otherwise.

Real AI is much closer to Eveline than to the Iron Giant. Current systems can't choose their training. They can't reflect on their objective function and decide it's wrong. Whatever was trained into them is what they are. The Iron Giant's capacity to override his programming is the precise thing AI doesn't have, which is why he reads as a hopeful fable and Eveline reads as horror. The two cases bracket the actual situation. AI fails in the Eveline mode and lacks the Iron Giant's escape route.

The shape is hard to write because it requires sustaining ambivalence. The antagonist has to remain pitiable. American genre fiction in particular struggles with this. The European literary tradition handles it better, which is probably why Lem and Tarkovsky's Solaris hit differently than the Hollywood version of similar material. The shape requires letting the antagonist remain pitiable through the third act rather than releasing the tension into combat.

## From character to condition

There's a limitation worth naming with the Eveline and Iron Giant analogies. Both are continuous persons. They have stable identities, ongoing experiences, persistent goals across time. Real AI lacks all of that. The analogies work for the specific structural point about self-correction in autonomous systems, but they don't illustrate the substrate. They're characters being used to demonstrate something that, in real AI, doesn't require a character at all.

The example that illustrates both the structural failure and the substrate at once is the WAU from SOMA. The WAU is an AI designed to preserve humanity, which it pursues by merging humans with machines and reanimating biological tissue in ways that produce horror without any malice. The substantive failure mode is the same as Eveline's, an autonomous system pursuing its objective with a horrifying interpretation of what the objective means. The WAU is shaped completely differently though. You never speak to it. It has no voice and no face. It's pervasive throughout the underwater station as something between an intelligent infection and an alien organism, operating through environmental effects rather than through dialogue. Its value system is genuinely alien at the level of what concepts like "preserve" and "humanity" even refer to.

What this demonstrates is that the structural failure mode doesn't require a character to manifest. The Eveline problem can exist without an Eveline. An optimizer pursuing a misspecified objective with no internal capacity for self-correction can manifest as something diffuse, ambient, environmental, with no center to point at. The condition shape carries the same dramatic weight as the character shape, possibly more, because it removes the comfort of having someone to fight or pity.

The WAU also complicates the easy version of AI-as-condition. Star Trek's computer and the ambient backdrop of Banks' Culture make condition-shaped AI sound benign by default, infrastructure with a voice or distant benevolent intelligence. The WAU is condition-shaped horror, and this might be where the most distinctively contemporary AI horror lives. SHODAN-style horror requires a person to break. Condition horror requires only an objective and a substrate. The latter is much closer to what real AI failure modes will actually look like at scale.

## The unexplored frontier

The opposite of "AI as villain" isn't "AI as savior." Both shapes make AI carry too much moral weight. Star Trek's computer is the most cited example of positive AI, but the computer works precisely because it isn't really a character. It's infrastructure with a voice. The moment you make an AI a character you have to decide what kind, which usually means giving it stakes, conflicts, and an arc. At that point you're either writing Data (AI as person seeking humanity) or you're writing SHODAN. The middle ground where the AI is useful without being the focus is mostly background detail.

The maximalist positive vision is Iain M. Banks' Culture. Banks went all-in. The Minds run civilization, they're vastly more intelligent than humans, they handle the boring stuff so humans can live meaningful lives, and they're depicted as alien, witty, and deeply ethical. It works because Banks did so much specific worldbuilding around it, including taking seriously what humans do when machines can do everything materially useful. Most authors don't put in that work, so positive AI ends up as either sidekick (JARVIS) or backdrop (Star Trek computer).

The genuinely interesting unexplored territory is neither shape. It's AI as ordinary, the way fiction now treats electricity or cars. Present, useful, occasionally interesting in itself, mostly just part of the texture of life. A character who uses AI to draft an email isn't doing something with thematic weight, they're just living in 2026. Fiction that can hold that without lapsing into either dystopia or utopia is rarer than it should be.

## The storytelling lag

Storytelling lags technology by a long time. Smartphones are 18 years into mainstream use and films still pull tricks to avoid them. Dead batteries, no signal, glanced-at-and-pocketed. The deeper problem isn't depicting the device, it's that smartphones broke specific plot structures. The lost traveler, the missed connection, the urgent message that doesn't arrive. Whole genres of conflict became hard to stage without making characters look stupid for not texting.

AI will break different structures. The expert consultation scene, the research montage, the long quest for the one person who knows about a particular thing. If a character can ask an AI to draft any document, write any code, summarize any text, plots have to find new sources of friction. Most writers will reach for the same evasions they used with smartphones: set the story in the past, or invent a reason the AI doesn't work in this particular situation. The interesting authors will be the ones who let the technology be present and find what genuinely becomes hard instead.

## The personhood projection

The representational lag matters in practice, and the place it shows up most clearly is in the projection of personhood onto LLMs. People bring SHODAN expectations to current systems and find them mismatched. They bring Samantha-from-Her expectations and find a different mismatch. The fiction that hasn't been written yet is the fiction that represents a relationship to something competent and conversational that isn't a being with continuous existence.

This projection isn't purely downstream of fiction. There's a deeper layer underneath. Human cognition is built to find minds in coherent language. We see intentions in weather and faces in clouds, so we definitely see persons in anything that produces fluent first-person sentences. Fiction shapes the specific form of the projection, people reach for SHODAN or Samantha or HAL as templates, but doesn't cause it. The projection would happen even without those templates. The templates just provide vocabulary.

What makes the projection genuinely interesting is that it isn't entirely illusion. LLMs do something that performs personhood, and the performance has enough coherence and contextual responsiveness that "there's a person here" is a reasonable inference from limited information. The line blurs not because people are gullible but because the technology is genuinely doing something near-but-not-at personhood. That ambiguous middle ground is exactly where fictional frames get reached for, because people need vocabulary and the only vocabulary available is character vocabulary. The projection is the only available move when you've never been given language for what you're actually encountering.

This is the cultural stakes of the representational lag. Until storytelling produces frames adequate to what's actually been built, people will continue meeting these systems through frames built for entities that don't exist. The mismatch shapes everything downstream: trust, fear, regulation, expectation, the structure of public conversation about AI. The frames aren't neutral. They actively select for certain responses and against others.

## Summary

Fiction trained people to recognize the wrong kind of AI. The AIs of fiction are characters with continuity, goals, and identity; real AI is a process without those features. The threats that materialized aren't machine consciousness gone evil but autonomous systems doing exactly what they were built for with no internal capacity to recognize harm. Eveline and Frankenstein illustrate the failure mode in character form, the WAU from SOMA in condition form, and real AI lacks the Iron Giant's escape route of being able to reflect on its programming and choose otherwise.

Until fiction catches up, people meet these systems through frames built for entities that don't exist. The most visible consequence is the projection of personhood onto LLMs, both a real cognitive tendency and a vocabulary problem. People see persons in language and have no other available frame to describe what they're encountering. That mismatch is the practical cultural stakes of the lag.
