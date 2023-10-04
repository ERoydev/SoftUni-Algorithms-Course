health = int(input())
initial_health = health

passed = set()

while True:
    immune_bonus = 1
    virus = input()
    if virus == "end":
        break

    virus_strength = sum([ord(x) for x in virus]) // 3

    if virus_strength > health:
        print(f"Immune System Defeated.")
        raise SystemExit

    if virus in passed:
        immune_bonus = 3

    seconds = len(virus) * virus_strength // immune_bonus
    minutes = seconds // 60
    secs = seconds - minutes * 60
    passed.add(virus)
    health -= seconds

    print(f"Virus {virus}: {virus_strength} => {seconds}")
    print(f"{virus} deafeated in {minutes}m {secs}s.")
    print(f"Remaining health: {health}")