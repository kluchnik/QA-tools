#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time

text = """
Stars are born, they live, and they die. The sun is no different, and when it goes, the Earth goes with it. But our planet won't go quietly into the night.

Rather, when the sun expands into a red giant during the throes of death, it will vaporize the Earth.

Perhaps not the story you were hoping for, but there's no need to start buying star-death insurance yet. The time scale is long — 7 billion or 8 billion years from now, at least. Humans have been around only about 40-thousandth that amo$

So what happens when the sun goes out? The answer has to do with how the sun shines. Stars begin their lives as big agglomerations of gas, mostly hydrogen with a dash of helium and other elements. Gas has mass, so if you put a lot of it$

There's enough hydrogen to keep this process going for billions of years. But eventually, almost all of the hydrogen in the sun's core will have fused into helium. At that point, the sun won't be able to generate as much energy, and wil$

That helium core, though, will start to collapse in on itself. When it does, it releases energy, though not through fusion. Instead it just heats up because of increased pressure (compressing any gas increases its temperature). That rel$

A 2008 study by astronomers Klaus-Peter Schröder and Robert Connon Smith estimated that the sun will get so large that its outermost surface layers will reach about 108 million miles (about 170 million kilometers) out, absorbing the pla$

On the bright side, the sun's luminosity is increasing by a factor of about 10 percent every billion years. The habitable zone, where liquid water can exist on a planet's surface, right now is between about 0.95 and 1.37 times the radiu$

As the water gets broken down, the hydrogen will escape to space and the oxygen will react with surface rocks. Nitrogen and carbon dioxide will probably become the major components of the atmosphere — rather like Venus is today, though $

But even Mars won't last as a habitable planet. Once the sun becomes a giant, the habitable zone will move out to between 49 and 70 astronomical units. Neptune in its current orbit would probably become too hot for life; the place to li$

One effect Schröder and Smith note is that stars like the sun lose mass over time, primarily via the solar wind. Planets' orbits around the sun will slowly expand. It won't happen fast enough to save the Earth, but if Neptune edges far $

Eventually, though, the hydrogen in the sun's outer core will get depleted, and the sun will start to collapse once again, triggering another cycle of fusion. For about 2 billion years the sun will fuse helium into carbon and some oxyge$

Since white dwarfs are heated by compression rather than fusion, initially they are quite hot — surface temperatures can reach 50,000 degrees Fahrenheit (nearly 28,000 degrees Celsius) — and they illuminate the slowly expanding gas in t$
"""

sections = text.split("\n\n")

for i, section in enumerate(sections):
    words = section.split(" ")
    line = ""
    for word in words:
        line_length = len(line)
        if line.rfind("\n") > 0:
            line_length -= line.rfind("\n")

        if line_length > 100:
            print(line)
            line = ""
            time.sleep(0.3)

        if line:
            line += " "
        line += word

    if line:
        print(line)

    if i < (len(sections) - 1):
        print()

        correct_answer = None
        print("Want to continue? y/n")
        while correct_answer is None:
            answer = input()
            if not (answer in ["y", "n"]):
                print("put correct answer")
            else:
                correct_answer = answer

        if correct_answer == "y":
            # just continuing
            pass
        elif correct_answer == "n":
            print("Bye bye!")
            break

