import random

from cloudbot import hook


@hook.command("drug","pill")
def drug(text, nick, message):
	"""Gives a User a drug <user>"""
	target = text.strip()

	# Use {N} to represent the person's nickname who is performing the action
	# Use {T} to represent the person's nickname who is the target of the action
	drug = [
		"{N} Hands {T} A bottle of Vicodin",
		"{N} Hands {T} A bag of OxyContin",
		"{N} Hands {T} A Moriphine Drip",
		"{N} Hands {T} Some Fentanyl",
		"{N} Hands {T} A Bottle of Codeine"
            ];

	out = "{}".format(random.choice(drug))
	out = out.replace("{N}", nick)
	out = out.replace("{T}", target)

	message(out)
