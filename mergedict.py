import collections
super_dict = collections.defaultdict(list)

newDict = {"Gpt": {"Trunk": {"E2H": ["BSW_changed", "dce"],"U2A16": "avcadd"}}}
mergeDict = {"Gpt": {"Trunk": {"E2H": "BSW_changed"}}}
dicts = [newDict]
for d in dicts:
    for moduleKey, moduleValue in d.items():  # d.items() in Python 3+
        if None != mergeDict.get(moduleKey):
            pass
        else:
            mergeDict[moduleKey] = moduleValue
            break
        for repoKey, repoValue in moduleValue.items():
            if None != mergeDict.get(moduleKey).get(repoKey):
                pass
            else:
                mergeDict[moduleKey][repoKey] = repoValue
                break
            for deviceKey, deviceValue in repoValue.items():
                print(mergeDict.get(moduleKey).get(repoKey).get(deviceKey))
                if None != mergeDict.get(moduleKey).get(repoKey).get(deviceKey):
                    mergeDict[moduleKey][repoKey][deviceKey] = list(mergeDict.get(moduleKey).get(repoKey).get(deviceKey)) + list(deviceValue)
                else:
                    mergeDict[moduleKey][repoKey][deviceKey] = [deviceValue]




print(mergeDict)