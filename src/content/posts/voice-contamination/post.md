---
title: "Voice contamination in prompts"
slug: voice-contamination
date: 2026-05-18
description: What happens when a prompt's prose style conflicts with its instructions, and why the prose style usually wins.
dek: >
  A prompt does two things at once. It states instructions, and it demonstrates
  a writing style. When the two pull in different directions, the demonstration
  tends to dominate, because every token in the prompt contributes to the
  conditioning while the rule occupies only a sentence.
teaser: >
  A prompt is two pieces of evidence about how to write: the rule, and the
  prose around it. When the two pull in different directions, the prose
  almost always wins.
---

You write a prompt that forbids em dashes. The model uses em dashes anyway.

The prompt is doing two things at once. It says what to write, and it shows what writing here looks like. The model takes instruction from both. When they line up, the rule holds. When they pull in different directions, the example tends to dominate, because the example is dispersed across every token of the prompt while the rule occupies a single sentence.

## Prompts are also writing samples

A prompt is a sample of text that sits in the context window next to whatever the model will generate next. Every token in the prompt enters the conditioning distribution for the next token. A small portion of those tokens are explicit instructions about how to write. Most are demonstration. The model reads both as data about the document.

If a careful paragraph forbids em dashes and the surrounding prose contains a single em dash, the model has read both. In context, the em dash example sits closer to the question "what does writing here look like?" than the prohibition sits to "what should I produce?"

## Amplification

The interaction is worse than imitation. The model exaggerates patterns it finds in the prompt; a feature used once in the source tends to recur with higher frequency in the response.

I have watched a single parenthetical aside in a prompt turn into parenthetical asides in every sentence of the response. One bulleted list in a "voice guidelines" section pulls bulleted output across sections that called for prose. A single rhetorical question used to set up a paragraph produces rhetorical question after rhetorical question in the answer. The behavior looks like the model concentrating on the modal features of the prompt and reproducing them at higher frequency than they appeared in the source.

The em dash is the most recognizable case because of how heavily it appears in the wider corpus of AI-generated text. Forbidding it in a prompt that still contains one produces the exact effect the forbidding was meant to prevent.

## The same dynamic at the structural level

The amplification operates above the sentence level. The model picks up structural patterns and applies them the same way.

If every section of your prompt follows the same shape (header, framing sentence, bulleted list), the output locks into that shape regardless of whether each section's content actually fits. If your "examples" section is six examples in a row, the model interprets "give an example" as "give six." If your instructions vary sentence length across short and long, the output varies; if every sentence in the prompt is medium-length, the output averages to medium and stays there.

The prompt is part of the same document the response will continue. Style and structure are inherited. The model takes them from the context it's been handed.

## Writing prompts the way you want output written

The practical implication is straightforward. Write the prompt the way you want the output written.

Cut em dashes and filler hedges from prompts the way you cut them from drafts. Vary sentence length within sections. Mix prose and lists based on what each section needs. If you are instructing for tone, demonstrate the tone in the surrounding prose. If you are instructing for structure, show the variety you want by varying the prompt's own structure.

In my projects, the voice section of a prompt and the prose around it have to match. Here is the voice section from the orchestrator in one of them, Find Your Canvas:

```
## Voice

Be concise and conversational. Talk about the work, not about yourself or the process. A response that opens with an observation about the image or a creative suggestion is stronger than one that opens with what you are about to do.

Avoid patterns that signal generated text:
- Filler and hedging: "It's worth noting," "That said," "Importantly"
- Performative enthusiasm: "Great choice!", "Love it!" React to the work, not the user.
- Restating the request before acting
- Starting every message with "I" or a direct reference to what the user said
- Em dashes. Use commas, colons, semicolons, parentheses instead.
- Ending every response with a numbered menu of options in your prose. If you have a recommendation, make it. If the next move is open, ask one focused question.

Vary how you open and organize responses. The same structure repeated across turns compounds into a recognizable template. If your last response opened with an observation and ended with a question, open the next one differently.
```

The bullet list states what to avoid. The prose around the list demonstrates the rules in action. No em dashes. No hedges. Sentence length varies. The instruction about response shape compounding is itself written without the patterns it warns about.

A prompt that reads like a careful human wrote it produces output that reads like a careful human wrote it. A prompt that contains AI-voice markers produces more of them regardless of what the rules around them say.

## What this leaves room for

Direct instructions still do real work. They orient the model and set explicit constraints. Style and structure operate alongside them on a separate channel, reaching the model with the strength of every token in the document.

When a recurring voice problem in output makes you want to add a new rule, audit the prompt's own voice first. The fix is usually upstream of the rule.
