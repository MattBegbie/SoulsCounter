#soulsCounter.py

d = [0, 673, 689, 706, 723, 740, 757, 775, 793, 811, 829, 847, 1038, 1238, 1445, 1659, 1882, 2113, 2353, 2601, 2857, 3122, 3395, 3678, 3969, 4270, 4580, 4899, 5228, 5566, 5915, 6272, 6640, 7018, 7407, 7805, 8214, 8633, 9064, 9505, 9956, 10419, 10893, 11379, 11876, 12384, 12904, 13435, 13979, 14535, 15102, 15682, 16274, 16879, 17497, 18127, 18770, 19425, 20094, 20776, 21472, 22181, 22903, 23640, 23390, 25153, 25931, 26723, 27530, 28351, 29186, 30036, 30900, 31780, 32675, 33584, 34509, 35449, 36405, 37377, 38364, 39376, 40385, 41420, 42472, 43539, 44623, 45723, 46841, 47975, 49125, 50293, 51478, 52681, 53901, 55138, 56393, 57665, 58956, 60265, 61591, 62936, 64299, 65681, 67082, 68939, 69939, 71395, 72871, 74367, 75881, 77415, 78968, 80542, 82134, 83747, 85380, 87033, 88707, 90400, 92115, 93850, 95605, 97382, 99179, 100998, 102838, 104699, 106582, 108486, 110413, 112360, 114330, 116322, 118337, 120373, 122432, 124513, 126618, 128744, 130894, 133067, 135263, 137483, 139725, 141992, 144282, 146595, 148933, 151292, 153680, 156090, 158524, 160983, 163466, 168507, 171065, 173648, 176257] 
# first of all tkinter sucks

#get the user input
currLevel = int(input("What is your current level?"))
desLevel = int(input("What is your desired level?"))

#figure out the math

print("current Level:{0}".format(currLevel))
print("desired Level:{0}".format(desLevel))

levelDifference =  desLevel - currLevel
print("Level Difference:{0}".format(levelDifference))
requiredSouls = 0
for i in range(currLevel-1, desLevel-1):
    print("Current Required:{0} Current Level:{1} Current Level Cost:{2}".format(requiredSouls, i, d[i]))
    requiredSouls = requiredSouls + d[i]

print("Final:{0}".format(requiredSouls))
input("Press enter to exit")