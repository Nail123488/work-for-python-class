states={"red":4 "red_amber":3, "green":5, "amber":3}
sequence=["red", "red_amber", "green", "amber"]
steps=int(input())
begin_idx=0
time_state=0
for time in range(steps):
    kind=sequence[begin_idx]
    print(f"Time {time:03d} State {kind}")
    time_state+=1
    if time_state>=states[kind]:
        begin_idx+=1
        if begin_idx>=len(sequence):
            begin_idx=0
        time_state=0