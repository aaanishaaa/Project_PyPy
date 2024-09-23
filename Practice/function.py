# def greet_with(name, location):
#     print(f"Hey {name}!")
#     print(f"What is it like in {location}")

# greet_with(location="delhi", name="Anisha")

def calculate_love_score(name1,name2):
    combined_name=name1+name2
    lower=combined_name.lower()
    
    t=lower.count("t")
    r=lower.count("r")
    u=lower.count("u")
    e=lower.count("e")
    
    first=t+r+u+e
    first1=str(first)
    l=lower.count("l")
    o=lower.count("o")
    v=lower.count("v")
    e=lower.count("e")

    second=l+o+v+e
    second1=str(second)
    
    final=first1+second1
    print(final)
    
calculate_love_score("Kanye West", "Kim Kardashian")