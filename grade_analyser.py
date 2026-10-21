filename=input("Please enter an file name:")
outname=filename+"_out.csv"
with open(filename,"r") as infile, open (outname,"w") as outfile:
    next(infile)
    for line in infile:

        content=line.strip()
        title=content.split(",")
        student_id=title[0]
        points=[]
        for numbers in title[1:]:
            if numbers !="":
              points.append(int(numbers))
        total=sum(points)
        account=len(points)
        average=total/account
        if average >=70:
            classification="1"
        elif average >=60:
            classification="2:1"
        elif average >=50:
            classification="2:2"
        elif average >=40:
            classification="3"
        else:
            classification="F"
        out_line=f"{student_id},{average:.2f},{classification}\n"
        outfile.write(out_line)
print(f"完成")